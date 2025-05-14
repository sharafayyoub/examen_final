import argparse
from repositorio_procesos import RepositorioProcesos
from scheduler import FCFSScheduler, RoundRobinScheduler
from metrics import calcular_metricas
from proceso import Proceso

def main():
    parser = argparse.ArgumentParser(description="Simulador de planificación de procesos.")
    parser.add_argument("--algoritmo", choices=["fcfs", "rr"], required=True, help="Algoritmo de planificación (fcfs o rr).")
    parser.add_argument("--quantum", type=int, help="Quantum para Round-Robin (requerido si se usa rr).")
    parser.add_argument("--archivo", required=True, help="Archivo JSON o CSV con los procesos.")
    args = parser.parse_args()

    repositorio = RepositorioProcesos()
    if args.archivo.endswith(".json"):
        repositorio.cargar_json(args.archivo)
    elif args.archivo.endswith(".csv"):
        repositorio.cargar_csv(args.archivo)
    else:
        raise ValueError("El archivo debe ser JSON o CSV.")

    procesos = repositorio.listar_procesos()

    if args.algoritmo == "fcfs":
        scheduler = FCFSScheduler()
    elif args.algoritmo == "rr":
        if not args.quantum:
            raise ValueError("Debe especificar un quantum para Round-Robin.")
        scheduler = RoundRobinScheduler(args.quantum)

    gantt = scheduler.planificar(procesos)
    metricas = calcular_metricas(procesos, gantt)

    print("Diagrama de Gantt:")
    for entrada in gantt:
        print(entrada)

    print("\nMétricas:")
    for clave, valor in metricas.items():
        print(f"{clave}: {valor:.2f}")

if __name__ == "__main__":
    main()
