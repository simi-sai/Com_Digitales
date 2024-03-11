import random

# Accion de tirar el dado
def tirar_dado():
    return random.randint(1,6)

# Calculo de Probabilidad mediante Monte Carlo
# (Ejercicio 4: Probabilidad de resultado menor a 5 en la suma del lanzamiento de 2 dados)
def monte_carlo(n):
    coincidencias = 0
    
    for i in range(n):
        if (tirar_dado() + tirar_dado()) < 5:
            coincidencias += 1
            
    return coincidencias

# Calculo de la probabilidad
n = 100
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)
n = 10000        
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)
n = 10000000       
print("Probabilidad: ", monte_carlo(n)/ n, " con n = ", n)
