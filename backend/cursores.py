from flask import Flask, jsonify
import pandas as pd

URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSs2orykjN4Oe-AwBZFnKDSwAmlfQZsbChpGvaa0371f9Ov2kYY8Sujfb5i-LvuqRtI77lOENEpTDys/pub?gid=0&single=true&output=csv"
def cursor_datos():
    df = pd.read_csv(URL_CSV)
    return df.to_dict(orient="records")

datos = cursor_datos()
print(datos)