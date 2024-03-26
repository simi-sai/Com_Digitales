import random
import numpy as np
import matplotlib.pyplot as plt

# Accion de tirar la moneda
def lanzar_moneda():
    return random.randint(0,1)

# Calculo de Probabilidad mediante Monte Carlo
# (Ejercicio 7: Lanzando 3 monedas legales, calcular y graficar la funcion distribucion de probabilidades)
def monte_carlo(n):
    
    grupos = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for _ in range(n):
        monedas = [lanzar_moneda(), lanzar_moneda(), lanzar_moneda()]
        num = 4 * monedas[0] + 2 * monedas[1] + monedas[2]
        grupos[num] += 1
        
    for i in range(8):
        grupos[i] = grupos[i] / n
        
    return grupos

# Grafico de la funcion distribucion probabilidades
def graficar_resultados(probabilidades):
    
    u = lambda t: np.heaviside(t,1)
    ti  = np.arange(-10, 10, 0.1)
    u0_i = 0
    
    for i in range(8):
        u0_i += probabilidades[i] * u(ti - i)

    # SALIDA - GRAFICA
    print('x:',ti)
    print('x:',u0_i)

    # GRAFICA
    plt.figure(1)
    plt.plot(ti,u0_i)

    plt.xlabel('x')
    plt.ylabel('Distribucion Acumulativa de Probabilidades con n = '+ str(n))
    plt.margins(0.1)
    plt.grid()
    plt.show()

# Calculo de las Probabilidades
n = 100
probabilidades = monte_carlo(n)
print(probabilidades)
graficar_resultados(probabilidades)

n = 10000
probabilidades = monte_carlo(n)
print(probabilidades)
graficar_resultados(probabilidades)

n = 1000000
probabilidades = monte_carlo(n)
print(probabilidades)
graficar_resultados(probabilidades)