from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy import sessionmaker
from database import Base, engine, relationship
from models import FechaModel  # Asegúrate de que el modelo Pydantic esté importado

class Fecha(Base):
    __tablename__ = 'fechas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idFixture = Column(Integer, ForeignKey('fixture.id'))  # Relación con Fixture
    fechaPartido = Column(Date)  # Fecha del partido

    # Relación con Fixture
    fixture = relationship("Fixture", back_populates="fechas")
    
    # Relación con Partidos
    partidos = relationship("Partido", back_populates="fecha")

    # CRUD Fecha
    @classmethod
    def agregar_fecha(cls, idFixture: int, fechaPartido: Date):
        nueva_fecha = cls(
            idFixture=idFixture,
            fechaPartido=fechaPartido
        )
        session = sessionmaker(bind=engine)()
        session.add(nueva_fecha)
        session.commit()
        session.refresh(nueva_fecha)
        session.close()
        return nueva_fecha

    @classmethod
    def mostrar_fechas(cls):
        session = sessionmaker(bind=engine)()
        fechas = session.query(cls).all()
        session.close()
        return fechas

    @classmethod
    def buscar_fecha(cls, fecha_id: int):
        session = sessionmaker(bind=engine)()
        fecha = session.query(cls).filter_by(id=fecha_id).first()
        session.close()
        return fecha

    @classmethod
    def eliminar_fecha(cls, fecha_id: int):
        session = sessionmaker(bind=engine)()
        fecha = session.query(cls).filter_by(id=fecha_id).first()
        if fecha:
            session.delete(fecha)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def modificar_fecha(cls, fecha_id: int, fecha_in: FechaModel):
        session = sessionmaker(bind=engine)()
        fecha_existente = session.query(cls).filter(cls.id == fecha_id).one_or_none()
        if not fecha_existente:
            session.close()
            raise Exception(f"Fecha con id {fecha_id} no encontrada")

        fecha_existente.idFixture = fecha_in.idFixture
        fecha_existente.fechaPartido = fecha_in.fechaPartido

        session.commit()
        session.refresh(fecha_existente)
        session.close()

        return FechaModel(
            id=fecha_existente.id,
            idFixture=fecha_existente.idFixture,
            fechaPartido=fecha_existente.fechaPartido
        )