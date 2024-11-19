from fastapi import APIRouter, HTTPException
from typing import List
from Jugador import Jugador  # Importar la clase Jugador
from models import JugadorModel  # Importar el modelo de datos para Jugador

router = APIRouter()

# Endpoint POST para agregar un Jugador
@router.post("/jugadores/nuevo/", tags=["Jugador"], summary="Crear un nuevo Jugador", description="Este endpoint crea un nuevo Jugador en la base de datos.")
def agregar_jugador(jugador: JugadorModel):
    # Llamar al método agregar_jugador directamente usando los atributos del objeto JugadorModel
    nuevo_jugador = Jugador.agregar_jugador(jugador.apyn, jugador.fechaNacimiento, jugador.posicion, jugador.numeroDeCamiseta, jugador.equipo_id)
    
    return {"message": "Jugador creado exitosamente", "jugador_id": nuevo_jugador.id}

# Endpoint GET para obtener todos los Jugadores
@router.get("/jugadores/", tags=["Jugador"], summary="Obtener todos los Jugadores", description="Este endpoint devuelve todos los Jugadores en la base de datos.")
def obtener_todos_los_jugadores():
    jugadores = Jugador.obtener_todos_los_jugadores()
    return jugadores

# Endpoint DELETE para eliminar un Jugador
@router.delete("/jugadores/{jugador_id}", tags=["Jugador"], summary="Eliminar un Jugador", description="Este endpoint elimina un Jugador de la base de datos.")
def eliminar_jugador(jugador_id: int):
    resultado = Jugador.eliminar_jugador(jugador_id)
    return {"message": resultado["message"]}

# Endpoint PUT para modificar un Jugador
@router.put("/jugadores/{jugador_id}", tags=["Jugador"], summary="Modificar un Jugador", description="Este endpoint modifica un Jugador existente en la base de datos.")
def modificar_jugador(jugador_id: int, jugador: JugadorModel):
    resultado = Jugador.modificar_jugador(jugador_id, jugador.apyn, jugador.fechaNacimiento, jugador.posicion, jugador.numeroDeCamiseta, jugador.equipo_id)
    if resultado["message"] == "Jugador modificado exitosamente":
        return {"message": "Jugador modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])