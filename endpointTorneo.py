from fastapi import APIRouter, HTTPException
from typing import List
from Torneo import Torneo
from models import TorneoModel

router = APIRouter()

# Endpoint POST para agregar un Torneo
@router.post("/torneos/nuevo/", tags=["Torneo"], summary="Crear un nuevo Torneo", description="Este endpoint crea un nuevo Torneo en la base de datos.")
def agregar_torneo(torneo: TorneoModel):
    # Llamar al método agregar_torneo directamente usando los atributos del objeto TorneoModel
    Torneo.agregar_torneo(torneo.nombre, torneo.fechaInicio, torneo.fechaFin, torneo.cantidadEquipos)
    
    return {"message": "Torneo creado exitosamente"}

# Endpoint GET para obtener todos los Torneos
@router.get("/torneos/", tags=["Torneo"], summary="Obtener todos los Torneos", description="Este endpoint devuelve todos los Torneos en la base de datos.")
def obtener_todos_los_torneos():
    torneos = Torneo.obtener_todos_los_torneos()
    return torneos

# Endpoint DELETE para eliminar un Torneo
@router.delete("/torneos/{torneo_id}", tags=["Torneo"], summary="Eliminar un Torneo", description="Este endpoint elimina un Torneo de la base de datos.")
def eliminar_torneo(torneo_id: int):
    resultado = Torneo.eliminar_torneo(torneo_id)
    return 

# Endpoint PUT para modificar un Torneo
@router.put("/torneos/{torneo_id}", tags=["Torneo"], summary="Modificar un Torneo", description="Este endpoint modifica un Torneo existente en la base de datos.")
def modificar_torneo(torneo_id: int, torneo: TorneoModel):
    resultado = Torneo.modificar_torneo(torneo_id, torneo.nombre, torneo.fechaInicio, torneo.fechaFin, torneo.cantidadEquipos)
    if resultado["message"] == "Torneo modificado exitosamente":
        return {"message": "Torneo modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])