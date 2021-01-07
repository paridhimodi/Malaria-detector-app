""" Created on sunday Jan 3 2021
@author - PARIDHI MODI
"""
from __future__ import division, print_function

import os

import numpy as np
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from flask_cors import cross_origin


app = Flask(__name__)


MODEL_PATH = 'malaria.h5'

model = load_model(MODEL_PATH)


def predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    preds = np.argmax(preds, axis=1)
    if preds == 0:
        preds = "The Person is Infected With Malaria"
    else:
        preds = "The Person is not Infected With Malaria"

    return preds


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def upload():
    if request.method == 'POST':
        fl = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        fl.save(file_path)

        # Make prediction
        preds = predict(file_path, model)
        result = preds
        return result
    return None


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
