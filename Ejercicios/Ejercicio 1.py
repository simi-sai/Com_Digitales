import random

# Accion de tirar el dado
def tirar_dado():
    return random.randint(1,6)

# Calculo de Probabilidad mediante Monte Carlo
# (Ejercicio 1: Probabilidad de que salga un numero par)
def monte_carlo(n):
    coincidencias = 0
    
    for i in range(n):
        if tirar_dado() % 2 == 0:
            coincidencias += 1
            
    return coincidencias

# Calculo de la probabilidad
n = 100
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)
n = 10000        
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)
n = 10000000       
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)