import pymongo

# Conexión a MongoDB
mongo_host = "localhost"
mongo_puerto = "27017"
mongo_outtime = 1000
mongo_uri = f"mongodb://{mongo_host}:{mongo_puerto}/"

try:
    cliente = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=mongo_outtime)
    cliente.server_info()  # Verifica si la conexión es exitosa
    print("Conexión exitosa")
except pymongo.errors.ServerSelectionTimeoutError as e:
    print(f"Error de conexión: {e}")
except pymongo.errors.ConnectionFailure as i:
    print(f"Fallo en la conexión: {i}")

# Selecciona la base de datos y colección
db = cliente['nombre_de_tu_base_de_datos']  # Cambia este nombre
collection = db['users']  # Cambia este nombre

# Imprime todos los correos para verificar si el correo está correctamente guardado
print("Lista de correos en la base de datos:")
for user in collection.find({}, {"correo": 1, "_id": 0}):
    print(user)
