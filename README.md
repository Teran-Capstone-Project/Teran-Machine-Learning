#👥 Teran-Machine-Learning - Capstone Project Bangkit 2024
Group = C241-PS061

Member =

    (ML) M281D4KX3241 – Tasya Ade Amelia 
    (ML) M129D4KX2350 – Eka Sulistyaningsih
    (ML) M004D4KY2039 – Royhan Nurisalam
    (CC) C193D4KY0367 – Muhammad Dariaz Zidane
    (CC) C129D4KX0459 – Lusy Damayanti
    (MD) A247D4KY3887 – Muhammad Ervan Fadillah 
    (MD) A524D4KY4068 – Arry Kusuma Putra

# Teran App
Teran App is an application designed to help college students manage stress by providing resources and tools for stress detection and management. The app features a machine learning algorithm to assess stress levels 📊, articles on stress management 📚, and a networking platform for users to share their experiences 🗣️. It is built using various technologies, including TensorFlow 🧠, Firebase for cloud integration ☁️, and a user-friendly interface designed with material components 💎.

## EDA & Data Preparation
Our dataset include 3 type of stress (anxiety, depressed, panicking) in Indonesia and total dataset is 500 data.

## Data Processing
The data processing steps we follow include loading the dataset, performing label encoding on categorical variables, separating the dataset into features and labels, and splitting the data into training and testing sets.

## Machine Learning Model
We use a Neural Network model with TensorFlow and Keras for training data and create layer model (dense layer and dropout layer). We achieved an accuracy of > 99% for students stress detection and saved the model with keras model h5.

## Model Deployment
After model already, we use tensorflow lite to convert the model and ready deploy to Android Studio.
