from fastapi import APIRouter, HTTPException
from typing import List
from Cancha import Cancha  # Importar la clase Cancha
from models import CanchaModel  # Importar el modelo de datos para Cancha

router = APIRouter()

# Endpoint POST para agregar una Cancha
@router.post("/canchas/nueva/", tags=["Cancha"], summary="Crear una nueva Cancha", description="Este endpoint crea una nueva Cancha en la base de datos.")
def agregar_cancha(cancha: CanchaModel):
    nueva_cancha = Cancha.agregar_cancha(
        cancha.nombre,
        cancha.ubicacion,
        cancha.tamaño,
        cancha.tipoSuperficie
    )
    
    return {"message": "Cancha creada exitosamente", "cancha_id": nueva_cancha.id}

# Endpoint GET para obtener todas las Canchas
@router.get("/canchas/", tags=["Cancha"], summary="Obtener todas las Canchas", description="Este endpoint devuelve todas las Canchas en la base de datos.")
def obtener_todas_las_canchas():
    canchas = Cancha.obtener_todas_las_canchas()
    return canchas

# Endpoint DELETE para eliminar una Cancha
@router.delete("/canchas/{cancha_id}", tags=["Cancha"], summary="Eliminar una Cancha", description="Este endpoint elimina una Cancha de la base de datos.")
def eliminar_cancha(cancha_id: int):
    resultado = Cancha.eliminar_cancha(cancha_id)
    return {"message": resultado["message"]}

# Endpoint PUT para modificar una Cancha
@router.put("/canchas/{cancha_id}", tags=["Cancha"], summary="Modificar una Cancha", description="Este endpoint modifica una Cancha existente en la base de datos.")
def modificar_cancha(cancha_id: int, cancha: CanchaModel):
    resultado = Cancha.modificar_cancha(cancha_id, cancha.nombre, cancha.ubicacion, cancha.tamaño, cancha.tipoSuperficie)
    if resultado["message"] == "Cancha modificada exitosamente":
        return {"message": "Cancha modificada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])