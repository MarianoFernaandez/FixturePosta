from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import sessionmaker
from database import Base, engine, relationship
from models import EquipoModel

#Defino la clase Equipo
class Equipo(Base): 
    __tablename__ = 'equipos'

    id_equipo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    escudo = Column(String(255))
    ciudad = Column(String(100))
    fechaFundacion = Column(Date)

    #Relaciono la clase Equipo con Jugador

    jugadores = relationship("Jugador", back_populates="equipo")

    #Crud Equipo

    @classmethod
    def agregar_equipo(cls, nombre: str, escudo: str, ciudad: str, fechaFundacion: Date):
        nuevo_equipo = cls(
            nombre=nombre,
            escudo=escudo,
            ciudad=ciudad,
            fechaFundacion=fechaFundacion
        )
        session = sessionmaker(bind=engine)()
        session.add(nuevo_equipo)
        session.commit()
        session.refresh(nuevo_equipo)
        session.close()
        return nuevo_equipo

    @classmethod
    def mostrar_equipos(cls):
        session = sessionmaker(bind=engine)()
        equipos = session.query(cls).all()
        session.close()
        return equipos

    @classmethod
    def eliminar_equipo(cls, equipo_id: int):
        session = sessionmaker(bind=engine)()
        equipo = session.query(cls).filter_by(id_equipo=equipo_id).first()
        if equipo:
            session.delete(equipo)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def modificar_equipo(cls, equipo_id: int, equipo_in: EquipoModel):
        session = sessionmaker(bind=engine)()
        equipo_existente = session.query(cls).filter(cls.id_equipo == equipo_id).one_or_none()
        if not equipo_existente:
            session.close()
            raise Exception(f"Equipo con id {equipo_id} no encontrado")

        equipo_existente.nombre = equipo_in.nombre
        equipo_existente.escudo = equipo_in.escudo
        equipo_existente.ciudad = equipo_in.ciudad
        equipo_existente.fechaFundacion = equipo_in.fechaFundacion

        session.commit()
        session.refresh(equipo_existente)
        session.close()
        
        return EquipoModel(
            id=equipo_existente.id_equipo,
            nombre=equipo_existente.nombre,
            escudo=equipo_existente.escudo,
            ciudad=equipo_existente.ciudad,
            fechaFundacion=equipo_existente.fechaFundacion
        )



