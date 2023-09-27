# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:38:29 2023

@author: riach
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import random
import xgboost as xgb
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)

def word_divide_char(inputs):
    characters=[]
    for i in inputs:
        characters.append(i)
    return characters

vectorizer=TfidfVectorizer(tokenizer=word_divide_char)
df=pd.read_csv('C:/Users/riach/Projects/Checking Password Strength/cleaned_data.csv')
df.dropna(inplace=True)
passwords_tuple=np.array(df)
random.shuffle(passwords_tuple)
y=[labels[1] for labels in passwords_tuple]
X=[labels[0] for labels in passwords_tuple]
X=vectorizer.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)  #splitting
xgb_classifier = xgb.XGBClassifier()
xgb_classifier.fit(X_train,y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from HTML form
        input_text = request.form['text_input']  # Assuming a single input field with 'text_input' as the name

        # All necessary preprocessing on the input text
        
        
        X_predict=np.array([str(input_text)])
        X_predict=vectorizer.transform(X_predict)

        # Make predictions using the loaded model
        # Ensure that the input format matches the format expected by your model
        prediction = xgb_classifier.predict(X_predict)

        # Return the prediction as JSON
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)








