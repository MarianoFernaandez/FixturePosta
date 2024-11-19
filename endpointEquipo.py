from fastapi import APIRouter, HTTPException
from typing import List
from Equipo import Equipo  # Importar la clase Equipo
from models import EquipoModel  # Importar el modelo de datos para Equipo

router = APIRouter()

# Endpoint POST para agregar un Equipo
@router.post("/equipos/nuevo/", tags=["Equipo"], summary="Crear un nuevo Equipo", description="Este endpoint crea un nuevo Equipo en la base de datos.")
def agregar_equipo(equipo: EquipoModel):
    # Llamar al método agregar_equipo directamente usando los atributos del objeto EquipoModel
    nuevo_equipo = Equipo.agregar_equipo(equipo.nombre, equipo.escudo, equipo.ciudad, equipo.fechaFundacion)
    
    return {"message": "Equipo creado exitosamente", "equipo_id": nuevo_equipo.id}

# Endpoint GET para obtener todos los Equipos
@router.get("/equipos/", tags=["Equipo"], summary="Obtener todos los Equipos", description="Este endpoint devuelve todos los Equipos en la base de datos.")
def obtener_todos_los_equipos():
    equipos = Equipo.obtener_todos_los_equipos()
    return equipos

# Endpoint DELETE para eliminar un Equipo
@router.delete("/equipos/{equipo_id}", tags=["Equipo"], summary="Eliminar un Equipo", description="Este endpoint elimina un Equipo de la base de datos.")
def eliminar_equipo(equipo_id: int):
    resultado = Equipo.eliminar_equipo(equipo_id)
    return {"message": resultado["message"]}

# Endpoint PUT para modificar un Equipo
@router.put("/equipos/{equipo_id}", tags=["Equipo"], summary="Modificar un Equipo", description="Este endpoint modifica un Equipo existente en la base de datos.")
def modificar_equipo(equipo_id: int, equipo: EquipoModel):
    resultado = Equipo.modificar_equipo(equipo_id, equipo.nombre, equipo.escudo, equipo.ciudad, equipo.fechaFundacion)
    if resultado["message"] == "Equipo modificado exitosamente":
        return {"message": "Equipo modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])