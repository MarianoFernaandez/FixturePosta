from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, sessionmaker, engine

class Fixture(Base):
    __tablename__ = 'fixture'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idTorneo = Column(Integer, ForeignKey('torneos.id_torneo'))  # Clave foránea hacia Torneo

    # Relación con Torneo
    torneo = relationship("Torneo", back_populates="fixtures")  # Un fixture está asociado a un único torneo

    # Relación con Fechas
    fechas = relationship("Fecha", back_populates="fixture")  # Un fixture puede tener muchas fechas

    # Métodos CRUD
    @classmethod
    def agregar_fixture(cls, idTorneo: int):
        nuevo_fixture = cls(idTorneo=idTorneo)
        session = sessionmaker(bind=engine)()
        session.add(nuevo_fixture)
        session.commit()
        session.refresh(nuevo_fixture)
        session.close()
        return nuevo_fixture

    @classmethod
    def mostrar_fixtures(cls):
        session = sessionmaker(bind=engine)()
        fixtures = session.query(cls).all()
        session.close()
        return fixtures

    @classmethod
    def eliminar_fixture(cls, fixture_id: int):
        session = sessionmaker(bind=engine)()
        fixture = session.query(cls).filter_by(id=fixture_id).first()
        if fixture:
            session.delete(fixture)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def modificar_fixture(cls, fixture_id: int, idTorneo: int):
        session = sessionmaker(bind=engine)()
        fixture_existente = session.query(cls).filter(cls.id == fixture_id).one_or_none()
        if not fixture_existente:
            session.close()
            raise Exception(f"Fixture con id {fixture_id} no encontrado")

        fixture_existente.idTorneo = idTorneo

        session.commit()
        session.refresh(fixture_existente)
        session.close()

        return fixture_existente