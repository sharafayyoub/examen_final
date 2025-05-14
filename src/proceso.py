class Proceso:
    procesos_existentes = set()  # Para validar que no haya PIDs duplicados

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid or pid in Proceso.procesos_existentes:
            raise ValueError("El PID debe ser único y no vacío.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        if not isinstance(prioridad, int):
            raise ValueError("La prioridad debe ser un entero.")

        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0  # Asumido como 0 para simplificación
        self.tiempo_inicio = None
        self.tiempo_fin = None

        Proceso.procesos_existentes.add(pid)

    def __repr__(self):
        return (f"Proceso(pid={self.pid}, duracion={self.duracion}, "
                f"prioridad={self.prioridad}, tiempo_restante={self.tiempo_restante}, "
                f"tiempo_llegada={self.tiempo_llegada}, tiempo_inicio={self.tiempo_inicio}, "
                f"tiempo_fin={self.tiempo_fin})")
