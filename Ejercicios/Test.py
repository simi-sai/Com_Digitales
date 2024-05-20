import numpy as np
from scipy import special

def Q_function(x):
    return 0.5 * (1 - special.erf(x/np.sqrt(2)))

# Metodo abreviado
x = 0.01
q_value = Q_function(x)
print("Q({}) = {:.15f}".format(x, q_value))
