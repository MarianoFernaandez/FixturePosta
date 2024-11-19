from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from Torneo import Torneo  # Asegúrate de que esta importación esté presente

class TorneoEquipo(Base):
    __tablename__ = 'torneo_equipo'

    torneo_id = Column(Integer, ForeignKey('torneos.id'), primary_key=True)  # Asegúrate de que la referencia sea correcta
    equipo_id = Column(Integer, ForeignKey('Equipos(id)'), nullable=False)

    torneo = relationship("Torneo", back_populates="torneos")  # Esta relación ahora debería funcionar correctamente