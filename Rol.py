from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Rol(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(String(50), nullable=False)  # Cambiado de 'nombre' a 'rol'

    jugadores = relationship("Jugador", secondary="jugador_rol", back_populates="roles")
    
    # CRUD Rol
    @classmethod
    def agregar_rol(cls, rol: str):
        nuevo_rol = cls(rol=rol)
        session = sessionmaker(bind=engine)()
        session.add(nuevo_rol)
        session.commit()
        session.refresh(nuevo_rol)
        session.close()
        return nuevo_rol
    
    @classmethod
    def obtener_todos_los_roles(cls):
        session = sessionmaker(bind=engine)()
        roles = session.query(cls).all()  # Asegúrate de que la consulta esté usando el nombre correcto
        session.close()
        return roles
        
    @classmethod
    def modificar_rol(cls, rol_id: int, rol: str):
        session = sessionmaker(bind=engine)()
        rol_obj = session.query(cls).filter(cls.id == rol_id).first()  # Busca el rol por ID
        if rol_obj:
            rol_obj.rol = rol
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Rol modificado exitosamente"}
        else:
            session.close()
            return {"message": "Rol no encontrado"}