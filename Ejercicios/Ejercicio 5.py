import random

# Accion de tirar el dado
def tirar_dado():
    return random.randint(1,6)

# Calculo de Probabilidad mediante Monte Carlo
# (Ejercicio 5: - Probabilidad de resultado divisible por 2 en la suma del lanzamiento de 2 dados
#               - Probabilidad de resultado divisible por 4 en la suma del lanzamiento de 2 dados)
def monte_carlo(n):
    coincidenciasA = 0
    coincidenciasB = 0
    coincidenciasC = 0

    for i in range(n):
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        suma = dado1 + dado2
        
        if suma % 4 == 0:
            coincidenciasB += 1
            coincidenciasC += 1
            coincidenciasA += 1
        elif suma % 2 == 0:
            coincidenciasA += 1
    
    return coincidenciasA, coincidenciasB, coincidenciasC
    

# Calculo de la probabilidad
n = 100
A, B, C = monte_carlo(n)
P1 = C/n
P2 = P1 / (A/n)
print("P(AB): ", P1, " con n = ", n)
print("P(B|A): ", P2, " con n = ", n)

n = 10000   
A, B, C = monte_carlo(n)
P1 = C/n
P2 = P1 / (A/n)
print("P(AB): ", P1, " con n = ", n)
print("P(B|A): ", P2, " con n = ", n)

n = 10000000       
A, B, C = monte_carlo(n)
P1 = C/n
P2 = P1 / (A/n)
print("P(AB): ", P1, " con n = ", n)
print("P(B|A): ", P2, " con n = ", n)

print("\nPrueba para comprobar si son independientes ambos eventos\n")
# Condicion -> P(A|B) = P(A) y P(B|A) = P(B)
n = 100
A, B, C = monte_carlo(n)
P1 = C/n
P2 = P1 / (A/n)
P3 = P1 / (B/n)
print("P(A|B): ", P3, " y P(B|A): ", P2, " con n = ", n)
print("P(A): ", A/n, " y P(B): ", B/n)
print("Son independientes: ", P3 == A/n, " y ", P2 == B/n)

n = 10000   
A, B, C = monte_carlo(n)
P1 = C/n
P2 = P1 / (A/n)
P3 = P1 / (B/n)
print("P(A|B): ", P3, " y P(B|A): ", P2, " con n = ", n)
print("P(A): ", A/n, " y P(B): ", B/n)
print("Son independientes: ", P3 == A/n, " y ", P2 == B/n)

n = 10000000       
A, B, C = monte_carlo(n)
P1 = C/n
P2 = P1 / (A/n)
P3 = P1 / (B/n)
print("P(A|B): ", P3, " y P(B|A): ", P2, " con n = ", n)
print("P(A): ", A/n, " y P(B): ", B/n)
print("Son independientes: ", P3 == A/n, " y ", P2 == B/n)