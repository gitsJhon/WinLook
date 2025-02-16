import flet as ft
import os
import zipfile

# Lista de cursores y sus nombres normalizados
CURSORS = {
    "arrow.cur": "Cursor normal",
    "help.cur": "Cursor de ayuda (signo de interrogación)",
    "appstarting.cur": "Cargando (flecha + círculo)",
    "wait.cur": "Espera (reloj de arena/círculo giratorio)",
    "cross.cur": "Cruz de precisión",
    "ibeam.cur": "Cursor de texto",
    "no.cur": "Prohibido (círculo con barra)",
    "size_nwse.cur": "Redimensionar diagonal ↖↘",
    "size_nesw.cur": "Redimensionar diagonal ↗↙",
    "size_we.cur": "Redimensionar horizontal ↔",
    "size_ns.cur": "Redimensionar vertical ↕",
    "size_all.cur": "Mover (flechas en todas direcciones)",
    "up.cur": "Flecha hacia arriba",
    "hand.cur": "Cursor de enlace (mano señalando)"
}

def main(page: ft.Page):
    page.title = "Normalizador de Cursores"
    page.vertical_alignment = "start"  # Alinear contenido al inicio
    page.horizontal_alignment = "center"
    page.window_width = 400  # Ancho de la ventana más angosto
    page.window_height = 600  # Alto de la ventana
    page.window_resizable = False  # Evitar que el usuario redimensione la ventana
    page.scroll = "adaptive"  # Habilitar scroll
    page.window_resizable = False  # Evitar que el usuario redimensione la ventana

    # Diccionario para almacenar los archivos subidos y su nombre normalizado
    uploaded_files = {}

    # Función para manejar la subida de archivos
    def on_file_upload(e: ft.FilePickerResultEvent, cursor_name):
        if not e.files:
            return

        # Guardar el archivo subido en el diccionario con su nombre normalizado
        file = e.files[0]
        uploaded_files[cursor_name] = file.path
        update_file_list()

    # Función para actualizar la lista de archivos subidos
    def update_file_list():
        file_list.controls.clear()
        for cursor_name, file_path in uploaded_files.items():
            file_list.controls.append(ft.Text(f"{cursor_name}: {os.path.basename(file_path)}"))
        page.update()

    # Función para comprimir los archivos en un .zip
    def create_zip(e):
        if not uploaded_files:
            lbl_result.value = "No se han subido archivos."
            page.update()
            return

        # Obtener el nombre del archivo .zip
        zip_name = zip_name_input.value.strip()
        if not zip_name:
            lbl_result.value = "Por favor, ingresa un nombre para el archivo .zip."
            page.update()
            return

        # Asegurarse de que el nombre del archivo termine en .zip
        if not zip_name.endswith(".zip"):
            zip_name += ".zip"

        # Crear una carpeta temporal para guardar los archivos renombrados
        temp_dir = "temp_cursors"
        os.makedirs(temp_dir, exist_ok=True)

        # Mover y renombrar los archivos
        for cursor_name, file_path in uploaded_files.items():
            new_path = os.path.join(temp_dir, cursor_name)
            os.rename(file_path, new_path)

        # Crear un archivo .zip con los archivos renombrados
        zip_path = zip_name
        with zipfile.ZipFile(zip_path, "w") as zipf:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    zipf.write(os.path.join(root, file), file)

        # Limpiar la carpeta temporal
        for file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, file))
        os.rmdir(temp_dir)

        lbl_result.value = f"Archivos comprimidos en '{zip_path}'."
        page.update()

    # Controles de la interfaz
    file_pickers = {}  # Almacenar los FilePicker para cada cursor

    # Crear un FilePicker para cada cursor
    for cursor_name, description in CURSORS.items():
        file_picker = ft.FilePicker(on_result=lambda e, c=cursor_name: on_file_upload(e, c))
        file_pickers[cursor_name] = file_picker
        page.overlay.append(file_picker)

    # Crear un campo de entrada para el nombre del .zip
    zip_name_input = ft.TextField(
        label="Nombre del archivo .zip",
        width=350,
        value="cursors.zip"  # Valor por defecto
    )

    # Crear una lista de controles para los botones de subida
    upload_controls = []
    for cursor_name, description in CURSORS.items():
        upload_controls.append(
            ft.Row(
                controls=[
                    ft.Text(description, width=200),  # Descripción del cursor
                    ft.ElevatedButton(
                        "Subir archivo",
                        on_click=lambda e, c=cursor_name: file_pickers[c].pick_files(allow_multiple=False)
                    )
                ]
            )
        )

    file_list = ft.Column()

    btn_create_zip = ft.ElevatedButton(
        "Crear .zip",
        on_click=create_zip
    )

    lbl_result = ft.Text()

    # Añadir controles a la página
    page.add(
        ft.Text("Nombre del archivo .zip:"),
        zip_name_input,
        ft.Divider(),  # Línea divisoria
        ft.Text("Sube los archivos de cursores:"),
        *upload_controls,
        ft.Divider(),  # Línea divisoria
        ft.Text("Archivos subidos:"),
        file_list,
        btn_create_zip,
        lbl_result
    )

# Ejecutar la aplicación
ft.app(target=main)