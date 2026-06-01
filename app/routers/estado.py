from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

estados_db = []

class Estado(BaseModel):
    id: int
    nombre: str

class EstadoCreate(BaseModel):
    nombre: str

@router.get("/estados", response_model=List[Estado])
def get_estados():
    return estados_db

@router.post("/estados", response_model=Estado)
def create_estado(estado: EstadoCreate):
    nuevo_estado = Estado(id=len(estados_db) + 1, nombre=estado.nombre)
    estados_db.append(nuevo_estado)
    return nuevo_estado

@router.delete("/estados/{estado_id}")
def delete_estado(estado_id: int):
    for estado in estados_db:
        if estado.id == estado_id:
            estados_db.remove(estado)
            return {"message": "Estado deleted"}
    raise HTTPException(status_code=404, detail="Estado not found")
