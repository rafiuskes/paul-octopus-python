import importlib

from flask import Flask, send_from_directory

from predictor.AbstractPredictor import AbstractPredictor
from utils.csv import *
from utils.gcs import download_blob

app = Flask(__name__)


@app.route("/")
def index():
    return "Paul the Octopus is alive!!!"


@app.route("/predict/<predictor_name>")
def predict(predictor_name):

    # Download all the files that you need for your predictors
    download_blob(blob_name='sample_predictions_submission.csv')
    download_blob(blob_name='historical_win-loose-draw_ratios.csv')

    # Use a sample file to load all matches
    matches = read_csv('sample_predictions_submission.csv')

    # Instantiate the Predictor class based on the predictor_name
    PredictorClass = getattr(importlib.import_module(f'predictor.{predictor_name}'), predictor_name)
    predictor: AbstractPredictor = PredictorClass()

    # Make predictions and write them into the predictions.csv file
    predictions = predictor.predict(matches)
    write_csv(predictions, ['home', 'home_score', 'away_score', 'away'], 'predictions.csv')

    # Return the predictions.csv file for downloading
    return send_from_directory('.', 'predictions.csv')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)


