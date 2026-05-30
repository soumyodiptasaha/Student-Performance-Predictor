# Student Performance Predictor

## Overview

Student Performance Predictor is a Machine Learning web application that predicts a student's final grade (G3) based on academic and behavioral factors such as study time, failures, absences, and previous grades.

The project includes data analysis, model training, a Flask web application, and cloud deployment using Render.

## Features

* Predict student final grade (G3)
* Performance classification
* Grade classification (A, B, C, D)
* Student status assessment
* Interactive web interface
* Cloud deployment using Render

## Tech Stack

* Python
* Flask
* Scikit-Learn
* Pandas
* NumPy
* HTML
* CSS
* Git & GitHub
* Render

## Dataset

Student Performance Dataset (UCI Machine Learning Repository / Kaggle)

Features used:

* Study Time
* Failures
* Absences
* G1 (First Period Grade)
* G2 (Second Period Grade)

Target:

* G3 (Final Grade)

## Model Performance

* Algorithm: Linear Regression
* R² Score: 0.91
* Mean Absolute Error (MAE): 0.90

## Live Demo

https://student-performance-predictor-z8td.onrender.com

## Sample Usage

Input:

Study Time = 3
Failures = 0
Absences = 5
G1 = 14
G2 = 15

Output:

Predicted Final Grade (G3): 15.81

Performance: Good 👍

Grade: B

Status: Above Average Student ⭐

## Installation

```bash
git clone https://github.com/soumyodiptasaha/Student-Performance-Predictor.git

cd Student-Performance-Predictor

pip install -r requirements.txt

python app.py
```

## Project Structure

Student-Performance-Predictor/

├── app.py

├── train_model.py

├── model.pkl

├── requirements.txt

├── render.yaml

├── data/

├── static/

└── templates/

## Author

Soumyodipta Saha

B.Tech CSE(AI) Student

Institute of Engineering and Management (IEM), Kolkata

## Future Improvements

* Random Forest Regression
* XGBoost Model
* Prediction Confidence Score
* User Authentication
* Database Integration
* Interactive Analytics Dashboard
