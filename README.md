# Utpl.RestApi
Proyecto para trabajar con API en REST utilizando FastAPI


## Descripción del Proyecto

**Este proyecto es una aplicación web construida utilizando FastAPI.** FastAPI es un framework de Python moderno, rápido y fácil de usar para crear APIs. Es ideal para construir aplicaciones web backend que necesitan ser eficientes y escalables.

## Requisitos

* **Python:** Asegúrate de tener Python 3.6 o superior instalado.
* **FastAPI:** Instala FastAPI usando pip:
  ```bash
  pip install fastapi uvicorn
  ```

  
## Documentación 
## API de Gestión de Inventarios
**Este proyecto es una API RESTful construida con FastAPI para la gestión de inventarios de ABCMotor**. La API permite realizar operaciones CRUD (Crear-Create, Leer-Read, Actualizar-Update y Eliminar-Delete) sobre los inventarios.

## Descripción del Proyecto

**La API de Gestión de Inventarios está diseñada para facilitar la administración de inventarios de ABC Motor**. Utiliza FastAPI, un framework moderno y de alto rendimiento para construir APIs con Python.

## Endpoints
Los metodos que se usaron son los siguientes:

**1) Obtener todo el inventario**  
URL: `/inventarios`  
Método: `GET`  
Descripción: Devuelve una lista de todos productos en inventario.  


**2) Crear un nuevo inventario**  
URL: `/inventarios`  
Método: `POST`  
Descripción: Crea un nuevo inventario.  
Cuerpo de la solicitud:  

Ejemplo: 

```json
{
  "id": 1,
  "detalle": "Llanta 175/70R13",
  "familia": "Llantas",
  "cantidad": 3,
  "precio": 50.0,
  "total": 150.0
}
```


**3) Actualizar un inventario**  
URL: /inventarios/{inventario_id}  
Método: PUT  
Descripción: Actualiza un inventario existente por su ID.  
Cuerpo de la solicitud:  

Ejemplo:  

```json
{
  "id": 1,
  "detalle": "Llanta 175/70R13",
  "familia": "Llantas",
  "cantidad": 4,
  "precio": 50.0,
  "total": 150.0
}
```


**Eliminar un inventario**  
URL: `/inventarios/{inventario_id}`  
Método: `DELETE`  
Descripción: Elimina un inventario por su ID. Para eliminar el item de la lista no es el id de la clase sino la posición en la lista empieza desde CERO.  


## Ejecucion
Ejecute el siguiente comando para inicar la aplicacion
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
  ```


## Postman

A continuacion vamos a documentar las pruebas realizadas con Postman para la API de gestión de inventarios.

### Obtener todos los inventarios
**URL**: `/inventarios`  
**Método**: `GET`  
**Descripción**: Devuelve una lista de todos los inventarios.

### Crear un nuevo inventario
**URL**: `/inventarios`  
**Método**: `POST`  
**Descripción**: Crea un nuevo inventario.  
**Cuerpo de la solicitud**:  
```json
{
  "codigo": "ABC123",
  "descripcion": "Llanta 175/70R13",
  "familia": "Llantas",
  "clase": "Auto",
  "cantidad": 3,
  "precio": 50.0,
  "total": 150.0
}
```
