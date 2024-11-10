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
    def ir(e):
        from index import inic
        page.controls.clear()
        page.controls.append(inic(page))

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
        if all([correo_field.value, password_field.value, name_field.value,number_field.value]) and  country_dropdown.value!=None:
            btn.disabled = False
            page.update()
        else:
            btn.disabled = True
            page.update()
    def lada(e):
        if country_dropdown.value=="México":
            number_field.prefix_text="+52"
            page.update()
        if country_dropdown.value=="Estados Unidos":
            number_field.prefix_text="+1"
            page.update()
        if country_dropdown.value=="Canadá":
            number_field.prefix_text="+1"
            page.update()
        if country_dropdown.value=="Brasil":
            number_field.prefix_text="+55"
            page.update()
        if country_dropdown.value=="Colombia":
            number_field.prefix_text="+57"
            page.update()
        if country_dropdown.value=="España":
            number_field.prefix_text="+34"
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
    number_field= ft.TextField(label="Numero",on_change=habil,input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9]*$", replacement_string=""),keyboard_type=ft.KeyboardType.NUMBER)
    country_dropdown= ft.Dropdown(
        options=[
            ft.dropdown.Option("México"),
            ft.dropdown.Option("Estados Unidos"),
            ft.dropdown.Option("Canadá"),
            ft.dropdown.Option("Chile"),
            ft.dropdown.Option("Brasil"),
            ft.dropdown.Option("Colombia"),
            ft.dropdown.Option("España"),
        ]
        ,
        label="Pais"
        ,
        hint_text="Ingresa tu pais"
        ,
        on_change=lada
    )
    btn= ft.ElevatedButton("Crear cuenta",on_click=crear,disabled=True)
    btnir= ft.ElevatedButton("Regresar",on_click=ir,disabled=True)
    corr = ft.Container(
        ft.Column([
            ft.Row([ft.Text("Crear Cuenta")]),
            ft.Row([correo_field]),
            ft.Row([password_field]),
            ft.Row([name_field]),
            ft.Row([country_dropdown]),
            ft.Row([number_field]),
            ft.Row([btn]),
            ft.Roe([btnir])
            
        ])
    )
    page.add(corr)

if  __name__ == "__main__":
    ft.app(target=creative)