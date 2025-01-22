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


# para trabajar con telegram

# para trabajar con telegram
# para trabajar con email
# from fastapi_versioning import VersionedFastAPI, version


from fastapi import FastAPI, Depends, HTTPException, Query, status
from pydantic import BaseModel
from typing import List, Annotated
from app.models import Inventario, InventarioUpdate, GetUser, PostUser, User
from sqlmodel import Session, select
from app.db import init_db, get_session
from app.security import verification
from app.utils.auth import decodeJWT, get_user, create_user, create_access_token, create_refresh_token, JWTBearer
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import date, datetime, timedelta, time
from app.utils.passwords import verify_pwd
from app.utils.telegram_service import send_message_telegram
from app.utils.email_service import send_email
from fastapi_versioning import VersionedFastAPI, version
tags_metadata = [
    {
        "name": "usuarios",
        "description": "Operaciones con usuarios. El **login** logica esta disponible aqui.",
    },
    {
        "name": "inventario",
        "description": "Administracion de inventario.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(title="FastAPI Utpl 2025",
              description="API para el Manejo de Inventario",
              version="1.0.0",
              contact={
                    "name": "Jimmy Garcia",
                    "url": "https://www.utpl.edu.ec/",
                    "email": "jjgarcia6@utpl.edu.ec"
              },
              openapi_tags=tags_metadata
              )


# app = FastAPI()

# Inicialización de la base de datos al iniciar la aplicación.


def get_user_by_id(user_id: int, db: Session) -> User:
    """
    Get a user by ID
    """
    return db.query(User).filter(User.id == user_id).first()
    # return db.exec(User).filter(User.id == user_id).first()


def get_current_user(token: str = Depends(JWTBearer()), session: Session = Depends(get_session)) -> User:
    """
    Get current user from JWT token
    """
    payload = decodeJWT(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token",
        )
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token",
        )
    # Assuming you have a function to get user by id from the database
    user = get_user_by_id(user_id, session)  # Implement this function
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


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
@app.get("/inventarios", response_model=List[Inventario], tags=["inventario"])
async def leer_inventario(session: Session = Depends(get_session), Verification=Depends(verification)):
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
@app.post("/inventarios", response_model=Inventario, tags=["inventario"])
async def crear_inventario(inventario: Inventario, session: Session = Depends(get_session), Verification=Depends(verification)):
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

        await send_message_telegram(f"Se ha creado un nuevo producto con el id: {inventario.id} y detalle: {inventario.detalle} de familia: {inventario.familia} con la cantidad: {inventario.cantidad} y precio: {inventario.precio}")
        send_email("Confirmación de Inventario", f"Se ha creado un nuevo producto con el id: {inventario.id} y detalle: {inventario.detalle} de familia: {inventario.familia} con la cantidad: {inventario.cantidad} y precio: {inventario.precio}", [
            "jjgarcia6@utpl.edu.ec"])
        return inventario
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail="Error al crear el inventario") from e

# Ruta para actualizar una orden existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Orden".


@app.put("/inventarios/{inventario_id}", response_model=Inventario, tags=["inventario"])
async def actualizar_inventario(inventario_id: int, inventario: InventarioUpdate, session: Session = Depends(get_session), Verification=Depends(verification)):
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


@app.delete("/inventarios/{inventario_id}", tags=["inventario"])
async def eliminar_inventario(inventario_id: int, session: Session = Depends(get_session), Verification=Depends(verification)):
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

# Register new user using email, username, password


@app.post("/register", response_model=GetUser, tags=["usuarios"])
def register_user(payload: PostUser, session: Session = Depends(get_session)):

    if not payload.email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please add Email",
        )
    user = get_user(session, payload.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User with email {payload.email} already exists",
        )
    user = create_user(session, payload)
    print(user)

    return user


@app.post("/login", tags=["usuarios"])
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    """
    Login user based on email and password
    """
    user = get_user(db, form_data.username)
    if not user or not verify_pwd(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    token = create_access_token(user.id, timedelta(minutes=30))
    refresh = create_refresh_token(user.id, timedelta(minutes=1008))

    return {'access_token': token, 'token_type': 'bearer', 'refresh_token': refresh, "user_id": user.id}


@app.get("/users/me", response_model=GetUser, tags=["usuarios"])
def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Get current user details
    """
    return current_user
