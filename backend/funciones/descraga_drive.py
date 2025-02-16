import gdown
import os

def descargar_drive(url, nombre_archivo):
    try:
        # Extraer ID del enlace de Google Drive
        file_id = url.split("/d/")[1].split("/")[0]
        direct_url = f"https://drive.google.com/uc?export=download&id={file_id}"
        
        # Definir la ruta de descarga (relativa al script)
        carpeta_destino = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../cursors_zip"))
        
        # Asegurar que la carpeta de destino existe
        os.makedirs(carpeta_destino, exist_ok=True)
        
        # Ruta completa del archivo de salida
        output_path = os.path.join(carpeta_destino, nombre_archivo if nombre_archivo.endswith(".zip") else f"{nombre_archivo}.zip")

        # Descargar el archivo
        gdown.download(direct_url, output_path, quiet=False)

        print(f"Archivo descargado en: {output_path}")
        return output_path

    except Exception as e:
        print(f"Error al descargar el archivo: {e}")
        return None

# Ejemplo de uso
descargar_drive("https://drive.google.com/file/d/1FXxcTxHRvxVW9nBYBHVyGdUfMj5JvkHi/view?usp=drive_link", "overwatch.zip")
