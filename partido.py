from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy import sessionmaker
from database import Base, engine, relationship
from models import PartidoModel
from equipo import Equipo  # Asegúrate de importar la clase Equipo
from cancha import Cancha  # Asegúrate de importar la clase Cancha
from arbitro import Arbitro  # Asegúrate de importar la clase Arbitro
from fecha import Fecha  # Asegúrate de importar la clase Fecha

# Defino la clase Partido
class Partido(Base): 
    __tablename__ = 'partidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idEquipoLocal = Column(Integer, ForeignKey('equipos.id_equipo'))
    idEquipoVisitante = Column(Integer, ForeignKey('equipos.id_equipo'))
    golLocal = Column(Integer)
    golVisitante = Column(Integer)

    # Relaciones hacia Equipos
    equipo_local = relationship("Equipo", foreign_keys=[idEquipoLocal])
    equipo_visitante = relationship("Equipo", foreign_keys=[idEquipoVisitante])
    
    # Relación con Cancha
    cancha_id = Column(Integer, ForeignKey('canchas.id'))  # Clave foránea para la cancha
    cancha = relationship("Cancha", back_populates="partidos")  # Un partido está asociado a una única cancha

    # Relación con Arbitro
    idArbitro = Column(Integer, ForeignKey('arbitros.id'))  # Clave foránea para el árbitro
    arbitros = relationship("Arbitro", back_populates="partido")  # Un árbitro puede estar en varios partidos

    # Relación con Fecha
    fecha_id = Column(Integer, ForeignKey('fechas.id'))  # Clave foránea para la fecha
    fecha = relationship("Fecha", back_populates="partidos")  # Un partido está asociado a una única fecha

    # CRUD Partido

    @classmethod
    def agregar_partido(cls, idEquipoLocal: int, idEquipoVisitante: int, golLocal: int, golVisitante: int, idArbitro: int, cancha_id: int, fecha_id: int):
        session = sessionmaker(bind=engine)()
        
        # Validar que los equipos existen
        equipo_local = session.query(Equipo).filter_by(id_equipo=idEquipoLocal).first()
        equipo_visitante = session.query(Equipo).filter_by(id_equipo=idEquipoVisitante).first()

        if not equipo_local:
            session.close()
            raise Exception(f"El equipo local con id {idEquipoLocal} no existe.")
        if not equipo_visitante:
            session.close()
            raise Exception(f"El equipo visitante con id {idEquipoVisitante} no existe.")

        # Validar que los goles son números no negativos
        if golLocal < 0 or golVisitante < 0:
            session.close()
            raise Exception("Los goles no pueden ser negativos.")

        # Crear el nuevo partido
        nuevo_partido = cls(
            idEquipoLocal=idEquipoLocal,
            idEquipoVisitante=idEquipoVisitante,
            golLocal=golLocal,
            golVisitante=golVisitante,
            idArbitro=idArbitro,
            cancha_id=cancha_id,
            fecha_id=fecha_id
        )
        session.add(nuevo_partido)
        session.commit()
        session.refresh(nuevo_partido)
        session.close()
        return nuevo_partido

    @classmethod
    def mostrar_partidos(cls):
        session = sessionmaker(bind=engine)()
        partidos = session.query(cls).all()
        session.close()
        return partidos

    @classmethod
    def buscar_partido(cls, partido_id: int):
        session = sessionmaker(bind=engine)()
        partido = session.query(cls).filter_by(id=partido_id).first()
        session.close()
        return partido

    @classmethod
    def eliminar_partido(cls, partido_id: int):
        session = sessionmaker(bind=engine)()
        partido = session.query(cls).filter_by(id=partido_id).first()
        if partido:
            session.delete(partido)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def modificar_partido(cls, partido_id: int, partido_in: PartidoModel):
        session = sessionmaker(bind=engine)()
        
        # Verificar si el partido existe
        partido_existente = session.query(cls).filter(cls.id == partido_id).one_or_none()
        if not partido_existente:
            session.close()
            raise Exception(f"Part ido con id {partido_id} no encontrado.")

        # Validar que los equipos existen
        equipo_local = session.query(Equipo).filter_by(id_equipo=partido_in.idEquipoLocal).first()
        equipo_visitante = session.query(Equipo).filter_by(id_equipo=partido_in.idEquipoVisitante).first()

        if not equipo_local:
            session.close()
            raise Exception(f"El equipo local con id {partido_in.idEquipoLocal} no existe.")
        if not equipo_visitante:
            session.close()
            raise Exception(f"El equipo visitante con id {partido_in.idEquipoVisitante} no existe.")

        # Validar que los goles son números no negativos
        if partido_in.golLocal < 0 or partido_in.golVisitante < 0:
            session.close()
            raise Exception("Los goles no pueden ser negativos.")

        # Actualizar los datos del partido existente
        partido_existente.idEquipoLocal = partido_in.idEquipoLocal
        partido_existente.idEquipoVisitante = partido_in.idEquipoVisitante
        partido_existente.golLocal = partido_in.golLocal
        partido_existente.golVisitante = partido_in.golVisitante
        partido_existente.idArbitro = partido_in.idArbitro
        partido_existente.cancha_id = partido_in.cancha_id
        partido_existente.fecha_id = partido_in.fecha_id

        session.commit()
        session.close()
        return partido_existente