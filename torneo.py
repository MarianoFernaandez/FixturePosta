from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine
from models import TorneoModel
from enum import Enum 

class Torneo(Base): 
    __tablename__ = 'torneos'

    id_torneo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    fechaInicio = Column(Date, nullable=False)  
    fechaFin = Column(Date, nullable=False)
    cantidadEquipos = Column(Integer, nullable=False)

    # Relación con TorneoEquipo
    torneos = relationship("TorneoEquipo", back_populates="torneo")

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

    # @classmethod
    # def mostrar_torneos(cls):
    #     session = sessionmaker(bind=engine)()
    #     try:
    #         torneos = session.query(cls).all()
    #     finally:
    #         session.close()
    #     return torneos

    # @classmethod
    # def eliminar_torneo(cls, torneo_id: int):
    #     session = sessionmaker(bind=engine)()
    #     try:
    #         torneo = session.query(cls).filter_by(id_torneo=torneo_id).first()
    #         if torneo:
    #             session.delete(torneo)
    #             session.commit()
    #             return True
    #         return False
    #     except Exception as e:
    #         session.rollback()
    #         raise Exception(f"Error al eliminar el torneo: {e}")
    #     finally:
    #         session.close()

    # @classmethod
    # def modificar_torneo(cls, torneo_id: int, torneo_in: TorneoModel):
    #     session = sessionmaker(bind=engine)()
    #     try:
    #         torneo_existente = session.query(cls).filter(cls.id_torneo == torneo_id).one_or_none()
    #         if not torneo_existente:
    #             raise Exception(f"Torneo con id {torneo_id} no encontrado")

    #         torneo_existente.nombre = torneo_in.nombre
    #         torneo_existente.fechaInicio = torneo_in.fechaInicio
    #         torneo_existente.fechaFin = torneo_in.fechaFin
    #         torneo_existente.cantidadEquipos = torneo_in.cantidadEquipos

    #         session.commit()
    #         session.refresh(torneo_existente)
    #     except Exception as e:
    #         session.rollback()
    #         raise Exception(f"Error al modificar el torneo: {e}")
    #     finally:
    #         session.close()

    #     return TorneoModel(
    #         id=torneo_existente.id_torneo,
    #         nombre=torneo_existente.nombre,
    #         fechaInicio=torneo_existente.fechaInicio,
    #         fechaFin=torneo_existente.fechaFin,
    #         cantidadEquipos=torneo_existente.cantidadEquipos
    #     )

    # @classmethod
    # def asociar_equipo(cls, torneo_id: int, equipo_id: int):
    #     from torneoEquipo import TorneoEquipo
    #     session = sessionmaker(bind=engine)()
    #     try:
    #         # Crear la relación en la tabla intermedia
    #         relacion = TorneoEquipo(torneo_id=torneo_id, equipo_id=equipo_id)
    #         session.add(relacion)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         raise Exception(f"Error al asociar el torneo con el equipo: {e}")
    #     finally:
    #         session.close()
