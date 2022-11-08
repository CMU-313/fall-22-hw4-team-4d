from http.client import HTTPException
import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        health = request.args.get('health')
        absences = request.args.get('absences')
        Medu = request.args.get('Medu')
        Fedu = request.args.get('Fedu')
        Dalc = request.args.get('Dalc')

        try:
            intHealth = int(health)
            if intHealth <=0 or intHealth > 5:
                raise HTTPException(
                    status_code=500
                )
            intAbsences = int(absences)
            if intAbsences < 0 or intAbsences > 93:
                raise HTTPException(
                    status_code=500
                )
            intMedu = int(Medu)
            if intMedu < 0 or intMedu > 4:
                raise HTTPException(
                    status_code=500
                )
            intFedu = int(Fedu)
            if intFedu < 0 or intFedu > 4:
                raise HTTPException(
                    status_code=500
                )
            intDalc = int(Dalc)
            if intDalc <= 0 or intDalc > 5:
                raise HTTPException(
                    status_code=500
                )
        except Exception:
                raise HTTPException(
                    status_code=500
                )

        data = [[health], [absences], [Medu], [Fedu], [Dalc]]
        query_df = pd.DataFrame({
            'Dalc':pd.Series(int(Dalc)),
            'Fedu':pd.Series(int(Fedu)),
            'Medu':pd.Series(int(Medu)),
            'absences': pd.Series(int(absences)),
            'health': pd.Series(int(health))
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction))
