import random

class SistemaColas:

    def __init__(self, tasaLlegada, tasaServicio, capacidadSistema, tiempoMax=10000.0, semilla=None):
        if semilla is not None:
            random.seed(semilla)
        self.tasaLlegada=tasaLlegada   #λ
        self.tasaServicio=tasaServicio #μ
        self.capacidadSistema=capacidadSistema #K (máx clientes en sistema, cola+servidor)
        self.tiempoMax=tiempoMax

    def run(self):
        #Estado inicial
        tiempo=0.0
        proximaLlegada=random.expovariate(self.tasaLlegada)
        finServicio=None
        cola=[]

        #Métricas
        clientesRechazados=clientesAtendidos=totalLlegadas=0
        areaSistema=areaCola=ultimoEvento=0.0
        sumaTiempoSistema=sumaTiempoCola=0.0
        clienteActual=None

        while tiempo<self.tiempoMax:
            tiempoSiguiente=min(proximaLlegada, finServicio) if finServicio else proximaLlegada
            if tiempoSiguiente>self.tiempoMax:
                dt=self.tiempoMax-ultimoEvento
                N=len(cola)+(1 if finServicio else 0)  #clientes en sistema
                Q=len(cola)                              #clientes en cola
                areaSistema+=N * dt
                areaCola+=Q * dt
                break

            dt=tiempoSiguiente - ultimoEvento
            N=len(cola)+(1 if finServicio else 0)
            Q=len(cola)
            areaSistema+=N * dt
            areaCola+=Q * dt
            ultimoEvento=tiempo=tiempoSiguiente

            #llegada
            if abs(tiempo - proximaLlegada) < 1e-12:
                totalLlegadas+=1
                if N<self.capacidadSistema:
                    cola.append(tiempo)
                else:
                    clientesRechazados+=1
                proximaLlegada=tiempo + random.expovariate(self.tasaLlegada)

            #fin de servicio
            if finServicio and abs(tiempo-finServicio) < 1e-12:
                clientesAtendidos+=1
                if clienteActual is not None:
                    sumaTiempoSistema+=(tiempo - clienteActual)
                    clienteActual=None
                finServicio=None

            #iniciar servicio si servidor libre y cola no vacía
            if not finServicio and cola:
                clienteActual=cola.pop(0)
                sumaTiempoCola+=(tiempo - clienteActual)
                finServicio=tiempo + random.expovariate(self.tasaServicio)

        tiempoTotal=tiempo
        return {
            'Clientes rechazados': clientesRechazados,
            'Clientes atendidos': clientesAtendidos,
            'Probabilidad de bloqueo': clientesRechazados / totalLlegadas if totalLlegadas else 0.0,
            'Número promedio en el sistema': areaSistema / tiempoTotal if tiempoTotal else 0.0,
            'Número promedio en la cola': areaCola / tiempoTotal if tiempoTotal else 0.0,
            'Tiempo promedio en el sistema': sumaTiempoSistema / clientesAtendidos if clientesAtendidos else float('nan'),
            'Tiempo promedio en la cola': sumaTiempoCola / clientesAtendidos if clientesAtendidos else float('nan'),
            'Tasa efectiva de llegadas': (totalLlegadas - clientesRechazados) / tiempoTotal if tiempoTotal else 0.0
        }

#ejemplo de uso:
if __name__=="__main__":
    sim = SistemaColas(tasaLlegada=0.95, tasaServicio=1/1.45, capacidadSistema=5, tiempoMax=15000.0, semilla=1234)
    resultados = sim.run()

    # Mostrar resultados uno debajo del otro
    for clave, valor in resultados.items():
        print(f"{clave}: {valor:.2f}")
