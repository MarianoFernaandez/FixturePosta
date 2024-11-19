from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from database import Base, engine

class Fecha(Base):
    __tablename__ = 'fechas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idFixture = Column(Integer, ForeignKey('fixture.id'), nullable=False)  # Clave foránea a la tabla Fixture
    fechaPartido = Column(Date, nullable=False)
    
    # Relación con los Partidos
    partidos = relationship("Partido", backref="fecha")

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
    def obtener_todas_las_fechas(cls):
        session = sessionmaker(bind=engine)()
        fechas = session.query(cls).all()  # Consulta para obtener todas las fechas
        session.close()
        return fechas
    
    @classmethod
    def modificar_fecha(cls, fecha_id: int, idFixture: int, fechaPartido: Date):
        session = sessionmaker(bind=engine)()
        fecha = session.query(cls).filter(cls.id == fecha_id).first()  # Busca la fecha por ID
        if fecha:
            fecha.idFixture = idFixture
            fecha.fechaPartido = fechaPartido
            session.commit()  # Confirma los cambios
            session.close()
            return {"message": "Fecha modificada exitosamente"}
        else:
            session.close()
            return {"message": "Fecha no encontrada"}
        
from Fixture import Fixture

fixture = relationship("Fixture", backref="fechas")  # Un fixture puede tener muchas fechas