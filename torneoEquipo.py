from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models import TorneoEquipo  # Importar TorneoEquipo si está en otro archivo


class TorneoEquipo(Base):
    __tablename__ = 'torneo_equipo'

    id_torneo_equipo = Column(Integer, primary_key=True, autoincrement=True)
    id_torneo = Column(Integer, ForeignKey('torneos.id_torneo'), nullable=False)
    id_equipo = Column(Integer, ForeignKey('equipos.id_equipo'), nullable=False)

    torneo = relationship("Torneo", back_populates="torneos")
    equipo = relationship("Equipo", back_populates="torneos")

