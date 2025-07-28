
# 🫀 Heart Disease Prediction Web Application

This is a machine learning–based web application that predicts the likelihood of heart disease using a set of clinical parameters entered by the user. The application features a user-friendly interface with secure login and registration, and it delivers real-time predictions using a trained Naive Bayes model.

## 🔍 Project Overview

This project aims to apply machine learning to support early detection of heart disease. It uses a web interface built with Flask, where users can create an account, log in, enter medical details, and receive instant feedback on their heart health based on the model’s prediction.

## 🚀 Features

- 🔐 User Registration & Login System (MySQL Database)
- 📊 ML Model Trained on Real-World Heart Disease Data
- 🧠 Prediction using Naive Bayes Algorithm
- 🎨 Clean and Responsive UI with Bootstrap
- 📁 Secure Form Handling with Session Management

## 🛠️ Technologies Used

| Category      | Tools/Libraries                        |
|---------------|----------------------------------------|
| Programming   | Python                                 |
| Web Framework | Flask                                  |
| Frontend      | HTML, CSS, Bootstrap                   |
| Database      | MySQL                                  |
| ML Libraries  | NumPy, Pandas, scikit-learn, Pickle    |
| Security      | Werkzeug (for password hashing)        |


## 🧠 Machine Learning Model

- **Algorithm**: Naive Bayes Classifier
- **Accuracy**: ~85%
- **Precision**:84%
- **Recall**:89%
- **F1 Score**: 86%
- **Target**: HeartDisease (0 = No, 1 = Yes)
- **Input Features**: Age, Gender, Chest Pain Type, FastingBS, Cholesterol, RestingECG, MaxHR, Exercise Angina, Oldpeak, ST_Slope.

#👥 User Flow
    1.Register a new user account
    2.Log in to the system
    3.Enter medical details into the form
    4.Click Submit to get prediction results
    5.Log out when done

## 📷 Screenshots

### 🔐 Login Page
![Login Screenshot](assets/login.png)

### 📊 Prediction Page
![Prediction Screenshot](assets/result.png)


