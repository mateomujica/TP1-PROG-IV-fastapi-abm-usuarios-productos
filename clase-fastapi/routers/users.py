from typing import Optional
from fastapi import APIRouter, HTTPException, status
from models.users import (
    User,
    GetUsersResponse,
    CreateUserResponse,
    DeleteUserResponse,
    UpdateUserResponse,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez"),
]


@router.get("/user")
def get_users(is_active: Optional[bool] = None) -> GetUsersResponse:
    if is_active is None:
        return GetUsersResponse(users=usuarios)

    filtrados = [u for u in usuarios if u.is_active == is_active]
    return GetUsersResponse(users=filtrados)


@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="ususario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


@router.post("/user")
def create_user(user: User) -> CreateUserResponse:
    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")


@router.put("/user/{id}")
def update_user(id: int, datos: User) -> UpdateUserResponse:
    for index, user in enumerate(usuarios):
        if user.id == id:
            usuarios[index] = datos
            return UpdateUserResponse(message="usuario actualizado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )