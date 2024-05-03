import numpy as np
from scipy.special import erf

def Q_function(x):
    return 0.5 * (1 - erf(x/np.sqrt(2)))

# Metodo abreviado
x = 0
q_value = Q_function(x)
print("Q({}) = {:.15f}".format(x, q_value))
