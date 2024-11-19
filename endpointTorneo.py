from fastapi import APIRouter, HTTPException
from typing import List
from Torneo import Torneo
from models import TorneoModel

router = APIRouter()

#Endpoint POST para agregar un Torneo
@router.post("/torneos/nuevo/", tags=["Torneo"], summary="Crear un nuevo Torneo", description="Este endpoint crea un nuevo Torneo en la base de datos.")
def agregar_torneo(torneo: TorneoModel):
    Torneo.agregar_torneo(torneo)
    return {"message": "Torneo creado exitosamente"}