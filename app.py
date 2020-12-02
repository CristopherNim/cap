import numpy as np
from flask import Flask, request, jsonify, render_template, session, flash, redirect, url_for, g
import os
import pickle

app = Flask(__name__)
model = pickle.load(open('mush.pkl', 'rb'))


@app.route('/', methods=['POST', 'get'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['get', 'post'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction

    return render_template('index.html', prediction_text='mushroom is {} (1= edible and 0 = poisonous)'.format(output))


@app.route('/results', methods=['Post', 'get'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
