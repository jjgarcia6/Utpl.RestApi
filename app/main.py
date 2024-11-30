from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Orden(BaseModel):
    id: int
    producto: str
    cantidad: float
    tipo: str
    precio: float
    total: float


# Lista vacía para almacenar los artículos creados.
ordenes = []

# Ruta para la página de inicio que devuelve un mensaje de bienvenida.
@app.get('/')
def bienvenida():
    return {'mensaje': 'Welcome a mi aplicación FastAPI Utpl 2028'}

# Ruta para obtener todos los artículos almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Orden".
@app.get("/ordenes", response_model=List[Orden])
async def leer_ordenes():
    return ordenes

# Ruta para crear un nuevo artículo.
# El parámetro "response_model" especifica que la respuesta será un objeto "Orden".
# ES
@app.post("/ordenes", response_model=Orden)
async def crear_orden(orden: Orden):
    ordenes.append(orden)  # Agrega el artículo a la lista.
    return orden

# Ruta para actualizar una orden existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Orden".
@app.put("/ordenes/{orden_id}", response_model=Orden)
async def actualizar_orden(orden_id: int, orden: Orden):
    ordenes[orden_id] = orden  # Actualiza la orden en la lista.
    return orden

# Ruta para eliminar una orden por su ID.
# No se especifica "response_model" ya que no se devuelve ningún objeto en la respuesta.
# Este metodo elimina una orden por su ID.
@app.delete("/ordenes/{orden_id}")
async def eliminar_orden(orden_id: int):
    del ordenes[orden_id]  # Elimina el item de la lista.
    return {"mensaje": "Orden eliminada"}  # Devuelve un mensaje informativo.