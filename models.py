from pydantic import BaseModel
from datetime import date

# Modelo para la tabla Torneos
class TorneoModel(BaseModel):
    id: int = None
    nombre: str = None
    fechaInicio: date = None  # Usamos datetime.date para fechas
    fechaFin: date = None
    cantidadEquipos: int = None

    class Config:
        from_attributes = True

# Modelo para la tabla Equipos
class EquipoModel(BaseModel):
    id: int = None
    nombre: str = None
    escudo: str = None  # Representa una URL o imagen
    ciudad: str = None
    fechaFundacion: date = None  # Usamos datetime.date

    class Config:
        from_attributes = True

# Modelo para la tabla Jugadores
class JugadorModel(BaseModel):
    id: int = None
    apellido: str = None
    nombre: str = None
    fechaNacimiento: date = None  # Usamos datetime.date
    posicion: str = None  # ENUM('arquero', 'defensor', 'central', 'delantero')
    numeroDeCamiseta: int = None
    equipo_id: int = None

    class Config:
        from_attributes = True

# Modelo para la tabla Roles
class RolModel(BaseModel):
    id: int = None
    rol: str = None  # ENUM('titular/capitan', 'titular', 'suplente')

    class Config:
        from_attributes = True

# Modelo para la tabla Fixture
class FixtureModel(BaseModel):
    id: int = None
    idTorneo: int = None

    class Config:
        from_attributes = True

# Modelo para la tabla Fechas
class FechaModel(BaseModel):
    id: int = None
    idFixture: int = None
    fechaPartido: date = None  # Usamos datetime.date

    class Config:
        from_attributes = True

# Modelo para la tabla Partidos
class PartidoModel(BaseModel):
    id: int = None
    idEquipoLocal: int = None
    idEquipoVisitante: int = None
    golLocal: int = None
    golVisitante: int = None

    class Config:
        from_attributes = True

# Modelo para la tabla Arbitros
class ArbitroModel(BaseModel):
    id: int = None
    apyn: str = None
    idPartido: int = None

    class Config:
        from_attributes = True

# Modelo para la tabla Canchas
class CanchaModel(BaseModel):
    id: int = None
    nombre: str = None
    ubicacion: str = None
    tamaño: str = None  # ENUM('F5', 'F6', 'F7', 'F8')
    tipoSuperficie: str = None  # ENUM('piso', 'pasto')

    class Config:
        from_attributes = True
