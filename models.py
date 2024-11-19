from pydantic import BaseModel
from datetime import date
from pydantic import BaseModel
from typing import Optional

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

class PartidoModel(BaseModel):
    idEquipoLocal: int
    idEquipoVisitante: int
    idCancha: int 
    golLocal: Optional[int] = None  # Cambia a Optional
    golVisitante: Optional[int] = None  # Cambia a Optional
    fechaPartido: date

    class Config:
        from_attributes =True
        
class CanchaModel(BaseModel):
    id: int  # ID de la cancha, requerido
    nombre: str
    ubicacion: str
    tamaño: str  # Puedes usar un tipo específico o ENUM si es necesario
    tipoSuperficie: str  # Puedes usar un tipo específico o ENUM si es necesario

    class Config:
        from_attributes = True

class ArbitroModel(BaseModel):
    id: int  
    apyn: str  
    idPartido: int  

    class Config:
        from_attributes = True