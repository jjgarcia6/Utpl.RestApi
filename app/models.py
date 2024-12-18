from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel


class Orden(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    producto: str
    cantidad: float
    tipo: str
    precio: float
    total: float


class OrdenActualizacion(BaseModel):
    precio: Optional[float] = None,
    cantidad: Optional[float] = None
