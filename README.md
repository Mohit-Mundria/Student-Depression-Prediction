Depression Prediction Model

This repository contains a Depression Prediction Model built using Python and Machine Learning. 
The model utilizes a Random Forest Classifier to predict whether a student is likely to be in depression based on various input features.

Project Overview

The project aims to identify students who may be experiencing depression by analyzing data collected from them.
This tool can help educational institutions and counselors provide timely support to students in need.

Key Features

Uses a Random Forest Classifier for prediction.
Accepts user input through the console for prediction.
Scales input features using StandardScaler.
Provides an easy-to-use interface for generating predictions.

File Structure

Depression_predict_file.py - Main Python script for taking inputs and making predictions.
Depression_RandomForestClassifier.pkl - Pre-trained model saved using Joblib.
StandardScaler_Depression.pkl - Scaler used to standardize input features.

Dependencies

Make sure you have the following Python libraries installed:
pip install pandas
pip install numpy
pip install scikit-learn
pip install joblib

Run the Python script:

python Depression_predict_file.py

Enter the required inputs when prompted.
Input Features

Feature Description

Example Values
ID, Unique ID of the student: 312
Age, Age of the student: 21
Academic Pressure, Academic stress level (0-5): 1
CGPA, Cumulative Grade Point Average: 6.5
Study Satisfaction, Satisfaction with studies (0-5): 1
Study Hours, Hours spent studying daily: 3
City_Encoded, Encoded city names (1-30): 30 (Delhi)
Gender_encoded, Gender of student (1 = Male, 0 = Female): 1
Degree_encoded, Encoded degree program (1-28): 5 (M.Tech)
Family History of Mental Illness, Mental health history (1 = Yes, 0 = No): 1
Sleep Duration, Average hours of sleep: 7
Dietary Habits, Dietary habits (0 = Healthy, 1 = Moderate, 2 = Unhealthy): 1
Suicidal Thoughts, Previous suicidal thoughts (1 = Yes, 0 = No): 1

Output
The model outputs either:
1 - The student is likely in depression.
0 - The student is not in depression.

Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

License

Contact
For queries or suggestions, please contact:
Email: mundriamohit100@gmail.com

GitHub: Mohit-Mundria

Thank you for visiting this repository!
