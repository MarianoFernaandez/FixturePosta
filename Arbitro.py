from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Arbitro(Base):
    __tablename__ = 'arbitros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    apyn = Column(String(200), nullable=False)  # Apellido y nombre del árbitro
    idPartido = Column(Integer, ForeignKey('partidos.id'), nullable=False)  # Clave foránea a la tabla partidos

    # Relación con Partido
    partido = relationship("Partido", backref="arbitros")  # Un árbitro puede estar asociado a muchos partidos

    # CRUD Arbitro
    @classmethod
    def agregar_arbitro(cls, apyn: str, idPartido: int):
        nuevo_arbitro = cls(
            apyn=apyn,
            idPartido=idPartido
        )
        session = sessionmaker(bind=engine)()
        session.add(nuevo_arbitro)
        session.commit()
        session.refresh(nuevo_arbitro)
        session.close()
        return nuevo_arbitro
    
    @classmethod
    def obtener_todos_los_arbitros(cls):
        session = sessionmaker(bind=engine)()
        arbitros = session.query(cls).all()  # Consulta para obtener todos los árbitros
        session.close()
        return arbitros
    
    @classmethod
    def eliminar_arbitro(cls, arbitro_id: int):
        session = sessionmaker(bind=engine)()
        arbitro = session.query(cls).filter(cls.id == arbitro_id).first()  # Busca el árbitro por ID
        if arbitro:
            session.delete(arbitro)  # Elimina el árbitro
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Árbitro eliminado exitosamente"}
        else:
            session.close()
            return {"message": "Árbitro no encontrado"}
        
    @classmethod
    def modificar_arbitro(cls, arbitro_id: int, apyn: str, idPartido: int):
        session = sessionmaker(bind=engine)()
        arbitro = session.query(cls).filter(cls.id == arbitro_id).first()  # Busca el árbitro por ID
        if arbitro:
            arbitro.apyn = apyn
            arbitro.idPartido = idPartido
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Árbitro modificado exitosamente"}
        else:
            session.close()
            return {"message": "Árbitro no encontrado"}