# Decima Clase 15/5

Waveform former:

$$w(t) = \underset{j = 1}{\overset{n} \sum} s_j\psi(t-jT)$$

Siendo:

- $s_j$ = un elemento del vector palabra código (escalar)

Expresion anterior:

$w_i(t) = \underset{j=1}{\overset{n}\sum}c_{i,j}\psi(t-jT)$

En este capitulo aprendemos a diseñar el pulso $psi(t)$

RECORDANDO:

Transformada de Fourier:

$$F(t) = \int_{-\infin}^{\infin}f(t)e^{-j\omega t}dt$$

## The ideal lowpass case

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

## Repaso Seno Realzado ($sinc(t)$)

$f(t) = sinc(\frac{t}{T})$

$\langle f(t),f(t) \rangle = \int_{-\infin}^{\infin}f(t)f(t)dt$

El pulso sinc que se utiliza en el testamento del teorema del muestreo no está normalizada a energia unitaria. Si la normalizamos, especificamente definimos $\psi(t) = \frac{1}{\sqrt{T}}sinc(\frac{t}{T})$ entonces ${...}$

...

donde $s_j = w(jT)\sqrt{T}$

## No me acuerdo que tema

$K_X[i] := \mathbb{E}[(X_{j+i} - \mathbb{E}[X_{j+i}])(X_j-\mathbb{E}[X_j])^*] = \mathbb{E}[X_{j+i}X_j^*]$

$X = [X_0, X_1, ..., X_n]$

X es un vector de Variable Aleatoria de Media Cero

donde $\mathbb{E}$ es la Esperanza:

$\mu_X = \mathbb{E}_{\{X\}} = [\mathbb{E}_{\{X_0\}}, ..., \mathbb{E}_{\{X_n\}}]$

Correlacion = $R_X(j)= \mathbb{E}_{\{X_i,X_{i+j}\}}$

Covarianza = $K_X(j) = \mathbb{E}_{\{(x_i-\mu_x_)(x_{i+j}-\mu_x)\}}$