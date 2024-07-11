import numpy as np
from scipy import special

def Q_function(x):
    return 0.5 * (1 - special.erf(x/np.sqrt(2)))

# Metodo abreviado
import numpy as np
from scipy import special

x = 0.01
q_value = Q_function(x)
print("Q({}) = {:.15f}".format(x, q_value))


import numpy as np
def raiz_coseno_realzado(simbolos, Beta, T, tt):
    signal = [[np.zeros(len(simbolos))],[np.zeros(len(tt))]]
    signal_added = np.zeros(len(tt))
    
    for i in range(len(simbolos)):
        for j in range(len(tt)):
            signal_added[i] += simbolos[i] * np.cos(2*np.pi*Beta*T*tt[j])
            signal[i][j] += signal_added[j]
            
            
            
            
