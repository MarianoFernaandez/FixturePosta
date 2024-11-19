from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Jugador(Base):
    __tablename__ = 'jugadores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    apyn = Column(String(200), nullable=False)  # Campo combinado de apellido y nombre
    fechaNacimiento = Column(Date, nullable=False)
    posicion = Column(String(50), nullable=False)
    numeroDeCamiseta = Column(Integer, nullable=False)
    equipo_id = Column(Integer, ForeignKey('equipos.id'))

    # Relación con Equipo
    equipo = relationship("Equipo", back_populates="jugadores")

    # CRUD Jugador
    @classmethod
    def agregar_jugador(cls, apyn: str, fechaNacimiento: Date, posicion: str, numeroDeCamiseta: int, equipo_id: int):
        nuevo_jugador = cls(
            apyn=apyn,
            fechaNacimiento=fechaNacimiento,
            posicion=posicion,
            numeroDeCamiseta=numeroDeCamiseta,
            equipo_id=equipo_id
        )
        session = sessionmaker(bind=engine)()
        session.add(nuevo_jugador)
        session.commit()
        session.refresh(nuevo_jugador)
        session.close()
        return nuevo_jugador
    
    @classmethod
    def obtener_todos_los_jugadores(cls):
        session = sessionmaker(bind=engine)()
        jugadores = session.query(cls).all()  # Consulta para obtener todos los jugadores
        session.close()
        return jugadores
    
    @classmethod
    def eliminar_jugador(cls, jugador_id: int):
        session = sessionmaker(bind=engine)()
        jugador = session.query(cls).filter(cls.id == jugador_id).first()  # Busca el jugador por ID
        if jugador:
            session.delete(jugador)  # Elimina el jugador
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Jugador eliminado exitosamente"}
        else:
            session.close()
            return {"message": "Jugador no encontrado"}
        
    @classmethod
    def modificar_jugador(cls, jugador_id: int, apyn: str, fechaNacimiento: Date, posicion: str, numeroDeCamiseta: int, equipo_id: int):
        session = sessionmaker(bind=engine)()
        jugador = session.query(cls).filter(cls.id == jugador_id).first()  # Busca el jugador por ID
        if jugador:
            jugador.apyn = apyn
            jugador.fechaNacimiento = fechaNacimiento
            jugador.posicion = posicion
            jugador.numeroDeCamiseta = numeroDeCamiseta
            jugador.equipo_id = equipo_id
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Jugador modificado exitosamente"}
        else:
            session.close()
            return {"message": "Jugador no encontrado"}

# Importar Equipo aquí para evitar problemas de referencia circular
from Equipo import Equipo

# Definir la relación aquí, después de que ambas clases están definidas
Equipo.jugadores = relationship("Jugador", back_populates="equipo")