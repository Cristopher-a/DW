from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import flet as ft
import bcrypt
from navigation import nav
from recoverp import recov
from create import creative


uri = "mongodb+srv://crisesv18:LoKY1804@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))


def inic(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Blue Switch"
    
    user_field = ft.TextField(label="Usuario", width=300)
    password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    banner = ft.Banner( 
        bgcolor=ft.colors.RED_600,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.RED_800, size=40),
        content=ft.Text("Error de inicio de sesión"),
        actions=[ft.TextButton(text="Cerrar", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(banner))]
    )

    def recover(e):
        page.controls.clear()
        page.controls.append(recov(page))
    def create(e):
        page.controls.clear()
        page.controls.append(creative(page))
        




    def iniciar_sesion(e):
        user = user_field.value
        password = password_field.value
        
        db = client['root']
        collection = db['users']
        user_data = collection.find_one({"email": user})
        
        if user_data:
            contraseña_encriptada = user_data.get("password")
            if bcrypt.checkpw(password.encode('utf-8'), contraseña_encriptada.encode('utf-8')):
                cargar_dashboard(page) 
            else:
                page.open(banner)
        else:
            page.open(banner)
        
        page.update()
    con = ft.Container(
        ft.Column([
            ft.Row([ft.Text("Blue Switch", text_align="center")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([user_field], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([password_field], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.TextButton(text="Recuperar contraseña", on_click=recover), 
                    ft.TextButton(text="Crear Cuenta",on_click=create)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton(text="Iniciar Sesión", on_click=iniciar_sesion)], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    page.add(con)

def cargar_dashboard(page):
    page.controls.clear()
    page.controls.append(nav(page))
    page.update()

if __name__ == "__main__":
    ft.app(target=inic)
