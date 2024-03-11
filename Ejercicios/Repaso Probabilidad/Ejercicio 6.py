import random

# Accion de tirar el dado
def tirar_dado():
    return random.randint(1,6)

# Calculo de Probabilidad mediante Monte Carlo
# (Ejercicio 6: probabilidad de que tirando dos dados, ambas caras sean un 1)
def monte_carlo(n):
    A = 0
    B = 0
    coincidencias = 0
    
    for i in range(n):
        dado1 = tirar_dado()
        dado2 = tirar_dado()
    
        if dado1 == 1:
            A += 1
        if dado2 == 1:
            B += 1
        if dado2 == 1 and dado1 == 1:
            coincidencias += 1
    
    return A/n, B/n, coincidencias/n
        
    
# Calculo de la probabilidad
n = 100
A, B, C = monte_carlo(n)
print("P(A): ", A, " P(B): ", B, " con n = ", n)
print("P(AB): ", C, " con n = ", n)

n = 10000        
A, B, C = monte_carlo(n)
print("P(A): ", A, " P(B): ", B, " con n = ", n)
print("P(AB): ", C, " con n = ", n)

n = 10000000       
A, B, C = monte_carlo(n)
print("P(A): ", A, " P(B): ", B, " con n = ", n)
print("P(AB): ", C, " con n = ", n)

# Comprobacion de independencia de los eventos
# Condicion -> P(A|B) = P(A) y P(B|A) = P(B)
print("\nPrueba para comprobar si son independientes ambos eventos\n")

n = 100
A, B, C = monte_carlo(n)
print("P(A|B): ", C/A, " y P(B|A): ", C/B, " con n = ", n)
print("P(A): ", A, " y P(B): ", B, " con n = ", n)

n = 10000
A, B, C = monte_carlo(n)
print("P(A|B): ", C/A, " y P(B|A): ", C/B, " con n = ", n)
print("P(A): ", A, " y P(B): ", B, " con n = ", n)

n = 10000000     
A, B, C = monte_carlo(n)
print("P(A|B): ", C/A, " y P(B|A): ", C/B, " con n = ", n)
print("P(A): ", A, " y P(B): ", B, " con n = ", n)

# Conclusion: Los eventos son independientes