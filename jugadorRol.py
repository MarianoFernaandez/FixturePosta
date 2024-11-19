from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from database import Base, engine

class JugadorRol(Base):
    __tablename__ = 'jugador_rol'

    jugador_id = Column(Integer, ForeignKey('jugadores.id'), primary_key=True)
    rol_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)

    @classmethod
    def agregar_asociacion(cls, jugador_id: int, rol_id: int):
        session = sessionmaker(bind=engine)()
        # Verificar si la asociación ya existe
        if session.query(cls).filter_by(jugador_id=jugador_id, rol_id=rol_id).first() is not None:
            session.close()
            return {"message": "La asociación ya existe."}
        
        nueva_asociacion = cls(jugador_id=jugador_id, rol_id=rol_id)
        session.add(nueva_asociacion)
        session.commit()
        session.refresh(nueva_asociacion)
        session.close()
        return {"message": "Asociación creada exitosamente", "jugador_rol_id": (jugador_id, rol_id)}

    @classmethod
    def eliminar_asociacion(cls, jugador_id: int, rol_id: int):
        session = sessionmaker(bind=engine)()
        # Buscar la asociación
        asociacion = session.query(cls).filter_by(jugador_id=jugador_id, rol_id=rol_id).first()
        if asociacion:
            session.delete(asociacion)  # Eliminar la asociación
            session.commit()  # Confirmar los cambios
            session.close()
            return {"message": "Asociación eliminada exitosamente"}
        else:
            session.close()
            return {"message": "Asociación no encontrada"}
    
    @classmethod
    def obtener_todas_asociaciones(cls):
        session = sessionmaker(bind=engine)()
        asociaciones = session.query(cls).all()  # Obtener todas las asociaciones
        session.close()
        return asociaciones