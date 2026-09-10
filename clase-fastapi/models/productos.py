from pydantic import BaseModel
from typing import List


class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    categoria: str


class GetProductosResponse(BaseModel):
    productos: List[Producto]


class CreateProductoResponse(BaseModel):
    message: str


class DeleteProductoResponse(BaseModel):
    message: str


class UpdateProductoResponse(BaseModel):
    message: str