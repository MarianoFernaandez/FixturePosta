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

class EquipoModel(BaseModel):
    id: int
    nombre: str
    escudo: str
    ciudad: str
    fechaFundacion: date

    class Config:
        from_attributes = True

class JugadorModel(BaseModel):
    apyn: str  
    fechaNacimiento: date  
    posicion: str  
    numeroDeCamiseta: int  
    equipo_id: int  

    class Config:
        from_attributes = True

class RolModel(BaseModel):
    id: int  # ID del rol (esto puede ser opcional en algunos casos, dependiendo de cómo se use)
    rol: str  # Nombre del rol (por ejemplo, 'titular', 'suplente', etc.)

    class Config:
        from_attributes = True