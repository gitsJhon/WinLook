import subprocess
import time

# 1. Iniciar el backend Flask
flask_process = subprocess.Popen(["python", "backend/app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 2. Esperar unos segundos para que Flask arranque
time.sleep(3)

# 3. Iniciar la aplicación de Electron
subprocess.Popen("npm start", shell=True)
