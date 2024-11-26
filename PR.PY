from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://crisesv18:Tanke1804.@aztech.ww3ye9j.mongodb.net/?retryWrites=true&w=majority&appName=aztech"
client = MongoClient(uri, server_api=ServerApi('1'))

correo = "cpma.cristopher.sanchez@gmail.com"
db=client['root']
col=db['users']
tema=col.find_one({"email":correo},{"teamnumber":1, "_id":0})
print(tema.get("teamnumber"))    