from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Partido(Base):
    __tablename__ = 'partidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idEquipoLocal = Column(Integer, ForeignKey('equipos.id'), nullable=False)
    idEquipoVisitante = Column(Integer, ForeignKey('equipos.id'), nullable=False)
    idCancha = Column(Integer, ForeignKey('canchas.id'), nullable=False)
    golLocal = Column(Integer, default=0)
    golVisitante = Column(Integer, default=0)
    fechaPartido = Column(Date, nullable=False)

    # Relación con el equipo local
    equipoLocal = relationship("Equipo", foreign_keys=[idEquipoLocal], backref="partidos_locales")
    
    # Relación con el equipo visitante
    equipoVisitante = relationship("Equipo", foreign_keys=[idEquipoVisitante], backref="partidos_visitantes")

    # Relación con la cancha
    cancha = relationship("Cancha")  # Relación con Cancha

    # Relación con la Fecha (una fecha puede tener múltiples partidos)
    idFecha = Column(Integer, ForeignKey('fechas.id'), nullable=False)

    # CRUD Partido
    @classmethod
    def agregar_partido(cls, idEquipoLocal: int, idEquipoVisitante: int, idCancha:int, golLocal: int, golVisitante: int, fechaPartido: Date):
        nuevo_partido = cls(
            idEquipoLocal=idEquipoLocal,
            idEquipoVisitante=idEquipoVisitante,
            idCancha=idCancha,
            golLocal=golLocal,  # Agregar este parámetro
            golVisitante=golVisitante,  # Agregar este parámetro
            fechaPartido=fechaPartido
        )
        session = sessionmaker(bind=engine)()
        session.add(nuevo_partido)
        session.commit()
        session.refresh(nuevo_partido)
        session.close()
        return nuevo_partido
    
    @classmethod
    def obtener_todos_los_partidos(cls):
        session = sessionmaker(bind=engine)()
        partidos = session.query(cls).all()  # Consulta para obtener todos los partidos
        session.close()
        return partidos
    
    @classmethod
    def eliminar_partido(cls, partido_id: int):
        session = sessionmaker(bind=engine)()
        partido = session.query(cls).filter(cls.id == partido_id).first()  # Busca el partido por ID
        if partido:
            session.delete(partido)  # Elimina el partido
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Partido eliminado exitosamente"}
        else:
            session.close()
            return {"message": "Partido no encontrado"}
        
    @classmethod
    def modificar_partido(cls, partido_id: int, idEquipoLocal: int, idEquipoVisitante: int,idCancha: int, golLocal: int, golVisitante: int, fechaPartido: Date):
        session = sessionmaker(bind=engine)()
        partido = session.query(cls).filter(cls.id == partido_id).first()  # Busca el partido por ID
        if partido:
            partido.idEquipoLocal = idEquipoLocal
            partido.idEquipoVisitante = idEquipoVisitante
            partido.idCancha = idCancha
            partido.golLocal = golLocal
            partido.golVisitante = golVisitante
            partido.fechaPartido = fechaPartido
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Partido modificado exitosamente"}
        else:
            session.close()
            return {"message": "Partido no encontrado"}