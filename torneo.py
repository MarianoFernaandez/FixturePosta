from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Torneo(Base): 
    __tablename__ = 'torneos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    fechaInicio = Column(Date, nullable=False)  
    fechaFin = Column(Date, nullable=False)
    cantidadEquipos = Column(Integer, nullable=False)

    # Relación con TorneoEquipo se define después
    # torneos = relationship("TorneoEquipo", back_populates="torneo")

    # CRUD Torneo
    @classmethod
    def agregar_torneo(cls, nombre: str, fechaInicio: Date, fechaFin: Date, cantidadEquipos: int):
        nuevo_torneo = cls(
            nombre=nombre,
            fechaInicio=fechaInicio,
            fechaFin=fechaFin,
            cantidadEquipos=cantidadEquipos
        )
        session = sessionmaker(bind=engine)()
        session.add(nuevo_torneo)
        session.commit()
        session.refresh(nuevo_torneo)
        session.close()
        return nuevo_torneo
    
    @classmethod
    def obtener_todos_los_torneos(cls):
        session = sessionmaker(bind=engine)()
        torneos = session.query(cls).all()  # Consulta para obtener todos los torneos
        session.close()
        return torneos
    
    @classmethod
    def eliminar_torneo(cls, torneo_id: int):
        session = sessionmaker(bind=engine)()
        torneo = session.query(cls).filter(cls.id == torneo_id).first()  # Busca el torneo por ID
        if torneo:
            session.delete(torneo)  # Elimina el torneo
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Torneo eliminado exitosamente"}
        else:
            session.close()
            return {"message": "Torneo no encontrado"}
        
    @classmethod
    def modificar_torneo(cls, torneo_id: int, nombre: str, fechaInicio: Date, fechaFin: Date, cantidadEquipos: int):
        session = sessionmaker(bind=engine)()
        torneo = session.query(cls).filter(cls.id == torneo_id).first()  # Busca el torneo por ID
        if torneo:
            torneo.nombre = nombre
            torneo.fechaInicio = fechaInicio
            torneo.fechaFin = fechaFin
            torneo.cantidadEquipos = cantidadEquipos
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Torneo modificado exitosamente"}
        else:
            session.close()
            return {"message": "Torneo no encontrado"}


# Importar TorneoEquipo aquí para evitar problemas de referencia circular
from torneoEquipo import TorneoEquipo

# Definir la relación aquí, después de que ambas clases están definidas
Torneo.torneos = relationship("TorneoEquipo", back_populates="torneo")