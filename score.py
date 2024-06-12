#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import sys

categorical = ['PULocationID', 'DOLocationID']

def load_model(path='model.bin'):
    with open(path, 'rb') as f_in:
        dv, model = pickle.load(f_in)
        return dv, model

def read_data(filename: str):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def make_predictions(df, dv, model):
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    return y_pred

#Create an aritificial column for ride_id
def create_ride_ids(df, year, month):
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    return df

def save_results(df, y_pred, output_file='results'):
    #Write the ride_id and the predictions to a dataframe with the results
    df_result = pd.DataFrame({
        'ride_id': df['ride_id'],  
        'prediction': y_pred
    })
    #Save it as a parquet
    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
)

def run():
    #Take the year and month from the arguements
    year = int(sys.argv[1])
    month = int(sys.argv[2]) 

    df = read_data(f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02}.parquet")
    dv, model = load_model()
    y_pred = make_predictions(df, dv, model)

    #Std deviation of Duration
    y_pred_series = pd.Series(y_pred)
    std_deviation = y_pred_series.std()
    print("Standard Deviation of Predictions:", std_deviation)

    # Calculate the mean of predictions
    mean_of_predictions = y_pred_series.mean()
    print("Mean of Predictions:", mean_of_predictions)

    # Create an artificial ride_id column
    df = create_ride_ids(df, year, month)
    save_results(df, y_pred, )

if __name__ == '__main__':
    run()
