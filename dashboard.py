import flet as ft
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

uri = "mongodb+srv://crisesv18:Tanke1804.@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))

def dsh(page:ft.Page, correo):
    page.padding = ft.Margin(10, 10, 10, 10)
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
        dispositivos = collection.find({"Email": correo})
        for dispositivo in dispositivos:
            content = ft.Card(
                content=ft.Column([
                    ft.Text(f"Nombre: {dispositivo.get('Device', 'N/A')}"),
                    ft.Text(f"Categoria: {dispositivo.get('Category', 'N/A')}"),
                    ft.Text(f"Watts: {dispositivo.get('Watss', 'N/A')}"),
                    ft.Text(f"Usuario {dispositivo.get('Name', 'N/A')}"),
                    ft.Text(f"Equipo {dispositivo.get('Team','N/A')}")
                ])
            )
            grid_view.controls.append(content)
        page.update()

    op = [ft.dropdown.Option(text="Sin Equipo")]
    def teams():
        db = client['root']
        col = db['users']
        tema = col.find_one({"email": correo}, {"teamnumber": 1, "_id": 0})
        if tema and tema.get("teamnumber"):
            for team in tema["teamnumber"]:
                op.append(ft.dropdown.Option(text=team))  


    teams()

    type_dropdown = ft.Dropdown(
        hint_text="Categoria",
        options=[
            ft.dropdown.Option(text="Computadoras"),
            ft.dropdown.Option(text="Herramientas"),
            ft.dropdown.Option(text="Robot"),
        ]
    )
    Team_dropdown = ft.Dropdown(
        hint_text="Equipo",
        options=op 
    )

    name = ft.TextField(label="Nombre del dispositivo")
    watts = ft.TextField(label="Watts", suffix_text="W", keyboard_type=ft.KeyboardType.NUMBER)

    def agregar(e):
        nombre = name.value
        wts = watts.value
        categoria = type_dropdown.value
        team=Team_dropdown.value
        db = client['root']
        collection = db['users']
        resultado = collection.find_one({"email": correo}, {"name": 1, "_id": 0})

        content = ft.Card(
            content=ft.Column([
                ft.Text(f"Nombre: {nombre}"),
                ft.Text(f"Categoria: {categoria}"),
                ft.Text(f"Watts: {wts}"),
                ft.Text(f"Usuario: {resultado.get('name')}"),
                ft.Text(f"Equipo: {team}"),
            ])
        )
        grid_view.controls.append(content)
        page.update()

        db = client['BlueApp']
        collection = db['Devices']
        dispositivo = {
            "Device": nombre,
            "Watss": wts,
            "Category": categoria,
            "Email": correo,
            "Name": resultado.get("name"),
            "Team":team,
            "StartDate": datetime.now(),
            "EndDate": None

        }
        collection.insert_one(dispositivo)

    controller = ft.Row([
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([name]),
                    ft.Row([watts]),
                    ft.Row([type_dropdown]),
                    ft.Row([Team_dropdown]),
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
