from fastapi import APIRouter, HTTPException
from typing import List
from Partido import Partido  # Importar la clase Partido
from models import PartidoModel  # Importar el modelo de datos para Partido

router = APIRouter()

# Endpoint POST para agregar un Partido
@router.post("/partidos/nuevo/", tags=["Partido"], summary="Crear un nuevo Partido", description="Este endpoint crea un nuevo Partido en la base de datos.")
def agregar_partido(partido: PartidoModel):
    nuevo_partido = Partido.agregar_partido(
        partido.idEquipoLocal,
        partido.idEquipoVisitante,
        partido.idCancha,
        partido.golLocal,  # Asegúrate de incluir golLocal
        partido.golVisitante,  # Asegúrate de incluir golVisitante
        partido.fechaPartido
    )
    
    return {"message": "Partido creado exitosamente", "partido_id": nuevo_partido.id}

# Endpoint GET para obtener todos los Partidos
@router.get("/partidos/", tags=["Partido"], summary="Obtener todos los Partidos", description="Este endpoint devuelve todos los Partidos en la base de datos.")
def obtener_todos_los_partidos():
    partidos = Partido.obtener_todos_los_partidos()
    return partidos

# Endpoint DELETE para eliminar un Partido
@router.delete("/partidos/{partido_id}", tags=["Partido"], summary="Eliminar un Partido", description="Este endpoint elimina un Partido de la base de datos.")
def eliminar_partido(partido_id: int):
    resultado = Partido.eliminar_partido(partido_id)
    return {"message": resultado["message"]}

# Endpoint PUT para modificar un Partido
@router.put("/partidos/{partido_id}", tags=["Partido"], summary="Modificar un Partido", description="Este endpoint modifica un Partido existente en la base de datos.")
def modificar_partido(partido_id: int, partido: PartidoModel):
    resultado = Partido.modificar_partido(partido_id, partido.idEquipoLocal, partido.idEquipoVisitante, partido.golLocal, partido.golVisitante, partido.fechaPartido)
    if resultado["message"] == "Partido modificado exitosamente":
        return {"message": "Partido modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])