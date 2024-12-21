from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel


class Inventario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    detalle: str
    familia: str
    cantidad: float
    precio: float
    total: float


class InventarioUpdate(BaseModel):
    detalle: Optional[str] = None
    familia: Optional[str] = None
    cantidad: Optional[float] = None
    precio: Optional[float] = None
