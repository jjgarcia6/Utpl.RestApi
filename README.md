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

## Especificacion del Caso de Estudio 

Para la implementacion del Portal de Comercio Electronico para ABC Motor, es necesario que desarrollemos API's que permitan la integracion de diferentes herramientas y desarrollos externos. Como por ejemplo, un carrito de compras, distintas pasarelas de pago, agendamiento de citas, por nombrar algunas.

Tambien necesitamos integrarnos con el ERP KERP que es el sistema que usa la empresa, con el proposito de obtener el inventario actualizado y poder mantener al dia nuestra oferta de productos online. 

**La API de Gestión de Inventarios está diseñada para facilitar la administración de inventarios de ABC Motor**. Utiliza FastAPI, un framework moderno y de alto rendimiento para construir APIs con Python.

![Pantalla de FastAPI con los metodos](/images/01_main.PNG)

## C4 Model

Como parte de este proyecto en el archivo `c4model.txt` encontraran el codigo del diseño de la Arquitectura C4 Model propuesta, esta desarrollada de forma parcial.

Pueden ejecutar el diseño en `https://structurizr.com`

Se incluye dos de los diagramas desarrollados.

**Diagrama de Contexto:**
![Diagrama de Contexto](/images/Contexto.png)


**Diagrama de Contenedor**
![Diagrama de Contenedor](/images/Contenedor.png)


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
  "detalle": "Foco LED",
  "familia": "Accesorios",
  "cantidad": 10,
  "precio": 1,
  "total": 10
}
```


**3) Actualizar un inventario**  
URL: `/inventarios/{inventario_id}` 
Método: `PUT`  
Descripción: Para actualizar el item de la lista no es el id de la clase sino la posición en la lista empieza desde CERO.  
Cuerpo de la solicitud:  

Ejemplo:  

```json
{
  "id": 1,
  "detalle": "Foco LED",
  "familia": "Accesorios",
  "cantidad": 5,
  "precio": 1,
  "total": 5
}
```


**4) Eliminar un inventario**  
URL: `/inventarios/{inventario_id}`  
Método: `DELETE`  
Descripción: Para eliminar el item de la lista no es el id de la clase sino la posición en la lista empieza desde CERO.  


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

![Muestra los productos registrados](/images/GET.PNG)


### Crear un nuevo inventario
**URL**: `/inventarios`  
**Método**: `POST`  
**Descripción**: Crea un nuevo inventario.  
**Cuerpo de la solicitud**:  
```json
{
  "id": 1,
  "detalle": "Foco LED",
  "familia": "Accesorios",
  "cantidad": 10,
  "precio": 1,
  "total": 10
}
```

![Muestra los productos registrados](/images/POST.PNG)


### Actualiza un inventario
**URL**: `/inventarios/{inventario_id}`  
**Método**: `PUT`  
**Descripción**: Para actualizar el item de la lista no es el id de la clase sino la posición en la lista empieza desde CERO.   

**Para poder hacer el PUT deben realizar el paso detallado a continuacion, en caso contrario no podran realizarlo y les saldra error**

En HEADERS deben colocar

KEY: `Content-Type`  
VALUE: `application/json`  

En BODY deben seleccionar `RAW` y `JSON`

**Cuerpo de la solicitud**:  
```json
{
  "id": 1,
  "detalle": "Foco LED",
  "familia": "Accesorios",
  "cantidad": 5,
  "precio": 1,
  "total": 5
}
```

![Muestra los productos registrados](/images/PUT.PNG)

Si listamos el producto saldra asi:

![Muestra los productos registrados](/images/GET_PUT.PNG)


**Eliminar un inventario**  
URL: `/inventarios/{inventario_id}`  
Método: `DELETE`  
Descripción: Para eliminar el item de la lista no es el id de la clase sino la posición en la lista empieza desde CERO.  

![Muestra los productos registrados](/images/DELETE.PNG)

Si volvemos a listar, no saldra nada

![Muestra los productos registrados](/images/GET_DELETE.PNG)

Espero que les sirva de guia, muchas gracias
