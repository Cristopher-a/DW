import flet as ft
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://crisesv18:Tanke1804.@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))

def dsh(page):
    is_mobile = page.width < 600  
    page.window.maximized = not is_mobile  

    grid_view = ft.GridView(
        expand=False,
        max_extent=300 if not is_mobile else 150,
        spacing=10,
        run_spacing=10,
        height=800 if not is_mobile else 400,
    )

    def cargar_dispositivos():
        db = client['BlueApp']
        collection = db['Devices']
        dispositivos = collection.find()
        for dispositivo in dispositivos:
            content = ft.Card(
                content=ft.Column([
                    ft.Text(f"Nombre: {dispositivo.get('Dispositivo', 'N/A')}"),
                    ft.Text(f"Categoria: {dispositivo.get('Categoria', 'N/A')}"),
                    ft.Text(f"Watts: {dispositivo.get('Watss', 'N/A')}"),
                ])
            )
            grid_view.controls.append(content)
        page.update()

    type_dropdown = ft.Dropdown(
        hint_text="Categoria",
        options=[
            ft.dropdown.Option(text="Computadoras"),
            ft.dropdown.Option(text="Herramientas"),
            ft.dropdown.Option(text="Robot"),
        ]
    )
    name = ft.TextField(label="Nombre del dispositivo")
    watts = ft.TextField(label="Watts", suffix_text="W", keyboard_type=ft.KeyboardType.NUMBER)
    
    selected_images = []  # Lista para almacenar las rutas de las imágenes seleccionadas

    # Lógica de selección de archivos
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_images.clear()  # Limpiar imágenes previas
            for file in e.files:
                selected_images.append(file.path)  # Guardar ruta de cada archivo seleccionado

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    files = ft.ElevatedButton(
        "Seleccionar archivos",
        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True)
    )

    def agregar(e):
        nombre = name.value
        wts = watts.value
        categoria = type_dropdown.value
        
        # Crear lista de componentes de imagen para el contenido de la tarjeta
        image_components = [
            ft.Image(src=image_path, width=100, height=100, fit=ft.ImageFit.CONTAIN)
            for image_path in selected_images
        ]
        
        # Agregar dispositivo con las imágenes al grid
        content = ft.Card(
            content=ft.Column([
                ft.Text(f"Nombre: {nombre}"),
                ft.Text(f"Categoria: {categoria}"),
                ft.Text(f"Watts: {wts}"),
                *image_components  # Agregar imágenes dentro de la tarjeta del dispositivo
            ])
        )
        grid_view.controls.append(content) 
        page.update()

        # Guardar dispositivo en MongoDB
        db = client['BlueApp']
        collection = db['Devices']
        dispositivo = {
            "Dispositivo": nombre,
            "Watss": wts,
            "Categoria": categoria,
            "Imagenes": selected_images  # Guardar rutas de imágenes en la base de datos
        }
        collection.insert_one(dispositivo)

    controller = ft.Row([
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([name]),
                    ft.Row([watts]),
                    ft.Row([type_dropdown]),
                    ft.Row([files]),  # Botón para seleccionar archivos
                    ft.Row([ft.ElevatedButton("Guardar", icon=ft.icons.CHECK, on_click=agregar)]),
                ]),
                padding=25,
                width=300 if is_mobile else 400
            )
        ),
        ft.Container(
            content=grid_view,
            width=500 if is_mobile else 1000,
            bgcolor="green200"
        )
    ])

    cargar_dispositivos()
    return controller
