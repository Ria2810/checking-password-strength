# Password Strength Checker

This GitHub repository contains a project for checking the strength of entered passwords, classifying them as low, medium, or high strength. The project involves data preprocessing, model training, and deployment of a web application for password strength prediction.

## Table of Contents
1.Introduction
2. Data
3. Data Preprocessing
4. Model Training
5. Deployment
6. Usage
7. Contributing

## <ins>Introduction </ins>
The goal of this project is to assess the strength of passwords based on their complexity and structure. Passwords are categorized into three classes: low strength, medium strength, and high strength. This classification is valuable for enhancing online security and helping users create stronger passwords.

## <ins>Data</ins>
The dataset used for this project consists of two columns:

- password: The password to be evaluated.
- strength: The strength level of the password (0 - low, 1 - medium, 2 - high).
## <ins>Data Preprocessing</ins>
Data preprocessing steps include:

- Handling missing values: Eliminating rows with missing values.
- Data splitting: Separating input features (passwords) and target labels (strength).
- Text vectorization: Using TfidfVectorizer to convert text data into numerical form.
- Data splitting: Dividing the dataset into training and testing sets.
## <ins>Model Training</ins>
Three machine learning algorithms were employed for password strength prediction:

- Logistic Regression
- Multinomial Naive Bayes
- XGBoost
Model evaluation was performed using R-squared. The model with the best performance was selected, and a serialized pickle file was created to save the trained model.

## <ins>Deployment</ins>
A web application was developed using Flask to deploy the trained model. Users can enter a password into the application, click the submit button, and receive results indicating whether the password is strong, medium, or weak.

## <ins>Usage</ins>
To use the password strength checker, follow these steps:

- Clone this repository to your local machine.
- Install the required dependencies using pip install -r requirements.txt.
- Run the Flask application: python app.py.
- Access the application through your web browser.
## <ins>Contributing </ins>
Contributions to this project are welcome. If you have suggestions for improvements or new features, please feel free to submit a pull request.
