from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload

# Configuración de conexión a la base de datos
username = 'root'
password = '454848'
host = '127.0.0.1'
port = '3306'  # Puerto de conexión / compu de Colegio: 3307 / Compu Casa: 3306
database = 'fixture' # En Colegio fixture / En casa fixture

# String de conexión
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Crear el motor para conectarse a la base de datos
engine = create_engine(connection_string)

# Crear una fábrica de sesiones para manejar conexiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarativa base para la creación de los modelos
Base = declarative_base()

# Dependency para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Probar la conexión
try:
    with engine.connect() as connection:
        print("¡Conexión exitosa!")
except Exception as e:
    print(f"Error al conectar: {e}")
