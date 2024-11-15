from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from fastapi.staticfiles import StaticFiles #Importante para poder montar los Static y simplificar
#from endpoints import router #Importante para poder llamar a los endpoints desde el main

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Montar la carpeta de archivos estáticos
#app.mount("/static", StaticFiles(directory="static"), name="static")

#app.include_router(router) #Registra los endpoints en la aplicacion

# CORS (permite la interacción con los navegadores)
origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "¡FastAPI está funcionando correctamente!"}
