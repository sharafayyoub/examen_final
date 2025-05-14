import pytest
from proceso import Proceso
from metrics import calcular_metricas

def test_calcular_metricas():
    procesos = [
        Proceso(pid="P1", duracion=5, prioridad=1),
        Proceso(pid="P2", duracion=3, prioridad=2),
    ]
    procesos[0].tiempo_llegada = 0
    procesos[0].tiempo_inicio = 0
    procesos[0].tiempo_fin = 5

    procesos[1].tiempo_llegada = 1
    procesos[1].tiempo_inicio = 5
    procesos[1].tiempo_fin = 8

    gantt = [("P1", 0, 5), ("P2", 5, 8)]
    metricas = calcular_metricas(procesos, gantt)

    assert metricas["tiempo_respuesta_promedio"] == 2.0
    assert metricas["tiempo_retorno_promedio"] == 6.5
    assert metricas["tiempo_espera_promedio"] == 3.5
