import os
import ctypes
import zipfile

def reemplazar_cursores_desde_zip(base_path, zip_filename):
    """Busca y reemplaza los cursores del sistema con los encontrados en el archivo ZIP."""
    
    zip_path = os.path.join(base_path, zip_filename)
    if not os.path.exists(zip_path):
        print(f"❌ Archivo ZIP no encontrado: {zip_path}")
        return

    # Carpeta temporal para extraer los cursores
    temp_folder = os.path.join(os.path.dirname(zip_path), "temp_cursors")
    os.makedirs(temp_folder, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extraer todo el contenido del ZIP directamente en la carpeta temporal
        zip_ref.extractall(temp_folder)

    # Mapeo de nombres de archivos a identificadores de cursor en Windows
    CURSOR_MAP = {
        "arrow.cur": 32512,         # Cursor normal
        "help.cur": 32651,          # Ayuda (?)
        "appstarting.cur": 32650,   # Cargando (flecha + círculo)
        "wait.cur": 32514,          # Espera (reloj de arena)
        "cross.cur": 32515,         # Cruz de precisión
        "ibeam.cur": 32513,         # Cursor de texto
        "no.cur": 32648,            # Prohibido (círculo con barra)
        "size_nwse.cur": 32642,     # Redimensionar diagonal ↖↘
        "size_nesw.cur": 32643,     # Redimensionar diagonal ↗↙
        "size_we.cur": 32644,       # Redimensionar horizontal ↔
        "size_ns.cur": 32645,       # Redimensionar vertical ↕
        "size_all.cur": 32646,      # Mover (todas direcciones)
        "up.cur": 32516,            # Flecha hacia arriba
        "hand.cur": 32649           # Cursor de enlace (mano)
    }

    # Buscar archivos CUR y reemplazar cursores
    for file_name, cursor_id in CURSOR_MAP.items():
        cursor_path = os.path.join(temp_folder, file_name)
        if os.path.exists(cursor_path):
            print(f"✅ Reemplazando {file_name}...")
            ctypes.windll.user32.SetSystemCursor(ctypes.windll.user32.LoadCursorFromFileW(cursor_path), cursor_id)
        else:
            print(f"⚠️ {file_name} no encontrado en el ZIP, se omite.")

    # Eliminar la carpeta temporal
    for root, dirs, files in os.walk(temp_folder, topdown=False):
        for file_name in files:
            os.remove(os.path.join(root, file_name))
        for dir_name in dirs:
            os.rmdir(os.path.join(root, dir_name))
    os.rmdir(temp_folder)

    print("🎯 Todos los cursores disponibles han sido aplicados.")

# Ejemplo de uso
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, "../../../PCMASTER/cursors_zip"))
zip_filename = "overwatch.zip"  # Se pasará este nombre dinámicamente

reemplazar_cursores_desde_zip(project_dir, zip_filename)
