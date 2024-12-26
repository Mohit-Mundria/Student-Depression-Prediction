import joblib
import pandas as pd
model=joblib.load(r"C:\Users\temp\Depression_RandomForestClassifier")
ss=joblib.load(r"C:\Users\temp\StandardScaler_Depression")

def predict_depression():
    Id=float(input("Enter the ID of the Student:"))
    Age=float(input("Enter the Age of the Student: "))
    Academic_Pressure=float(input("Enter the Academic Pressure of the Student( Range: 0-5): "))
    CGPA=float(input("Enter the CGPA of the Student: "))
    Study_Satisfaction=float(input("Enter the Study Satisfaction of the Student(Range: 0-5): "))
    Study_Hours=float(input("Enter how many hrs the student study: "))
    Financial_Stress=float(input("Enter does the student have financial stress: (0-5)"))
    City_Encoded=float(input("Enter the City of Student: ['1 for Visakhapatnam', 2 for 'Bangalore', 3 for 'Srinagar', 4 for 'Varanasi', 5 for 'Jaipur',6 for 'Pune', 7 for 'Thane', 8 for 'Chennai', 9 for 'Nagpur', 10 for 'Nashik', 11 for 'Vadodara',12 for 'Kalyan', 13 for 'Rajkot',14 for 'Ahmedabad',15 for 'Kolkata', 16 for 'Mumbai', 17 for 'Lucknow',18 for 'Indore', 19 for 'Surat', 20 for 'Ludhiana',21 for 'Bhopal', 22 for 'Meerut', 23 for 'Agra',24 for 'Ghaziabad',25 for 'Hyderabad',26 for 'Vasai-Virar', 27 for 'Kanpur', 28 for 'Patna',29 for 'Faridabad', 30 for 'Delhi']"))
    Gender_encoded=float(input("Enter Gender of the Student[1 for Male, 0 for Female]: "))
    Degree_encoded=float(input("Enter the Degree the Student Persuing: {'B.Pharm':1, 'BSc':2, 'BA':3, 'BCA':4, 'M.Tech':5, 'PhD':6, 'Class 12':7, 'B.Ed':8,'LLB':9, 'BE':10, 'M.Ed':11, 'MSc':12, 'BHM':13, 'M.Pharm':14, 'MCA':15, 'MA':16, 'B.Com':17,'MD':18, 'MBA':19, 'MBBS':20, 'M.Com':21, 'B.Arch':22, 'LLM':23, 'B.Tech':24, 'BBA':25,'ME':26, 'MHM':27, 'Others':28}"))
    Family_History_of_Mental_Illness_encoded=float(input("Tell something about Student Mental Health: [0 for No, 1 for Yes]  "))
    Sleep_Duration_encoded=float(input("Enter how many Student take Sleep: "))
    Dietary_Habits_encoded=float(input("Tell about Dietary Habit of Student [0 for Healthy, 1 for Moderate, 2 for Unhealthy]: "))
    Have_you_ever_had_suicidal_thoughts_encoded=float(input("Student try any suicidal attempt [1 for yes, 0 for No]: "))
    col=['id','Age','Academic Pressure','CGPA', 'Study Satisfaction','Study Hours','Financial Stress','City_Encoded', 'Gender_encoded' ,'Degree_encoded',	'Family History of Mental Illness_encoded'	,'Sleep Duration_encoded'	,'Dietary Habits_encoded' 	,'Have you ever had suicidal thoughts ?_encoded']
    data= pd.DataFrame([[Id,Age,Academic_Pressure,CGPA,Study_Satisfaction,Study_Hours,Financial_Stress,City_Encoded,Gender_encoded,Degree_encoded,Family_History_of_Mental_Illness_encoded,Sleep_Duration_encoded, Dietary_Habits_encoded,Have_you_ever_had_suicidal_thoughts_encoded]],columns=col)
    standard_data=ss.transform(data)



    prediction=model.predict(standard_data)


    if prediction[0]==1:
        print("The Student is likely in Depression. Plz take care of the Student.")
    else:
        print("The Student is not in depression.")

if __name__=="__main__":
    predict_depression()
    
