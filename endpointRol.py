from fastapi import APIRouter, HTTPException
from typing import List
from Rol import Rol  # Importar la clase Rol
from models import RolModel  # Importar el modelo de datos para Rol

router = APIRouter()

# Endpoint POST para agregar un Rol
@router.post("/roles/nuevo/", tags=["Rol"], summary="Crear un nuevo Rol", description="Este endpoint crea un nuevo Rol en la base de datos.")
def agregar_rol(rol: RolModel):
    nuevo_rol = Rol.agregar_rol(rol.rol)  # Usar el atributo 'rol' del modelo
    return {"message": "Rol creado exitosamente", "rol_id": nuevo_rol.id}

# Endpoint GET para obtener todos los Roles
@router.get("/roles/", response_model=List[RolModel], tags=["Rol"], summary="Obtener todos los Roles", description="Este endpoint devuelve todos los Roles en la base de datos.")
def obtener_todos_los_roles():
    roles = Rol.obtener_todos_los_roles()
    return roles

# Endpoint PUT para modificar un Rol
@router.put("/roles/{rol_id}", tags=["Rol"], summary="Modificar un Rol", description="Este endpoint modifica un Rol existente en la base de datos.")
def modificar_rol(rol_id: int, rol: RolModel):
    resultado = Rol.modificar_rol(rol_id, rol.rol)  # Usar el atributo 'rol' del modelo
    return {"message": resultado["message"]}