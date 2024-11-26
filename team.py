import flet as ft
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
import math
uri = "mongodb+srv://crisesv18:Tanke1804.@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))

def tm(page: ft.Page, correo):
    global hrsusadastotales
    global CO2Total
    CO2Total=0
    hrsusadastotales = 0
    page.padding = ft.Margin(10, 10, 10, 10)
    team=ft.TextField(label="Ingresa el nombre del equipo")
    pasw=ft.TextField(label="Ingrese la contraseña")
    def agregar(e):
        team=e.control.data
        grid_view.controls.clear()
        page.update()
        cor=correo
        db = client['BlueApp']
        collection = db['Devices']
        dispositivos = collection.find({"Team":str(team)})
        for dispositivo in dispositivos:
            content = ft.Card(
                content=ft.Column([
                    ft.Text(f"Nombre: {dispositivo.get('Device', 'N/A')}"),
                    ft.Text(f"Categoria: {dispositivo.get('Category', 'N/A')}"),
                    ft.Text(f"Watts: {dispositivo.get('Watss', 'N/A')}"),
                    ft.Text(f"Equipo: {dispositivo.get('Team', 'N/A')}"),
                ])
            )
            grid_view.controls.append(content)
        page.update()
    def inicio(e):
        team="Sin Equipo"
        grid_view.controls.clear()
        page.update()
        cor=correo
        db = client['BlueApp']
        collection = db['Devices']
        dispositivos = collection.find({"Email":correo,"Team":str(team)})
        for dispositivo in dispositivos:
            content = ft.Card(
                content=ft.Column([
                    ft.Text(f"Nombre: {dispositivo.get('Device', 'N/A')}"),
                    ft.Text(f"Usuario: {dispositivo.get('Name', 'N/A')}"),
                    ft.Text(f"Categoria: {dispositivo.get('Category', 'N/A')}"),
                    ft.Text(f"Watts: {dispositivo.get('Watss', 'N/A')}"),
                    ft.Text(f"Equipo: {dispositivo.get('Team', 'N/A')}"),
                ])
            )
            grid_view.controls.append(content)
        page.update()
    def crear(e):
        equipo=team.value
        contraseña=pasw.value
        db=client['BlueApp']
        collection=db['Teams']
        collection.insert_one({
            "Teams":equipo,
            "Password":contraseña,
            "EmailAdmin": correo,
            "Members":[]
        })
        inicio(None)
    
    def unirse(e):
        db=client['BlueApp']
        collection=db['Teams']
        equipo=team.value
        teams=collection.find_one({"Teams":equipo})
        if team:
            contr=collection.find_one({"Teams":equipo},{"Password":1,"_id":0})
            if contr.get("Password")==pasw.value:
                collection.update_one({"Teams":equipo},{"$push":{"Members":correo}})    
                db=client["root"]
                collection=db["users"]
                collection.update_one({"email":correo},{"$push":{"teamnumber":equipo}})
                inicio(None)

    def abrir(e):
        tipo=e.control.data
        grid_view.controls.clear()
        page.update()
        if tipo=="Create":
            btn=ft.ElevatedButton("Crear", on_click=crear)
        elif tipo=="Join":
            btn=ft.ElevatedButton("Unirse", on_click=unirse)
        preguntas=ft.Container(
            ft.Column([
                ft.Row([
                    team
                ]),
                ft.Row([
                    pasw
                ]),
                ft.Row([
                    btn
                ])
            ])
        )
        grid_view.controls.append(preguntas)
        page.update()
    def Co2(e):
        global hrsusadastotales
        global CO2Total        
        equipo=e.control.data
        db=client['BlueApp']
        collection=db['Devices']
        if equipo== "Sin Equipo":
            busqueda=collection.find({'Email':correo,'Team':equipo})
        else:
            busqueda=collection.find({'Team':equipo})
        for i in list(busqueda):
            Wa=float(i.get('Watss'))
            date=i.get('StartDate')
            if isinstance(date,datetime.datetime):
                dif=datetime.datetime.now()-date
                hrs=dif.total_seconds()/3600
                ec=Wa*hrs
                Co2=ec*.475
                CO2Total+=Co2
                hrsusadastotales+=hrs
        content = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text(f"Horas totales usadas: {hrsusadastotales:.2f}"),
            ]),
            ft.Row([
                ft.Text(f"CO2 Generado: {CO2Total:.2f}")
            ]),
            ft.Row([
                ft.Text(f"Los arboles a plantar son {math.ceil((CO2Total)/22)}")
            ])
        ])
    )
        grid_view.controls.clear()
        grid_view.controls.append(content)
        page.update()
    


        
    

    page.horizontal_alignment = ft.MainAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    is_mobile = page.width < 600
    page.window.maximized = not is_mobile
    
    grid_view = ft.GridView(
        expand=False,
        max_extent=300 if not is_mobile else 150,
        spacing=10,
        run_spacing=10,
        height=800 if not is_mobile else 400,
    )
    
    add = [
        ft.SubmenuButton(
            content=ft.Text("Sin Equipo"),
            controls=[
                ft.MenuItemButton(content=ft.Text("Dashboard"), on_click=inicio, data="Sin Equipo"),
                ft.MenuItemButton(content=ft.Text("Co2"),data="Sin Equipo",on_click=Co2),
            ]
        )
    ]
    
    def addteams():
        db = client['root']
        collection = db['users']
        teams = collection.find_one({"email": correo}, {"teamnumber": 1, "_id": 0})
        
        if teams and teams.get("teamnumber"):
            for team_number in teams.get("teamnumber"):
                co = ft.SubmenuButton(
                    content=ft.Text(team_number),
                    controls=[
                        ft.MenuItemButton(content=ft.Text("Dashboard"), on_click=agregar, data=team_number,),
                        ft.MenuItemButton(content=ft.Text("Co2"),data=team_number, on_click=Co2),
                    ]
                )
                add.append(co)

    addteams()
    
    contenido = ft.Row([
        ft.Column([
            ft.FilledButton(icon=ft.icons.CREATE, text="Crear",data="Create",on_click=abrir),
            ft.FilledButton(icon=ft.icons.ADD_LINK, text="Unirse",data="Join",on_click=abrir),
            *add
        ], width=150),
        ft.Container(
            content=grid_view,
            width=500 if is_mobile else 1000,
            bgcolor="green200"
        )
    ])
    inicio(None)
    return contenido
