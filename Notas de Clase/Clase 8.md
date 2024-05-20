# Octava Clase 24/04

![alt text](Imagenes/image-16.png)

Para este caso la matriz de covarianza esta implicita, se supone su valor de la diagonal $\sigma^2=\frac{N_0}{2}$. Si no fuera este el caso aparecerian otros terminos dentro de la ecuacion.

## Norma MAP

### I

$$\underset{i}\argmax{P_H(i)\cdot f_{Y|H}(y|i)} \\ \underset{i}\argmax{[\ln P_H(i)+(-\frac{\|y-c_i\|^2}{2\sigma^2})]} \\ \underset{i}\argmin{[\|y-c_i\|^2-\ln{f_H(i)\cdot2\sigma^2}]}$$

### II

$y\nearrow\downarrow Z = y - c_i\\\longrightarrow\\c_i$

$Z = \{Z_1,Z_2,...,Z_n\}$ Ruido

$Z_i=\langle N,\sigma_i \rangle$

$\|a\|^2 = \langle a,a \rangle$

$\langle a,b \rangle = a \cdot b = \|a\| \|b\| \cos(\angle{ab})$

$\|a-b\|^2 = \langle a-b,a-b \rangle = \langle a-b,a \rangle -\langle a-b,b\rangle = \langle a,a \rangle - \langle b,a \rangle - \langle a,b \rangle + \langle b,b \rangle$

### III

![alt text](Imagenes/image-18.png)

![alt text](Imagenes/image-17.png)

Si $a$ es complejo la norma de a al cuadrado $\|a\|^2$ es igual a $\langle a,a^* \rangle$ siendo $a^*$ el vector conjugado.

Muestreo filtrado. (??)

Una forma de expresar la convolución

$$y(T) = \int r(t) b(t)dt \\ y(\alpha) = \int r(t)b^*(\alpha - T + t) dt = r(t) * b^*(-t+T)$$

$$\alpha = T \rightarrow y(T) = \int r(t)b^*(t)$$

![alt text](Imagenes/image-19.png)

![alt text](Imagenes/image-20.png)

$$\int w_1 \psi $$

![alt text](Imagenes/image-21.png)
