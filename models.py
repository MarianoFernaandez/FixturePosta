from pydantic import BaseModel
from datetime import date
from pydantic import BaseModel

class TorneoModel(BaseModel):
    id: int
    nombre: str
    fechaInicio: date
    fechaFin: date
    cantidadEquipos: int

    class Config:
        from_attributes = True

