"""Codigo que permite la creacion de una API RESTful con FastAPI para la 
   gestion de inventarios de ABC Motor
"""

# Declaracion de librerias
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Creacion de la aplicacion FastAPI
app = FastAPI()

# Clase que define la estructura de un inventario


class Inventario(BaseModel):
    id: int
    codigo: str
    descripcion: str
    familia: str
    clase: str
    cantidad: float
    precio: float
    total: float


# Lista vacía para almacenar los artículos creados.
inventarios = []

# Ruta para la página de inicio que devuelve un mensaje de bienvenida.


@app.get('/')
def bienvenida():
    return {'mensaje': 'Bienvenidos a mi API FastAPI Interoperabilidad Empresarial Diciembre 2024'}


# Ruta para obtener todos los artículos almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Inventario".
@app.get("/inventarios", response_model=List[Inventario])
async def leer_inventario():
    return inventarios

# Ruta para crear un nuevo artículo.
# El parámetro "response_model" especifica que la respuesta será un objeto "Inventario".


@app.post("/inventarios", response_model=Inventario)
async def crear_inventario(inventario: Inventario):
    inventarios.append(inventario)  # Agrega el artículo a la lista.

    return inventario

# Ruta para actualizar una orden existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Inventario".


@app.put("/inventarios/{inventario_id}", response_model=Inventario)
async def actualizar_inventario(inventario_id: int, inventario: Inventario):
    # Actualiza el inventario en la lista.
    inventarios[inventario_id] = inventario
    return inventario

# Ruta para eliminar una orden por su ID.
# No se especifica "response_model" ya que no se devuelve ningún objeto en la respuesta.
# Este metodo elimina una orden por su ID.


@app.delete("/inventarios/{inventario_id}")
async def eliminar_inventario(inventario_id: int):
    del inventarios[inventario_id]
    """Elimina el item de la lista no es el id de la clase
    sino la posicion en la lista empieza desde 0"""
    # Devuelve un mensaje informativo.
    return {"mensaje": "Inventario eliminado"}
