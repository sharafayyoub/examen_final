from typing import List, Dict
from proceso import Proceso
from scheduler import GanttEntry

def calcular_metricas(procesos: List[Proceso], gantt: List[GanttEntry]) -> Dict[str, float]:
    tiempos_respuesta = []
    tiempos_retorno = []
    tiempos_espera = []

    for proceso in procesos:
        tiempo_inicio = proceso.tiempo_inicio
        tiempo_llegada = proceso.tiempo_llegada
        tiempo_fin = proceso.tiempo_fin
        duracion = proceso.duracion

        tiempo_respuesta = tiempo_inicio - tiempo_llegada
        tiempo_retorno = tiempo_fin - tiempo_llegada
        tiempo_espera = tiempo_retorno - duracion

        tiempos_respuesta.append(tiempo_respuesta)
        tiempos_retorno.append(tiempo_retorno)
        tiempos_espera.append(tiempo_espera)

    return {
        "tiempo_respuesta_promedio": sum(tiempos_respuesta) / len(tiempos_respuesta),
        "tiempo_retorno_promedio": sum(tiempos_retorno) / len(tiempos_retorno),
        "tiempo_espera_promedio": sum(tiempos_espera) / len(tiempos_espera),
    }
