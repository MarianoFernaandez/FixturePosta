from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy import sessionmaker
from database import Base, engine, relationship
from models import CanchaModel  # Asegúrate de que el modelo Pydantic esté importado

# Defino la clase Cancha
class Cancha(Base):
    __tablename__ = 'canchas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(255))
    tamaño = Column(Enum('F5', 'F6', 'F7', 'F8'), nullable=False)  # Agregar nullable=False para asegurar que siempre se proporcione un tamaño
    tipoSuperficie = Column(Enum('piso', 'pasto'), nullable=False)  # Agregar nullable=False para asegurar que siempre se proporcione un tipo de superficie

    # Relación con Partidos
    partidos = relationship("Partido", back_populates="cancha")

    # CRUD Cancha

    @classmethod
    def agregar_cancha(cls, nombre: str, ubicacion: str, tamaño: str, tipoSuperficie: str):
        # Validar que el tamaño y tipo de superficie sean válidos
        if tamaño not in ['F5', 'F6', 'F7', 'F8']:
            raise ValueError("Tamaño inválido. Debe ser 'F5', 'F6', 'F7' o 'F8'.")
        if tipoSuperficie not in ['piso', 'pasto']:
            raise ValueError("Tipo de superficie inválido. Debe ser 'piso' o 'pasto'.")

        nueva_cancha = cls(
            nombre=nombre,
            ubicacion=ubicacion,
            tamaño=tamaño,
            tipoSuperficie=tipoSuperficie
        )
        session = sessionmaker(bind=engine)()
        try:
            session.add(nueva_cancha)
            session.commit()
            session.refresh(nueva_cancha)
        except Exception as e:
            session.rollback()  # Deshacer la transacción en caso de error
            raise Exception(f"Error al agregar la cancha: {e}")
        finally:
            session.close()
        return nueva_cancha

    @classmethod
    def mostrar_canchas(cls):
        session = sessionmaker(bind=engine)()
        try:
            canchas = session.query(cls).all()
        finally:
            session.close()
        return canchas

    @classmethod
    def buscar_cancha(cls, cancha_id: int):
        session = sessionmaker(bind=engine)()
        try:
            cancha = session.query(cls).filter_by(id=cancha_id).first()
        finally:
            session.close()
        return cancha

    @classmethod
    def eliminar_cancha(cls, cancha_id: int):
        session = sessionmaker(bind=engine)()
        try:
            cancha = session.query(cls).filter_by(id=cancha_id).first()
            if cancha:
                session.delete(cancha)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()  # Deshacer la transacción en caso de error
            raise Exception(f"Error al eliminar la cancha: {e}")
        finally:
            session.close()

    @classmethod
    def modificar_cancha(cls, cancha_id: int, cancha_in: CanchaModel):
        session = sessionmaker(bind=engine)()
        try:
            cancha_existente = session.query(cls).filter(cls.id == cancha_id).one_or_none()
            if not cancha_existente:
                raise Exception(f"Cancha con id {cancha_id} no encontrada")

            # Validar que el tamaño y tipo de superficie sean válidos
            if cancha_in.tamaño not in ['F5', 'F6', 'F7', 'F8']:
                raise ValueError("Tamaño inválido. Debe ser 'F5', 'F6', 'F7' o 'F8'.")
            if cancha_in.tipoSuperficie not in ['piso', 'pasto']:
                raise ValueError("Tipo de superficie inválido. Debe ser 'piso' o 'pasto'.")

            cancha_existente.nombre = cancha_in.nombre
            cancha_existente.ubicacion = cancha_in.ubicacion
            cancha_existente.tamaño = cancha_in.tamaño
            cancha_existente.tipoSuperficie = cancha_in.tipoSuperficie

            session.commit()
            session.refresh(cancha_existente)
        except Exception as e:
            session.rollback()  # Deshacer la transacción en caso de error
            raise Exception(f"Error al modificar la cancha: {e}")
        finally:
            session.close()

        return CanchaModel(
            id= cancha_existente.id,
            nombre=cancha_existente.nombre,
            ubicacion=cancha_existente.ubicacion,
            tamaño=cancha_existente.tamaño,
            tipoSuperficie=cancha_existente.tipoSuperficie
        )