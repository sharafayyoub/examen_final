from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso

GanttEntry = Tuple[str, int, int]  # (pid, tiempo_inicio, tiempo_fin)

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """Planifica los procesos y devuelve una lista de entradas de Gantt."""
        pass

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

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo.")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        cola = procesos[:]
        tiempo_actual = 0
        gantt = []

        while cola:
            proceso = cola.pop(0)
            if proceso.tiempo_restante > 0:
                tiempo_inicio = max(tiempo_actual, proceso.tiempo_llegada)
                tiempo_ejecucion = min(self.quantum, proceso.tiempo_restante)
                tiempo_fin = tiempo_inicio + tiempo_ejecucion
                gantt.append((proceso.pid, tiempo_inicio, tiempo_fin))
                proceso.tiempo_restante -= tiempo_ejecucion
                tiempo_actual = tiempo_fin

                if proceso.tiempo_restante > 0:
                    cola.append(proceso)  # Reinsertar si no ha terminado
                else:
                    proceso.tiempo_fin = tiempo_fin

        return gantt
