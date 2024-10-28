import flet as ft
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from threading import Timer
import bcrypt

uri = "mongodb+srv://crisesv18:LoKY1804@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))


def creative(page:ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Crear Cuenta"
    page.padding = ft.Margin(20, 20, 20, 20)

    def close_banner(page, banner):
      page.close(banner)

    def crear(e):
        db = client['root']
        collection = db['users']
        correo=correo_field.value
        passw=password_field.value
        name=name_field.value
        password= bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user=collection.find_one({"email":correo})
        if user:
            page.open(error)
            Timer(3, close_banner, args=(page, error)).start()
        else:
            reg={
             "email": correo,
             "password": password,
             "name": name
            }
            collection.insert_one(reg)
            page.open(creado)
            Timer(3, close_banner, args=(page, creado)).start()
    def habil(e):
        if all([correo_field.value, password_field.value, name_field.value]):
            btn.disabled = False
            page.update()
        else:
            btn.disabled = True
            page.update()

    creado = ft.Banner(
        bgcolor=ft.colors.RED_600,
        leading=ft.Icon(ft.icons.CREATE_NEW_FOLDER_OUTLINED, color=ft.colors.RED_800, size=40),
        content=ft.Text("Nueva cuenta creada"),
        actions=[
            ft.TextButton(text="Cerrar", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(creado)),
        ]
    )
    error = ft.Banner(
        bgcolor=ft.colors.RED_600,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.RED_800, size=40),
        content=ft.Text("El correo ya existe"),

        actions=[
            ft.TextButton(text="Cerrar", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(error)),
        ]
    )
    
    correo_field = ft.TextField( width=300, label="Email", on_change=habil)
    password_field = ft.TextField( width=300, label="Contraseña",can_reveal_password=True,password=True,on_change=habil)
    name_field=ft.TextField(label="Ingresa tu nombre",on_change=habil)
    number_field= ft.TextField(label="Numero",on_change=habil,keyboard_type=ft.KeyboardType.NUMBER)
    country_dropdown= ft.Dropdown(
        options=[
            ft.dropdown.Option("Mexico"),
            ft.dropdown.Option("Estados Unidos"),
            ft.dropdown.Option("Canada"),
            ft.dropdown.Option("Chile"),
            ft.dropdown.Option("Brasil"),
            ft.dropdown.Option("Colombia"),
            ft.dropdown.Option("España"),
        ]
        ,
    )
    btn= ft.ElevatedButton("Crear cuenta",on_click=crear,disabled=True)
    corr = ft.Container(
        ft.Column([
            ft.Row([ft.Text("Crear Cuenta")]),
            ft.Row([correo_field]),
            ft.Row([password_field]),
            ft.Row([name_field]),
            ft.Row([btn]),
            ft.Row([country_dropdown]),
        ])
    )
    page.add(corr)

if  __name__ == "__main__":
    ft.app(target=creative)