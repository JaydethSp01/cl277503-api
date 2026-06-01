from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

usuarios_db = []

class Usuario(BaseModel):
    id: int
    nombre: str

class UsuarioCreate(BaseModel):
    nombre: str

@router.get("/usuarios", response_model=List[Usuario])
def get_usuarios():
    return usuarios_db

@router.post("/usuarios", response_model=Usuario)
def create_usuario(usuario: UsuarioCreate):
    nuevo_usuario = Usuario(id=len(usuarios_db) + 1, nombre=usuario.nombre)
    usuarios_db.append(nuevo_usuario)
    return nuevo_usuario

@router.delete("/usuarios/{usuario_id}")
def delete_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            usuarios_db.remove(usuario)
            return {"message": "Usuario deleted"}
    raise HTTPException(status_code=404, detail="Usuario not found")
