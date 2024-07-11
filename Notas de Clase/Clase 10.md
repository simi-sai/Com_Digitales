# Decima Clase 15/5

Waveform former:

$$w(t) = \underset{j = 1}{\overset{n} \sum} s_j\psi(t-jT)$$

Siendo:

- $s_j$ = (símbolo), un elemento del vector palabra código (escalar).

Expresión anterior:

$w_i(t) = \underset{j=1}{\overset{n}\sum}c_{i,j}\psi(t-jT)$

En este capitulo aprendemos a diseñar el pulso $psi(t)$

RECORDANDO:

Transformada de Fourier:

$$F(t) = \int_{-\infty}^{\infty}f(t)e^{-j\omega t}dt$$

## The ideal lowpass case

Version idealizada del filtro pasabajo:

$$\begin{equation*}
h_\mathcal{F}(f) =
    \left\{
        \begin{aligned}
            1, \quad |f|\leq B \\
            0, \quad \text{otherwise}
        \end{aligned}
    \right.
\quad
\end{equation*}$$

Suponiendo un canal como el de abajo, con un Ruido Gaussiano Aditivo con Densidad Espectral de $N_0/2$. Debido a que el filtro bloquea todas las componentes de la señal que se encuentran fuera del intervalo de frecuencia $[-B,B]$, sin la perdida de optimalidad, consideramos señales que se encuentran estrictamente limitadas en ancho de banda a $[-B,B]$. El teorema del muestreo nos dice que dichas señales pueden ser descriptas por una secuencia de números. La idea es hacer que el encoder produzca estos numeros y dejar que el waveform former haga la interpolación que convierte las muestras en la deseada waveform $w(t)$.

![[Pasted image 20240611104231.png]]

## Teorema de Muestreo

Sea $w(t)$ una función continua $\mathcal{L}_2$ (con posibilidad de ser compleja) y sea su transformada de Fourier $w_{\mathcal{F}}(f)$ desaparecida (vanished) para valores $f \notin [-B,B]$. Entonces $w(t)$ puede ser reconstruida de una secuencia de muestras separadas por T-espacios $w(nT)$, $n \in \mathbb{Z}$, proveido que $T \leq \frac{1}{2B}$. Especificamente, 

![[Pasted image 20240611111016.png]]

donde $sinc(t)=\frac{\sin(\pi t)}{\pi t}$.

$f(t) = sinc(\frac{t}{T})$

$\langle f(t),f(t) \rangle = \int_{-\infty}^{\infty}f(t)f(t)dt$

El pulso $sinc$ que se utiliza en el testamento del Teorema del Muestreo no está normalizado a energía unitaria. Si la normalizamos, definimos específicamente  $\psi(t) = \frac{1}{\sqrt{T}}sinc(\frac{t}{T})$ entonces $\{\psi(t-jT)\}_{j=\infty}^{\infty}$ forma un set ortonormal. Esto se puede verificar usando la Relación de Perseval.

![[Pasted image 20240611111622.png]]

donde $s_j = w(jT)\sqrt{T}$. Por ende una señal $w(t)$ que cumple las condiciones del Teorema de Muestreo es una que vive en el producto interno del espacio abarcado por $\{\psi(t-jT)\}_{j=\infty}^{\infty}$. Al muestrear dicha señal, obtenemos (up to a scaling factor) los coeficientes de su expansión ortonormal con respecto a la base ortonormal $\{\psi(t-jT)\}_{j=\infty}^{\infty}$.

Cabe destacar que usamos el Teorema de Muestreo algoasi como al reves. En una tipica aplicación del Teorema de Muestreo el primer paso consiste en muestrear la señal de la fuente, luego dichas muestras son almacenadas o transmitidas para luego reconstruir la señal original. Al contrario, en el diagrama 5.2, el transmisor realiza la (re)construcción como primer paso, dicha señal (re)construida es transmitida, y finalmente el receptor hace el muestreo. 

Bonus:

La transformada de Fourier de la señal $sinc$ es:

$$\begin{equation*}
\psi_\mathcal{F}(f) =
    \left\{
        \begin{aligned}
            \sqrt{T}, \quad |f|\leq \frac{1}{2T} \\
            0, \quad \text{otherwise}
        \end{aligned}
    \right.
\quad
\end{equation*}$$

## Autocovarianza

Un vector aleatorio queda completamente caracterizado por su función de densidad de probabilidad (pdf).

$K_X[i] := \mathbb{E}[(X_{j+i} - \mathbb{E}[X_{j+i}])(X_j-\mathbb{E}[X_j])^*] = \mathbb{E}[X_{j+i}X_j^*]$

$X = [X_0, X_1, ..., X_n]$

$X$ es un vector de Variable Aleatoria de Media Cero.

donde $\mathbb{E}$ es la Esperanza:

$\mu_X = \mathbb{E}_{\{X\}} = [\mathbb{E}_{\{X_0\}}, ..., \mathbb{E}_{\{X_n\}}]$

Correlación = $R_X(j)= \mathbb{E}_{\{X_i,X_{i+j}\}}$

La matriz de correlación, $R$ se relaciona con la matriz de covarianza $K$ de manera que $K=R-\mu\mu^T$

Covarianza = $K_X(j) = \mathbb{E}_{\{(x_{i}-\mu_{x})(x_{i+j}-\mu_{x})\}}$

La matriz de covarianza $K$, asociada con un vector de variables aleatorias reales $X$, es el valor esperado del producto externo de $(X-\mu)(X-\mu)^T$ siendo $\mu$ el vector de valores esperados.

Sean los vectores aleatorios $X,Y$, con sus respectivos vectores de medias $\mu_X,\mu_Y$. Si el valor esperado del producto externo entre ellos resulta: $E\{XY^T\}=\mu_X\mu_Y$ se dice que los vectores aleatorios son NO correlacionados. En cambio si el valor es $E\{XY^T\}=0$ ambos vectores son ortogonales.

Sean dos vectores aleatorios, con sus respectivos vectores de medias, si la densidad conjunta de ambos es igual al producto de las pdf individuales se dice que son Independientes. $f_{XY}(x,y)=f_X(x)\cdot f_Y(y)$

La esperanza de un vector $X$ de variables aleatorias resulta en un nuevo vector determinístico, de la misma dimensión que el vector $X$.