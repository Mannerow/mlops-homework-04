# mlops-homework-04
DataTalks: MLOps Zoomcamp - Homework for Module 4

## 📝 Description

This Python script uses a pre-trained scikit-learn model to predict taxi trip durations from data loaded from a specified URL. It processes the data, computes and displays key statistics, and saves the results with unique identifiers to a Parquet file. The script is designed to operate dynamically from the command line, accepting year and month as parameters to fetch and analyze nyc taxi data for specific periods.

## 🔧 Instructions to Run

### 1. Build the Docker Image

```bash
docker build -t duration-predictions .
```

### 2. Run the Docker Image

The first command line argument is for year, and the second is for month. 

```bash
docker run duration-predictions 2023 5
```
