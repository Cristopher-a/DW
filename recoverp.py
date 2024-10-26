import flet as ft
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import ssl
import smtplib
from email.message import EmailMessage
import random
import bcrypt
import time
from threading import Timer

n = 0
c = ""
uri = "mongodb+srv://crisesv18:LoKY1804@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))

def recov(page: ft.Page):

    page.title = "Recovery Page"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def close_banner(page, banner):
      page.close(banner)
    def co(e):
        if all([txt1.value, txt2.value, txt3.value, txt4.value]):
            tn.disabled = False
        else:
            tn.disabled = True
        page.update()

    def r(e):
        global n
        t = txt1.value + txt2.value + txt3.value + txt4.value

        if n == int(t):
            page.controls.clear()
            page.controls.append(rec)
            page.update()
        else:
            page.open(error2)
            Timer(3, close_banner, args=(page, error2)).start()


    def cocon(e):
        if txtcont==None:
            btncon.disabled = True
        elif txtcont.value == txtconcont.value:
            btncon.disabled = False
        else:
            btncon.disabled = True
        page.update()
        
    def recover(e):
        global c
        c = correo_field.value
        db = client['root']
        collection = db['users']
        user_data = collection.find_one({"email": c})
        if user_data:
            number = random.randint(1000, 9999)
            global n
            n = number
            remitente = 'crisesv4@gmail.com'
            contrasena = 'dxfz ieip tibc vjti'
            asunto = 'Recuperar contraseña'
            em = EmailMessage()
            em['From'] = remitente
            em['To'] = c
            em['Subject'] = asunto
            em.set_content(str(number))
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(remitente, contrasena)
                smtp.sendmail(remitente, c, em.as_string())
            page.open(enviado)
            Timer(3, close_banner, args=(page, enviado)).start()
            page.controls.clear()
            page.controls.append(nd)
            page.update()
        else:
            page.open(error)
            Timer(3, close_banner, args=(page, error)).start()
    def cocont(e):
         from index import inic
         global c     
         db = client['root']
         collection = db['users']
         contraseña = txtcont.value
         cencrip = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') 
         filtro = {"email": c}
         act = {"$set": {"password": cencrip}}
         collection.update_one(filtro, act)
         page.open(cambiado)
         Timer(3, close_banner, args=(page, cambiado)).start()
         page.controls.clear()
         page.controls.append(inic(page))

    
    correo_field = ft.TextField(hint_text="Email", width=300, label="Email")
    txt1 = ft.TextField(max_length=1, counter_text=" ", text_size=40, width=50, on_change=co)
    txt2 = ft.TextField(max_length=1, counter_text=" ", text_size=40, width=50, on_change=co)
    txt3 = ft.TextField(max_length=1, counter_text=" ", text_size=40, width=50, on_change=co)
    txt4 = ft.TextField(max_length=1, counter_text=" ", text_size=40, width=50, on_change=co)
    
    tn = ft.ElevatedButton("Submit", on_click=r, disabled=True)
    txtcont = ft.TextField(label="Ingresa la nueva contraseña", password=True, can_reveal_password=True, on_change=cocon)
    txtconcont = ft.TextField(label="Confirma la nueva contraseña", password=True, can_reveal_password=True, on_change=cocon)
    btncon = ft.ElevatedButton("Submit", on_click=cocont, disabled=True)

    rec = ft.Container(
        ft.Column([
            ft.Row([ft.Text("Recovery Page")]),
            ft.Row([txtcont]),
            ft.Row([txtconcont]),
            ft.Row([btncon])
        ])
    )

    nd = ft.Container(
        ft.Column([
            ft.Row([ft.Text("Recovery Page")]),
            ft.Row([txt1, txt2, txt3, txt4]),
            ft.Row([tn])
        ])
    )
    
    error = ft.Banner(
        bgcolor=ft.colors.RED_600,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.RED_800, size=40),
        content=ft.Text("No existe correo"),
        actions=[
            ft.TextButton(text="Crear cuenta", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(error)),
            ft.TextButton(text="Cerrar", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(error)),
        ]
    )
    error2 = ft.Banner(
        bgcolor=ft.colors.RED_600,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.RED_800, size=40),
        content=ft.Text("No es el codigo correcto"),
        actions=[
            ft.TextButton(text="Cerrar", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(error2))
        ]
    )
    
    enviado = ft.Banner(
        bgcolor=ft.colors.GREEN_600,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.GREEN_800, size=40),
        content=ft.Text("Correo enviado"),
        actions=[ft.TextButton(text="Cerrar", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(enviado))]
    )
    cambiado = ft.Banner(
        bgcolor=ft.colors.GREEN_600,
        leading=ft.Icon(ft.icons.ERROR_OUTLINE, color=ft.colors.GREEN_800, size=40),
        content=ft.Text("Contraseña cambiada con exito"),
        actions=[ft.TextButton(text="Cerrar", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=lambda _: page.close(cambiado))]
    )
    
    corr = ft.Container(
        ft.Column([
            ft.Row([ft.Text("Ingresa tu correo")]),
            ft.Row([correo_field]),
            ft.Row([ft.ElevatedButton("Recuperar", on_click=recover)])
        ])
    )
    
    page.add(corr)

if __name__ == "__main__":
    ft.app(target=recov)
