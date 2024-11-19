from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Fixture(Base):
    __tablename__ = 'fixture'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idTorneo = Column(Integer, ForeignKey('torneos.id'), nullable=False)  # Clave foránea a la tabla Torneos
    idFecha = Column(Integer, ForeignKey('fechas.id'), nullable=False)
    # Relación con Torneo
    torneo = relationship("Torneo", backref="fixtures")  # Un torneo puede tener múltiples fixtures

    # CRUD Fixture
    @classmethod
    def agregar_fixture(cls, idTorneo: int, idFecha: int):
        nuevo_fixture = cls(idTorneo=idTorneo, idFecha=idFecha)  # Asegúrate de incluir idFecha
        session = sessionmaker(bind=engine)()
        session.add(nuevo_fixture)
        session.commit()
        session.refresh(nuevo_fixture)
        session.close()
        return nuevo_fixture

    @classmethod
    def obtener_todos_los_fixtures(cls):
        session = sessionmaker(bind=engine)()
        fixtures = session.query(cls).all()  # Consulta para obtener todos los fixtures
        session.close()
        return fixtures

    @classmethod
    def eliminar_fixture(cls, fixture_id: int):
        session = sessionmaker(bind=engine)()
        fixture = session.query(cls).filter(cls.id == fixture_id).first()  # Busca el fixture por ID
        if fixture:
            session.delete(fixture)  # Elimina el fixture
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Fixture eliminado exitosamente"}
        else:
            session.close()
            return {"message": "Fixture no encontrado"}

    @classmethod
    def modificar_fixture(cls, fixture_id: int, idTorneo: int, idFecha: int):
        session = sessionmaker(bind=engine)()
        fixture = session.query(cls).filter(cls.id == fixture_id).first()  # Busca el fixture por ID
        if fixture:
            fixture.idTorneo = idTorneo
            fixture.idFecha = idFecha
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Fixture modificado exitosamente"}
        else:
            session.close()
            return {"message": "Fixture no encontrado"}
        
from Fecha import Fecha

# Relación con Fechas
fechas = relationship("Fecha", backref="fixture")