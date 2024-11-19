from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Equipo(Base): 
    __tablename__ = 'equipos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    escudo = Column(String(255), nullable=False)
    ciudad = Column(String(255), nullable=False)
    fechaFundacion = Column(Date, nullable=False)

    # Relación con TorneoEquipo se define después
    # equipos = relationship("TorneoEquipo", back_populates="equipo")

    # CRUD Equipo
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
    def obtener_todos_los_equipos(cls):
        session = sessionmaker(bind=engine)()
        equipos = session.query(cls).all()  # Consulta para obtener todos los equipos
        session.close()
        return equipos
    
    @classmethod
    def eliminar_equipo(cls, equipo_id: int):
        session = sessionmaker(bind=engine)()
        equipo = session.query(cls).filter(cls.id == equipo_id).first()  # Busca el equipo por ID
        if equipo:
            session.delete(equipo)  # Elimina el equipo
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Equipo eliminado exitosamente"}
        else:
            session.close()
            return {"message": "Equipo no encontrado"}
        
    @classmethod
    def modificar_equipo(cls, equipo_id: int, nombre: str, escudo: str, ciudad: str, fechaFundacion: Date):
        session = sessionmaker(bind=engine)()
        equipo = session.query(cls).filter(cls.id == equipo_id).first()  # Busca el equipo por ID
        if equipo:
            equipo.nombre = nombre
            equipo.escudo = escudo
            equipo.ciudad = ciudad
            equipo.fechaFundacion = fechaFundacion
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Equipo modificado exitosamente"}
        else:
            session.close()
            return {"message": "Equipo no encontrado"}


# Importar TorneoEquipo aquí para evitar problemas de referencia circular
from torneoEquipo import TorneoEquipo

# Definir la relación aquí, después de que ambas clases están definidas
Equipo.equipos = relationship("TorneoEquipo", back_populates="equipo")