from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy import sessionmaker
from database import Base, engine, relationship
from models import JugadorModel

#Defino la clase Jugador
class Jugador(Base): 
    __tablename__ = 'jugadores'

    id_jugador = Column(Integer, primary_key=True, autoincrement=True)
    apyn = Column(String(255))
    fechaNacimiento = Column(Date)  
    posicion = Column(Enum('arquero', 'defensor', 'central', 'delantero', name='posicion_enum'))
    numeroCamiseta = Column(Integer)
    equipo_id = Column(Integer, ForeignKey('equipos.id_equipo'))


    #Relaciono la clase Jugador con Equipo

    jugadores = relationship("Equipo", back_populates="jugador")

    #Crud Jugador

    @classmethod
    def agregar_jugador(cls, apyn: str, fechaNacimiento: Date, posicion: str, numeroCamiseta: int, equipo_id: int):
        nuevo_jugador = cls(
            apyn=apyn,
            fechaNacimiento=fechaNacimiento,
            posicion=posicion,
            numeroCamiseta=numeroCamiseta,
            equipo_id=equipo_id
        )
        session = sessionmaker(bind=engine)()
        session.add(nuevo_jugador)
        session.commit()
        session.refresh(nuevo_jugador)
        session.close()
        return nuevo_jugador

    @classmethod
    def mostrar_jugadores(cls):
        session = sessionmaker(bind=engine)()
        jugadores = session.query(cls).all()
        session.close()
        return 
    
    @classmethod
    def buscar_jugador(cls, jugador_id: int):
        session = sessionmaker(bind=engine)()
        jugador = session.query(cls).filter_by(id_jugador=jugador_id).first()
        session.close()
        if jugador:
            return JugadorModel(
                id=jugador.id_jugador,
                apyn=jugador.apyn,
                fechaNacimiento=jugador.fechaNacimiento,
                posicion=jugador.posicion,
                numeroCamiseta=jugador.numeroCamiseta,
                equipo_id=jugador.equipo_id
            )
        return None

    @classmethod
    def eliminar_jugador(cls, jugador_id: int):
        session = sessionmaker(bind=engine)()
        jugador = session.query(cls).filter_by(id_jugador=jugador_id).first()
        if jugador:
            session.delete(jugador)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def modificar_jugador(cls, jugador_id: int, jugador_in: JugadorModel):
        session = sessionmaker(bind=engine)()
        jugador_existente = session.query(cls).filter(cls.id_jugador == jugador_id).one_or_none()
        if not jugador_existente:
            session.close()
            raise Exception(f"Jugador con id {jugador_id} no encontrado")

        jugador_existente.apyn = jugador_in.apyn
        jugador_existente.fechaNacimiento = jugador_in.fechaNacimiento
        jugador_existente.posicion = jugador_in.posicion
        jugador_existente.numeroCamiseta = jugador_in.numeroCamiseta
        jugador_existente.equipo_id = jugador_in.equipo_id

        session.commit()
        session.refresh(jugador_existente)
        session.close()

        return JugadorModel(
            id=jugador_existente.id_jugador,
            apyn=jugador_existente.apyn,
            fechaNacimiento=jugador_existente.fechaNacimiento,
            posicion=jugador_existente.posicion,
            numeroCamiseta=jugador_existente.numeroCamiseta,
            equipo_id=jugador_existente.equipo_id
        )


