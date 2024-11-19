from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from endpointTorneo import router as router_torneo
from endpointEquipo import router as router_equipo

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Montar la carpeta de archivos estáticos
#app.mount("/static", StaticFiles(directory="static"), name="static")

#app.include_router(router) #Registra los endpoints en la aplicacion

# CORS (permite la interacción con los navegadores)
origins = [
    "http://localhost",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Agrega los Endpoint

app.include_router(router_torneo)
app.include_router(router_equipo)
