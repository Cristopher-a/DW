import flet as ft
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

uri = "mongodb+srv://crisesv18:Tanke1804.@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))

def dsh(page, correo):
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
        cor=correo
        db = client['BlueApp']
        collection = db['Devices']
        dispositivos = collection.find({"Correo":cor})
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
   
    def agregar(e):
        cor=correo
        nombre = name.value
        wts = watts.value
        categoria = type_dropdown.value
        db = client['root']
        collection = db['users']
        resultado=collection.find_one({"email":cor},{"name":1,"_id":0})
        content = ft.Card(
            content=ft.Column([
                ft.Text(f"Nombre: {nombre}"),
                ft.Text(f"Categoria: {categoria}"),
                ft.Text(f"Watts: {wts}"),
                ft.Text(f"Usuario: {resultado.get("name")}")
            ])
        )
        grid_view.controls.append(content) 
        page.update()

        db = client['BlueApp']
        collection = db['Devices']
        dispositivo = {
            "Dispositivo": nombre,
            "Watss": wts,
            "Categoria": categoria,
            "Correo":correo,
            "Nombre":resultado.get("name"),
            "FechaInic": datetime.now(),
            "FechaFin": None

        }
        collection.insert_one(dispositivo)

    controller = ft.Row([
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([name]),
                    ft.Row([watts]),
                    ft.Row([type_dropdown]),
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
