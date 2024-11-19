from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import sessionmaker
from database import Base, engine, relationship
from models import ArbitroModel  # Asegúrate de que el modelo Pydantic esté importado
from partido import Partido  # Importar la clase Partido para la validación

# Defino la clase Arbitro
class Arbitro(Base):
    __tablename__ = 'arbitros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    apyn = Column(String(200))
    idPartido = Column(Integer, ForeignKey('partidos.id'))  # Relación con Partido

    # Relación hacia Partido
    partido = relationship("Partido", back_populates="arbitros")

    # CRUD Arbitro

    @classmethod
    def agregar_arbitro(cls, apyn: str, idPartido: int):
        session = sessionmaker(bind=engine)()
        
        # Validar que el partido existe
        partido_existente = session.query(Partido).filter_by(id=idPartido).first()
        if not partido_existente:
            session.close()
            raise Exception(f"El partido con id {idPartido} no existe.")

        nuevo_arbitro = cls(
            apyn=apyn,
            idPartido=idPartido
        )
        try:
            session.add(nuevo_arbitro)
            session.commit()
            session.refresh(nuevo_arbitro)
        except Exception as e:
            session.rollback()  # Deshacer la transacción en caso de error
            raise Exception(f"Error al agregar el árbitro: {e}")
        finally:
            session.close()
        return nuevo_arbitro

    @classmethod
    def mostrar_arbitros(cls):
        session = sessionmaker(bind=engine)()
        try:
            arbitros = session.query(cls).all()
        finally:
            session.close()
        return arbitros

    @classmethod
    def buscar_arbitro(cls, arbitro_id: int):
        session = sessionmaker(bind=engine)()
        try:
            arbitro = session.query(cls).filter_by(id=arbitro_id).first()
        finally:
            session.close()
        return arbitro

    @classmethod
    def eliminar_arbitro(cls, arbitro_id: int):
        session = sessionmaker(bind=engine)()
        try:
            arbitro = session.query(cls).filter_by(id=arbitro_id).first()
            if arbitro:
                session.delete(arbitro)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()  # Deshacer la transacción en caso de error
            raise Exception(f"Error al eliminar el árbitro: {e}")
        finally:
            session.close()

    @classmethod
    def modificar_arbitro(cls, arbitro_id: int, arbitro_in: ArbitroModel):
        session = sessionmaker(bind=engine)()
        try:
            arbitro_existente = session.query(cls).filter(cls.id == arbitro_id).one_or_none()
            if not arbitro_existente:
                raise Exception(f"Árbitro con id {arbitro_id} no encontrado")

            arbitro_existente.apyn = arbitro_in.apyn
            arbitro_existente.idPartido = arbitro_in.idPartido  # Actualizar id del partido

            session.commit()
            session.refresh(arbitro_existente)
        except Exception as e:
            session.rollback()  # Deshacer la transacción en caso de error
            raise Exception(f"Error al modificar el árbitro: {e}")
        finally:
            session.close()

        return ArbitroModel(
            id=arbitro_existente.id,
            apyn=arbitro_existente.apyn,
            idPartido=arbitro_existente.idPartido
        )

    @classmethod
    def buscar_arbitros_por_partido(cls, partido_id: int):
        session = sessionmaker(bind=engine)()
        try:
            arbitros = session.query(cls).filter_by(idPartido=partido_id).all()
        finally:
            session.close()
        return arbitros