import time
import threading
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSs2orykjN4Oe-AwBZFnKDSwAmlfQZsbChpGvaa0371f9Ov2kYY8Sujfb5i-LvuqRtI77lOENEpTDys/pub?gid=0&single=true&output=csv"

def cursor_datos():
    df = pd.read_csv(URL_CSV)
    return df.to_dict(orient="records")

@app.route("/cursores", methods=["GET"])
def obtener_cursores():
    return jsonify(cursor_datos())

def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    
    while True:  # Evita que el script termine
        time.sleep(1)
