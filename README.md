# Utpl.RestApi
Proyecto para trabajar con Api en REST utilizando fastapi


## Descripción del Proyecto

**Este proyecto es una aplicación web construida utilizando FastAPI.** FastAPI es un framework de Python moderno, rápido y fácil de usar para crear APIs. Es ideal para construir aplicaciones web backend que necesitan ser eficientes y escalables.

## Requisitos

* **Python:** Asegúrate de tener Python 3.6 o superior instalado.
* **FastAPI:** Instala FastAPI usando pip:
  ```bash
  pip install fastapi uvicorn

## Documentación 
## API de Gestión de Inventarios
**Este proyecto es una API RESTful construida con FastAPI para la gestión de inventarios de ABCMotor**. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los inventarios.

## Descripción del Proyecto

**La API de Gestión de Inventarios está diseñada para facilitar la administración de inventarios de ABC Motor**. Utiliza FastAPI, un framework moderno y de alto rendimiento para construir APIs con Python.

## Endpoints

**Obtener todos los inventarios**
URL: /inventarios
Método: GET
Descripción: Devuelve una lista de todos los inventarios.


**Crear un nuevo inventario**
URL: /inventarios
Método: POST
Descripción: Crea un nuevo inventario.
Cuerpo de la solicitud:

Ejemplo: 
**JSON** 

```json
{
  "id": 1,
  "codigo": "ABC123",
  "descripcion": "Llanta 175/70R13",
  "familia": "Llantas",
  "clase": "Auto",
  "cantidad": 3,
  "precio": 50.0,
  "total": 150.0
}


**Actualizar un inventario**
URL: /inventarios/{inventario_id}
Método: PUT
Descripción: Actualiza un inventario existente por su ID.
Cuerpo de la solicitud:

Ejemplo:

{
  "id": 1,
  "codigo": "ABC123",
  "descripcion": "Llanta 175/70R13 Auto",
  "familia": "Llanta",
  "clase": "Auto",
  "cantidad": 3,
  "precio": 50.0,
  "total": 150.0
}

**Eliminar un inventario**
URL: /inventarios/{inventario_id}
Método: DELETE
Descripción: Elimina un inventario por su ID. Para eliminar el item de la lista no es el id de la clase sino la posicion en la lista empieza desde CERO.

## Ejecucion
Ejecute el siguiente comando para inicar la aplicacion
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
