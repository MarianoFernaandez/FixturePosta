from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Cancha(Base):
    __tablename__ = 'canchas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(255))
    tamaño = Column(String(50))  # Puedes definir un ENUM si lo prefieres
    tipoSuperficie = Column(String(50))  # Puedes definir un ENUM si lo prefieres

    # Relación con Partido
    partidos = relationship("Partido")  # Un partido puede estar asociado a una cancha

    # CRUD Cancha
    @classmethod
    def agregar_cancha(cls, nombre: str, ubicacion: str, tamaño: str, tipoSuperficie: str):
        nueva_cancha = cls(
            nombre=nombre,
            ubicacion=ubicacion,
            tamaño=tamaño,
            tipoSuperficie=tipoSuperficie
        )
        session = sessionmaker(bind=engine)()
        session.add(nueva_cancha)
        session.commit()
        session.refresh(nueva_cancha)
        session.close()
        return nueva_cancha
    
    @classmethod
    def obtener_todas_las_canchas(cls):
        session = sessionmaker(bind=engine)()
        canchas = session.query(cls).all()  # Consulta para obtener todas las canchas
        session.close()
        return canchas
    
    @classmethod
    def eliminar_cancha(cls, cancha_id: int):
        session = sessionmaker(bind=engine)()
        cancha = session.query(cls).filter(cls.id == cancha_id).first()  # Busca la cancha por ID
        if cancha:
            session.delete(cancha)  # Elimina la cancha
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Cancha eliminada exitosamente"}
        else:
            session.close()
            return {"message": "Cancha no encontrada"}
        
    @classmethod
    def modificar_cancha(cls, cancha_id: int, nombre: str, ubicacion: str, tamaño: str, tipoSuperficie: str):
        session = sessionmaker(bind=engine)()
        cancha = session.query(cls).filter(cls.id == cancha_id).first()  # Busca la cancha por ID
        if cancha:
            cancha.nombre = nombre
            cancha.ubicacion = ubicacion
            cancha.tamaño = tamaño
            cancha.tipoSuperficie = tipoSuperficie
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Cancha modificada exitosamente"}
        else:
            session.close()
            return {"message": "Cancha no encontrada"}