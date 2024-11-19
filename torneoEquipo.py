from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TorneoEquipo(Base):
    __tablename__ = 'torneo_equipo'

    torneo_id = Column(Integer, ForeignKey('torneos.id'), primary_key=True)
    equipo_id = Column(Integer, ForeignKey('equipos.id'), primary_key=True)

    # Definir la relación aquí, pero no importes Equipo y Torneo todavía
    torneo = None  # Inicializa la relación como None
    equipo = None  # Inicializa la relación como None

# Importar las clases después de que ambas hayan sido definidas
from Torneo import Torneo
from Equipo import Equipo

# Ahora define las relaciones
TorneoEquipo.torneo = relationship("Torneo", back_populates="torneos")  # Relación con Torneo
TorneoEquipo.equipo = relationship("Equipo", back_populates="equipos")  # Relación con Equipo