from fastapi import APIRouter, HTTPException
from typing import List
from Arbitro import Arbitro  # Importar la clase Arbitro
from models import ArbitroModel  # Importar el modelo de datos para Arbitro

router = APIRouter()

# Endpoint POST para agregar un Árbitro
@router.post("/arbitros/nuevo/", tags=["Árbitro"], summary="Crear un nuevo Árbitro", description="Este endpoint crea un nuevo Árbitro en la base de datos.")
def agregar_arbitro(arbitro: ArbitroModel):
    nuevo_arbitro = Arbitro.agregar_arbitro(
        arbitro.apyn,
        arbitro.idPartido
    )
    
    return {"message": "Árbitro creado exitosamente", "arbitro_id": nuevo_arbitro.id}

# Endpoint GET para obtener todos los Árbitros
@router.get("/arbitros/", response_model=List[ArbitroModel], tags=["Árbitro"], summary="Obtener todos los Árbitros", description="Este endpoint devuelve todos los Árbitros en la base de datos.")
def obtener_todos_los_arbitros():
    arbitros = Arbitro.obtener_todos_los_arbitros()
    return arbitros

# Endpoint DELETE para eliminar un Árbitro
@router.delete("/arbitros/{arbitro_id}", tags=["Árbitro"], summary="Eliminar un Árbitro", description="Este endpoint elimina un Árbitro de la base de datos.")
def eliminar_arbitro(arbitro_id: int):
    resultado = Arbitro.eliminar_arbitro(arbitro_id)
    return {"message": resultado["message"]}

# Endpoint PUT para modificar un Árbitro
@router.put("/arbitros/{arbitro_id}", tags=["Árbitro"], summary="Modificar un Árbitro", description="Este endpoint modifica un Árbitro existente en la base de datos.")
def modificar_arbitro(arbitro_id: int, arbitro: ArbitroModel):
    resultado = Arbitro.modificar_arbitro(arbitro_id, arbitro.apyn, arbitro.idPartido)
    if resultado["message"] == "Árbitro modificado exitosamente":
        return {"message": "Árbitro modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])