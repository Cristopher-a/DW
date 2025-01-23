from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import math

uri = "mongodb+srv://crisesv18:Tanke1804.@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['BlueApp']
collection = db['Devices']
w=.0675
r=(datetime.now())-(resultado.get("FechaInic"))
print(r.total_seconds()/3600)
energia_consumida = w * r.total_seconds()/3600
print(energia_consumida)
CO2 = energia_consumida * .475

print(f"El co2 consumido es {CO2}")
arboles= CO2/22

print(f"Los arboles a plantar son {math.ceil(arboles)}")
