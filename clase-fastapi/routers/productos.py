from fastapi import APIRouter
from typing import Optional
from models.productos import (
    Producto,
    GetProductosResponse,
    CreateProductoResponse,
    DeleteProductoResponse,
    UpdateProductoResponse
)
router = APIRouter()

productos: list[Producto] = [
    Producto(id=1, nombre="Auriculares Bluetooth", precio=15999.99, stock=20, categoria="Tecnologia"),
    Producto(id=2, nombre="Jabón líquido", precio=250.50, stock=50, categoria="Higiene"),
    Producto(id=3, nombre="Arroz", precio=500, stock=100, categoria="Comida"),
]

@router.get("/producto")
def get_productos(categoria: Optional[str] = None) -> GetProductosResponse:
    if categoria is None:
        return GetProductosResponse(productos=productos)

    filtrados = [p for p in productos if p.categoria.lower() == categoria.lower()]
    return GetProductosResponse(productos=filtrados)

@router.get("/producto/{id}")
def get_producto(id: int) -> Producto:
    for producto in productos:
        if producto.id == id:
            return producto

    return Producto(id=0, nombre="Producto no encontrado", precio=0.0, stock=0, categoria="")

@router.post("/producto")
def create_producto(producto: Producto) -> CreateProductoResponse:
    productos.append(producto)
    return CreateProductoResponse(message="producto creado")

@router.delete("/producto/{id}")
def delete_producto(id: int) -> DeleteProductoResponse:
    for producto in productos:
        if producto.id == id:
            productos.remove(producto)
            return DeleteProductoResponse(message="producto borrado")

    return DeleteProductoResponse(message="producto no encontrado")

@router.put("/producto/{id}")
def update_producto(id: int, datos: Producto) -> UpdateProductoResponse:
    for index, producto in enumerate(productos):
        if producto.id == id:
            productos[index] = datos
            return UpdateProductoResponse(message="producto actualizado")

    return UpdateProductoResponse(message="producto no encontrado")