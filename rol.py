from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import sessionmaker
from database import Base, engine
from models import RolModel  # Importar el modelo Pydantic
from enum import Enum 

# Defino la clase Rol
class Rol(Base): 
    __tablename__ = 'roles'

    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(Enum('titular/capitan', 'titular', 'suplente', name='rol_enum'))

    # CRUD Rol

    @classmethod
    def agregar_rol(cls, rol_in: RolModel):
        nuevo_rol = cls(rol=rol_n.rol)  # Usar RolModel para crear el rol
        session = sessionmaker(bind=engine)()
        session.add(nuevo_rol)
        session.commit()
        session.refresh(nuevo_rol)
        session.close()
        return nuevo_rol

    @classmethod
    def mostrar_roles(cls):
        session = sessionmaker(bind=engine)()
        roles = session.query(cls).all()
        session.close()
        return roles  # Devolver la lista de roles

    @classmethod
    def buscar_rol(cls, rol_id: int):
        session = sessionmaker(bind=engine)()
        rol = session.query(cls).filter_by(id_rol=rol_id).first()
        session.close()
        if rol:
            return RolModel(id=rol.id_rol, rol=rol.rol)  # Devolver RolModel
        return None

    @classmethod
    def eliminar_rol(cls, rol_id: int):
        session = sessionmaker(bind=engine)()
        rol = session.query(cls).filter_by(id_rol=rol_id).first()
        if rol:
            session.delete(rol)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def modificar_rol(cls, rol_id: int, rol_in: RolModel):
        session = sessionmaker(bind=engine)()
        rol_existente = session.query(cls).filter(cls.id_rol == rol_id).one_or_none()
        if not rol_existente:
            session.close()
            raise Exception(f"Rol con id {rol_id} no encontrado")

        rol_existente.rol = rol_in.rol  # Usar RolModel para modificar el rol

        session.commit()
        session.refresh(rol_existente)
        session.close()

        return RolModel(id=rol_existente.id_rol, rol=rol_existente.rol)  # Devolver RolModel