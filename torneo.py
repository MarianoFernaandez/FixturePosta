from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy import sessionmaker
from database import Base, engine, relationship
from models import TorneoModel
from enum import Enum as PyEnum

class CantidadEquiposEnum(PyEnum):
    ocho = 8
    diez = 10
    doce = 12
    catorce = 14
    dieciseis = 16

#Defino la clase Torneo
class Torneo(Base): 
    __tablename__ = 'torneos'

    id_torneo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    fechaInicio = Column(Date)  
    fechaFin = Column(Date)
    cantidadEquipos = Column(Enum(CantidadEquiposEnum), nullable=False)
    equipo_id = Column(Integer, ForeignKey('equipos.id_equipo'))

    #Relaciono la clase Torneo con Equipo (unidireccional)

    torneos = relationship("Equipo")

    #CRUD Torneo

    @classmethod
    def agregar_torneo(cls, nombre: str, fechaInicio: Date, fechaFin: Date, cantidadEquipos: CantidadEquiposEnum, equipo_id: int):
        nuevo_torneo = cls(
            nombre=nombre,
            fechaInicio=fechaInicio,
            fechaFin=fechaFin,
            cantidadEquipos=cantidadEquipos,
            equipo_id=equipo_id
        )
        session = sessionmaker(bind=engine)()
        session.add(nuevo_torneo)
        session.commit()
        session.refresh(nuevo_torneo)
        session.close()
        return nuevo_torneo

    @classmethod
    def mostrar_torneos(cls):
        session = sessionmaker(bind=engine)()
        torneos = session.query(cls).all()
        session.close()
        return torneos

    @classmethod
    def eliminar_torneo(cls, torneo_id: int):
        session = sessionmaker(bind=engine)()
        torneo = session.query(cls).filter_by(id_torneo=torneo_id).first()
        if torneo:
            session.delete(torneo)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def modificar_torneo(cls, torneo_id: int, torneo_in: 'TorneoModel'):
        session = sessionmaker(bind=engine)()
        torneo_existente = session.query(cls).filter(cls.id_torneo == torneo_id).one_or_none()
        if not torneo_existente:
            session.close()
            raise Exception(f"Torneo con id {torneo_id} no encontrado")

        torneo_existente.nombre = torneo_in.nombre
        torneo_existente.fechaInicio = torneo_in.fechaInicio
        torneo_existente.fechaFin = torneo_in.fechaFin
        torneo_existente.cantidadEquipos = torneo_in.cantidadEquipos
        torneo_existente.equipo_id = torneo_in.equipo_id

        session.commit()
        session.refresh(torneo_existente)
        session.close()
        
        return TorneoModel(
            id=torneo_existente.id_torneo,
            nombre=torneo_existente.nombre,
            fechaInicio=torneo_existente.fechaInicio,
            fechaFin=torneo_existente.fechaFin,
            cantidadEquipos=torneo_existente.cantidadEquipos,
            equipo_id=torneo_existente.equipo_id
        )
