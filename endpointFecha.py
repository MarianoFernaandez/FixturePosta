from fastapi import APIRouter, HTTPException
from typing import List
from Fecha import Fecha  # Importar la clase Fecha
from models import FechaModel  # Importar el modelo de datos para Fecha

router = APIRouter()

# Endpoint POST para agregar una Fecha
@router.post("/fechas/nueva/", tags=["Fecha"], summary="Crear una nueva Fecha", description="Este endpoint crea una nueva Fecha en la base de datos. TENER EN CUENTA EN PONER EL ID DE FIXTURE")
def agregar_fecha(fecha: FechaModel):
    nueva_fecha = Fecha.agregar_fecha(
        fecha.idFixture,
        fecha.fechaPartido
    )
    
    return {"message": "Fecha creada exitosamente", "fecha_id": nueva_fecha.id}

# Endpoint GET para obtener todas las Fechas
@router.get("/fechas/", response_model=List[FechaModel], tags=["Fecha"], summary="Obtener todas las Fechas", description="Este endpoint devuelve todas las Fechas en la base de datos.")
def obtener_todas_las_fechas():
    fechas = Fecha.obtener_todas_las_fechas()
    return fechas

#NO SE PUEDE POR UNA RELACION

# Endpoint PUT para modificar una Fecha
@router.put("/fechas/{fecha_id}", tags=["Fecha"], summary="Modificar una Fecha", description="Este endpoint modifica una Fecha existente en la base de datos.")
def modificar_fecha(fecha_id: int, fecha: FechaModel):
    resultado = Fecha.modificar_fecha(fecha_id, fecha.idFixture, fecha.fechaPartido)
    if resultado["message"] == "Fecha modificada exitosamente":
        return {"message": "Fecha modificada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])