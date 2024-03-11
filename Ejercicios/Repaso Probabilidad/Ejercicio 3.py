import random

# Accion de tirar la moneda
def tirar_moneda():
    return random.randint(1,2)

# Calculo de Probabilidad mediante Monte Carlo
# (Ejercicio 3: Probabilidad de lanzando 2 monedas legales obtener la misma cara)
def monte_carlo(n):
    coincidencias = 0
    
    for i in range(n):
        if tirar_moneda() == tirar_moneda():
            coincidencias += 1
            
    return coincidencias

# Calculo de la probabilidad
n = 100
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)
n = 10000        
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)
n = 10000000       
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)