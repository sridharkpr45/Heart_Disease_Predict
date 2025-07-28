import numpy as np
from flask import Flask, request, render_template, request, redirect, url_for, session
import pickle
import os
#import traceback
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash


db = mysql.connector.connect(
    host="localhost",
    user="root",             # replace with your MySQL username
    password="tiger",# replace with your MySQL password
    database="heart_project"
)

cursor = db.cursor(dictionary=True)


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
app.secret_key = 'my123devsecret'

users={}

@app.route('/')
def home():
  return redirect(url_for('login_page'))

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            return "User already exists!"

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
        db.commit()
        return redirect(url_for('login_page'))
        #if username in users:
         #   return "User already exists!"
        #users[username] = password
        #return redirect(url_for('login_page'))
    return render_template('register.html')
        

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('predict'))
        else:
            return "Invalid credentials"
        #if username in users and users[username] == password:
         #   session['user'] = username
          #  return redirect(url_for('predict'))
        #else:
         #  return "Invalid credentials"
    return render_template('login.html')
        

@app.route('/predict', methods=['GET', 'POST'])
def predict():
      if 'user' not in session:
          return redirect(url_for('login_page'))

      if request.method == 'POST':
          print(request.form)

          age = float(request.form['age'])
          gender = int(request.form['gender'])
          cp = int(request.form['cp'])
          rbp = float(request.form['Rbp'])
          chol = float(request.form['Chol'])
          fbs = int(request.form['fbs'])
          ecg = int(request.form['ecg'])
          mhr = float(request.form['mhr'])
          ex = int(request.form['ex'])
          op = float(request.form['op'])
          slp = int(request.form['slp'])

          features = [age, gender, cp, rbp, chol, fbs, ecg, mhr, ex, op, slp]
          output = model.predict([features])[0]
          print("Prediction output:", output)

          if output == 0:
               res_val = "The Patient Has Heart Disease. Please consult a Doctor."
          else:
               res_val = "The Patient is Normal."

          return render_template('index1.html', prediction_text=f"Result - {res_val}")

      return render_template('index1.html', prediction_text='')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login_page'))

if __name__ == "__main__":
  app.run()
##host='0.0.0.0',debug=False, port = 4566
