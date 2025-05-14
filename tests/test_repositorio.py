import pytest
from proceso import Proceso
from repositorio_procesos import RepositorioProcesos

def test_agregar_proceso():
    repositorio = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=5, prioridad=1)
    repositorio.agregar_proceso(proceso)
    assert repositorio.obtener_proceso("P1") == proceso

def test_eliminar_proceso():
    repositorio = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=5, prioridad=1)
    repositorio.agregar_proceso(proceso)
    repositorio.eliminar_proceso("P1")
    with pytest.raises(ValueError):
        repositorio.obtener_proceso("P1")

def test_listar_procesos():
    repositorio = RepositorioProcesos()
    proceso1 = Proceso(pid="P1", duracion=5, prioridad=1)
    proceso2 = Proceso(pid="P2", duracion=3, prioridad=2)
    repositorio.agregar_proceso(proceso1)
    repositorio.agregar_proceso(proceso2)
    assert repositorio.listar_procesos() == [proceso1, proceso2]

def test_guardar_y_cargar_json(tmp_path):
    repositorio = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=5, prioridad=1)
    repositorio.agregar_proceso(proceso)
    filepath = tmp_path / "procesos.json"
    repositorio.guardar_json(filepath)
    repositorio.cargar_json(filepath)
    assert repositorio.obtener_proceso("P1").duracion == 5

def test_guardar_y_cargar_csv(tmp_path):
    repositorio = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=5, prioridad=1)
    repositorio.agregar_proceso(proceso)
    filepath = tmp_path / "procesos.csv"
    repositorio.guardar_csv(filepath)
    repositorio.cargar_csv(filepath)
    assert repositorio.obtener_proceso("P1").duracion == 5
