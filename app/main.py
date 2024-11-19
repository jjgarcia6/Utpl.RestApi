from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Definición de un modelo Pydantic llamado "Item" con tres campos: id, name y price.
class Articulo(BaseModel):
    id: int
    nombre: str
    precio: float

# Lista vacía para almacenar los artículos creados.s
articulos = []

# Ruta para la página de inicio que devuelve un mensaje de bienvenida.
@app.get('/')
def bienvenida():
    return {'mensaje': 'Bienvenido a mi aplicación FastAPI'}

# Ruta para obtener todos los artículos almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Articulo".
@app.get("/articulos", response_model=List[Articulo])
async def leer_articulos():
    return articulos

# Ruta para crear un nuevo artículo.
# El parámetro "response_model" especifica que la respuesta será un objeto "Articulo".
@app.post("/articulos", response_model=Articulo)
async def crear_articulo(articulo: Articulo):
    articulos.append(articulo)  # Agrega el artículo a la lista.
    return articulo

# Ruta para actualizar un artículo existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Articulo".
@app.put("/articulos/{articulo_id}", response_model=Articulo)
async def actualizar_articulo(articulo_id: int, articulo: Articulo):
    articulos[articulo_id] = articulo  # Actualiza el artículo en la lista.
    return articulo

# Ruta para eliminar un artículo por su ID.
# No se especifica "response_model" ya que no se devuelve ningún objeto en la respuesta.
@app.delete("/articulos/{articulo_id}")
async def eliminar_articulo(articulo_id: int):
    del articulos[articulo_id]  # Elimina el artículo de la lista.
    return {"mensaje": "Artículo eliminado"}  # Devuelve un mensaje informativo.