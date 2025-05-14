from scheduler_base import Scheduler, GanttEntry
from typing import List
from proceso import Proceso

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        procesos.sort(key=lambda p: p.tiempo_llegada)  # Ordenar por tiempo de llegada
        tiempo_actual = 0
        gantt = []

        for proceso in procesos:
            tiempo_inicio = max(tiempo_actual, proceso.tiempo_llegada)
            tiempo_fin = tiempo_inicio + proceso.duracion
            gantt.append((proceso.pid, tiempo_inicio, tiempo_fin))
            proceso.tiempo_inicio = tiempo_inicio
            proceso.tiempo_fin = tiempo_fin
            tiempo_actual = tiempo_fin

        return gantt
