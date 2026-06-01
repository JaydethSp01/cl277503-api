from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

tareas_db = []

class Tarea(BaseModel):
    id: int
    nombre: str
    estado: str = 'pendiente'

class TareaCreate(BaseModel):
    nombre: str

@router.get("/tareas", response_model=List[Tarea])
def get_tareas():
    return tareas_db

@router.post("/tareas", response_model=Tarea)
def create_tarea(tarea: TareaCreate):
    nueva_tarea = Tarea(id=len(tareas_db) + 1, nombre=tarea.nombre)
    tareas_db.append(nueva_tarea)
    return nueva_tarea

@router.patch("/tareas/{tarea_id}", response_model=Tarea)
def update_tarea(tarea_id: int, estado: str):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            tarea.estado = estado
            return tarea
    raise HTTPException(status_code=404, detail="Tarea not found")

@router.delete("/tareas/{tarea_id}")
def delete_tarea(tarea_id: int):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            tareas_db.remove(tarea)
            return {"message": "Tarea deleted"}
    raise HTTPException(status_code=404, detail="Tarea not found")
