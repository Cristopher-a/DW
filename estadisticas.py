import flet as ft
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
import math
uri = "mongodb+srv://crisesv18:Tanke1804.@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))

def stadistics(page: ft.Page,correo):
    global hrsusadastotales
    global CO2Total
    CO2Total=0
    hrsusadastotales = 0
    page.title = "Estadísticas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.Margin(10, 10, 10, 10)

    def contarhrs():
        global hrsusadastotales
        db = client['BlueApp']
        collection = db['Devices']
        dispositivos = collection.find({"Email": correo}, {"StartDate": 1, "_id": 0})

        for dispositivo in dispositivos:
            start_date = dispositivo.get("StartDate")
            if isinstance(start_date, datetime.datetime): 
                dif = datetime.datetime.now() - start_date
                horas = dif.total_seconds() / 3600
                hrsusadastotales += horas
            else:
                print(f"StartDate no es un objeto datetime: {start_date}")
    def contarCO2():
        global CO2Total
        db= client['BlueApp']
        collection = db['Devices']
        disp=collection.find({'Email':correo},{'Watss':1,'StartDate':1,'_id':0})
        for i in list(disp):
            watts=int(i.get('Watss'))
            date=i.get('StartDate')
            if isinstance(date,datetime.datetime):
                dif=datetime.datetime.now()- date
                horas = dif.total_seconds() / 3600
                ec=watts*horas
                CO2=ec*.475
                CO2Total+=CO2
    contarhrs()
    contarCO2()
    hrsacontainer = ft.Container(
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
    return hrsacontainer

