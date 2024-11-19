from fastapi import APIRouter, HTTPException
from typing import List
from models import JugadorRolModel  # Asegúrate de que este modelo esté definido correctamente
from jugadorRol import JugadorRol  # Importa la clase JugadorRol

router = APIRouter()

@router.post("/jugadores/roles/", tags=["JugadorRol"], summary="Crear una asociación entre Jugador y Rol", description="Este endpoint permite crear una nueva asociación entre un jugador y un rol.")
def crear_asociacion(jugador_rol: JugadorRolModel):
    # Lógica para agregar la asociación
    resultado = JugadorRol.agregar_asociacion(jugador_rol.jugador_id, jugador_rol.rol_id)
    return resultado  # Retorna el resultado del método agregar_asociacion

@router.get("/jugadores/roles/", response_model=List[JugadorRolModel], tags=["JugadorRol"], summary="Obtener todas las asociaciones de Jugadores y Roles", description="Este endpoint devuelve todas las asociaciones existentes entre Jugadores y Roles.")
def mostrar_asociaciones():
    # Lógica para obtener todas las asociaciones
    asociaciones = JugadorRol.obtener_todas_asociaciones()  # Asumiendo que tienes este método en la clase JugadorRol
    return asociaciones  # Retorna la lista de asociaciones

@router.delete("/jugadores/roles/", tags=["JugadorRol"], summary="Eliminar una asociación entre Jugador y Rol", description="Este endpoint permite eliminar una asociación existente entre un jugador y un rol.")
def eliminar_asociacion(jugador_id: int, rol_id: int):
    # Lógica para eliminar la asociación
    resultado = JugadorRol.eliminar_asociacion(jugador_id, rol_id)
    return resultado  # Retorna el resultado del método eliminar_asociacion

