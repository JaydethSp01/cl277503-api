from pydantic import BaseModel

class Tarea(BaseModel):
    id: int
    titulo: str
    estado: str