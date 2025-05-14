import json
import csv
from proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar_proceso(self, proceso: Proceso):
        if proceso.pid in self.procesos:
            raise ValueError(f"Ya existe un proceso con el PID {proceso.pid}.")
        self.procesos[proceso.pid] = proceso

    def listar_procesos(self):
        return list(self.procesos.values())

    def eliminar_proceso(self, pid: str):
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con el PID {pid}.")
        del self.procesos[pid]

    def obtener_proceso(self, pid: str) -> Proceso:
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con el PID {pid}.")
        return self.procesos[pid]

    def guardar_json(self, filepath: str):
        with open(filepath, 'w') as file:
            json.dump([proceso.__dict__ for proceso in self.procesos.values()], file)

    def cargar_json(self, filepath: str):
        with open(filepath, 'r') as file:
            data = json.load(file)
            self.procesos = {}
            for proceso_data in data:
                proceso = Proceso(
                    pid=proceso_data['pid'],
                    duracion=proceso_data['duracion'],
                    prioridad=proceso_data['prioridad']
                )
                proceso.tiempo_restante = proceso_data['tiempo_restante']
                proceso.tiempo_llegada = proceso_data['tiempo_llegada']
                proceso.tiempo_inicio = proceso_data['tiempo_inicio']
                proceso.tiempo_fin = proceso_data['tiempo_fin']
                self.agregar_proceso(proceso)

    def guardar_csv(self, filepath: str):
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad', 'tiempo_restante', 'tiempo_llegada', 'tiempo_inicio', 'tiempo_fin'])
            for proceso in self.procesos.values():
                writer.writerow([
                    proceso.pid, proceso.duracion, proceso.prioridad,
                    proceso.tiempo_restante, proceso.tiempo_llegada,
                    proceso.tiempo_inicio, proceso.tiempo_fin
                ])

    def cargar_csv(self, filepath: str):
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            self.procesos = {}
            for row in reader:
                proceso = Proceso(
                    pid=row['pid'],
                    duracion=int(row['duracion']),
                    prioridad=int(row['prioridad'])
                )
                proceso.tiempo_restante = int(row['tiempo_restante'])
                proceso.tiempo_llegada = int(row['tiempo_llegada'])
                proceso.tiempo_inicio = None if row['tiempo_inicio'] == 'None' else int(row['tiempo_inicio'])
                proceso.tiempo_fin = None if row['tiempo_fin'] == 'None' else int(row['tiempo_fin'])
                self.agregar_proceso(proceso)
