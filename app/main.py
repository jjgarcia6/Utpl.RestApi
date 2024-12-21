"""Codigo que permite la creacion de una API RESTful con FastAPI para la 
   gestion de inventarios de ABC Motor
"""

""" Pasos para ejecutar la aplicacion:
    1. Ejecute el siguiente comando en una terminal para inicar la aplicacion
       uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    2. Vaya a PORTS y cambie el puerto 8000 de privado a publico
    3. Forwarded Address le asignara una direccion de clic en Open in Browser
"""

# Declaracion de librerias

# Inicialización de la aplicación FastAPI
from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel
from typing import List
from app.models import Inventario, InventarioUpdate
from sqlmodel import Session, select
from app.db import init_db, get_session
app = FastAPI()

# Inicialización de la base de datos al iniciar la aplicación.


@app.on_event("startup")
def on_startup():
    init_db()


# Ruta para la página de inicio que devuelve un mensaje de bienvenida.
@app.get('/')
async def bienvenida() -> dict:
    """
    Ruta para la página de inicio que devuelve un mensaje de bienvenida.

    Returns:
        dict: Mensaje de bienvenida.
    """
    return {'mensaje': 'Bienvenidos a mi API Interoperabilidad Empresarial - ABC Motor'}


# Ruta para obtener todos los artículos almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Inventario".
@app.get("/inventarios", response_model=List[Inventario])
async def leer_inventario(session: Session = Depends(get_session)):
    """
    Ruta para obtener todos los artículos almacenados en la base de datos.

    Args:
        session (Session): Sesión de la base de datos proporcionada por la dependencia.

    Returns:
        List[Inventario]: Lista de objetos Inventario.
    """
    try:
        resultItems = session.exec(select(Inventario)).all()
        return resultItems
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Error al obtener los inventarios") from e


# Ruta para crear un nuevo artículo.
# El parámetro "response_model" especifica que la respuesta será un objeto "Inventario".
@app.post("/inventarios", response_model=Inventario)
async def crear_inventario(inventario: Inventario, session: Session = Depends(get_session)):
    """
    Ruta para crear un nuevo inventario.

    Args:
        inventario (Inventario): Objeto Inventario a crear.
        session (Session): Sesión de la base de datos proporcionada por la dependencia.

    Returns:
        Inventario: Objeto Inventario creado.
    """
    try:
        session.add(inventario)
        session.commit()
        session.refresh(inventario)
        return inventario
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail="Error al crear el inventario") from e

# Ruta para actualizar una orden existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Orden".


@app.put("/inventarios/{inventario_id}", response_model=Inventario)
async def actualizar_inventario(inventario_id: int, inventario: InventarioUpdate, session: Session = Depends(get_session)):
    """
    Ruta para actualizar un inventario existente por su ID.

    Args:
        inventario_id (int): ID del inventario a actualizar.
        inventario (InventarioUpdate): Objeto InventarioUpdate con los campos a actualizar.
        session (Session): Sesión de la base de datos proporcionada por la dependencia.

    Returns:
        Inventario: Objeto Inventario actualizado.
    """
    try:
        itemDB = session.get(Inventario, inventario_id)
        if itemDB is None:
            raise HTTPException(
                status_code=404, detail="Inventario no encontrado")

        update_data = inventario.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(itemDB, key, value)

        session.add(itemDB)
        session.commit()
        session.refresh(itemDB)
        return itemDB
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail="Error al actualizar el inventario") from e

# Ruta para eliminar una orden por su ID.
# No se especifica "response_model" ya que no se devuelve ningún objeto en la respuesta.
# Este metodo elimina una orden por su ID.


@app.delete("/inventarios/{inventario_id}")
async def eliminar_inventario(inventario_id: int, session: Session = Depends(get_session)):
    """
    Ruta para eliminar un inventario por su ID.

    Args:
        inventario_id (int): ID del inventario a eliminar.
        session (Session): Sesión de la base de datos proporcionada por la dependencia.

    Returns:
        dict: Mensaje de confirmación de eliminación.
    """
    try:
        itemDB = session.get(Inventario, inventario_id)
        if itemDB is None:
            raise HTTPException(
                status_code=404, detail="Inventario no encontrado")

        session.delete(itemDB)
        session.commit()
        return {"mensaje": "Inventario eliminado"}
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail="Error al eliminar el inventario") from e
