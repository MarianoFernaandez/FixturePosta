from fastapi import APIRouter, HTTPException
from typing import List
from Fixture import Fixture  # Importar la clase Fixture
from models import FixtureModel  # Importar el modelo de datos para Fixture

router = APIRouter()

# Endpoint POST para agregar un Fixture
@router.post("/fixtures/nuevo/", tags=["Fixture"], summary="Crear un nuevo Fixture", description="Este endpoint crea un nuevo Fixture en la base de datos.")
def agregar_fixture(fixture: FixtureModel):
    nuevo_fixture = Fixture.agregar_fixture(
        fixture.idTorneo,
        fixture.idPartido
    )
    return {"message": "Fixture creado exitosamente", "fixture_id": nuevo_fixture.id}

# Endpoint GET para obtener todos los Fixtures
@router.get("/fixtures/", tags=["Fixture"], summary="Obtener todos los Fixtures", description="Este endpoint devuelve todos los Fixtures en la base de datos.")
def obtener_todos_los_fixtures():
    fixtures = Fixture.obtener_todos_los_fixtures()
    return fixtures

# Endpoint DELETE para eliminar un Fixture
@router.delete("/fixtures/{fixture_id}", tags=["Fixture"], summary="Eliminar un Fixture", description="Este endpoint elimina un Fixture de la base de datos.")
def eliminar_fixture(fixture_id: int):
    resultado = Fixture.eliminar_fixture(fixture_id)
    return {"message": resultado["message"]}

# Endpoint PUT para modificar un Fixture
@router.put("/fixtures/{fixture_id}", tags=["Fixture"], summary="Modificar un Fixture", description="Este endpoint modifica un Fixture existente en la base de datos.")
def modificar_fixture(fixture_id: int, fixture: FixtureModel):
    resultado = Fixture.modificar_fixture(fixture_id, fixture.idTorneo, fixture.idPartido)
    if resultado["message"] == "Fixture modificado exitosamente":
        return {"message": "Fixture modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=resultado["message"])
