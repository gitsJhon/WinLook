import time
import threading
from flask import Flask, jsonify, request
from cursors_datos import cursor_datos
import webbrowser
app = Flask(__name__)

@app.route("/cursores", methods=["GET"])
def obtener_cursores():
    return jsonify(cursor_datos())

@app.route("/abrir-url", methods=["POST"])
def abrir_url():
    data = request.json
    url = data.get("url")
    
    if url:
        webbrowser.open(url)  # Abre la URL en el navegador predeterminado
        return jsonify({"status": "success", "message": f"Abriendo {url}"}), 200
    else:
        return jsonify({"status": "error", "message": "No se proporcionó una URL"}), 400

def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    
    while True:  # Evita que el script termine
        time.sleep(1)
