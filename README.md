# mlops-homework-04
DataTalks: MLOps Zoomcamp - Homework for Module 4

## 📝 Description

This Python script uses a pre-trained scikit-learn model to predict taxi trip durations from data loaded from a specified URL. It processes the data, computes and displays key statistics, and saves the results with unique identifiers to a Parquet file. The script operates dynamically from the command line, accepting year and month as parameters to fetch and analyze NYC taxi data for specific periods. It accesses AWS credentials from the .env.aws file and stores the Parquet file in an S3 bucket.

## 🔧 Instructions to Run

### 1. Store AWS Credentials in a file: 'env.aws'

```bash
AWS_ACCESS_KEY_ID=<YOUR-KEY-ID>
AWS_SECRET_ACCESS_KEY=<YOUR-SECRET-KEY>
```

### 2. Build the Docker Image

```bash
docker build -t duration-predictions .
```

### 3. Run the Docker Image

The first command line argument is for year, the second is for month, and the third argument is the name of your S3 bucket.

```bash
docker run --env-file .env.aws duration-predictions <YEAR> <MONTH> <YOUR-BUCKET-NAME>
```

Example Command: 
```bash
docker run --env-file .env.aws duration-predictions 2023 5 mlops-bucket-mannerow
```