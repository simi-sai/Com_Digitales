# Undécima Clase 29/05

Al sacarle la media a la covarianza de una señal, se la está volviendo determinística. (?)

## Power Spectrum Density (PSD)

$$S_X(f)=\frac{|\xi_{\mathcal{F}}(f)|^2}{T}\sum_kK_X[k]\exp(-j2\pi kfT)$$

Es la transformada de Fourier de tiempo discreto de $\{K_X[k]\}_{k=-\infty}^{\infty}\}$, valuada en $fT$. Esta es la densidad espectral de potencia del proceso de tiempo discreto $\{X_i\}_{i=-\infty}^{\infty}$. Si pensamos que $\frac{|\xi_{\mathcal{F}}(f)|^2}{T}$ es la densidad espectral de potencia de $\xi(t)$, podemos interpretar a $S_X(f)$ como el producto entre 2 PSD, la de $\xi(t)$ y la de $\{X_i\}_{i=-\infty}^{\infty}$.

**Power Spectral Density:**

La PSD (densidad espectral de potencia) de la salida del transmisor modelada como:

$$X(t) = \sum_{i=-\infty}^{\infty}X_i\xi(t-iT-\Theta)$$

donde $\{X_j\}_{j=-\infty}^{\infty}$ es un proceso de tiempo discreto de media zero estacionaria de amplio sentido (zero-mean wide-sense stationary (WSS)), $\xi(t)$ es una funcion $\mathcal{L}_2$ arbitraria (no necesariamente normalizada o ortonormal) y $\Theta$ es un retardo aleatorio (dither o delay) independiente de $\{X_j\}_{j=-\infty}^{\infty}$.

Autocovarianza (formula):

![[Pasted image 20240611191051.png]]

que depende solo de $i$ ya que asumimos $\{X_j\}_{j=-\infty}^\infty$ es WSS.

Self-similarity function of a the pulse $\xi(\tau)$:

$$R_\xi(\tau)=\int_{-\infty}^{\infty}\xi(\alpha+\tau)\xi^*(\alpha)d\alpha$$

El proceso $X(t)$ es de media cero. Utilizando la independencia entre $\Theta$ y $X_i$ y el hecho de que $\mathbb{E}[X_i]=0$, obtenemos que $\mathbb{E}[X(t)]=\sum_{i=-\infty}^\infty \mathbb{E}[X_i]\mathbb{E}[\xi(t-iT-\Theta)]=0$

La **autocovarianza** de $X(t)$ es:

$K_X(t+\tau,t) = \mathbb{E}[(X(t+\tau)-\mathbb{E}[(t+\tau])(X(t)-\mathbb{E}[X(t)])^*]=...$

$...=\mathbb{E}[X(t+\tau)X^*(t)]$

## Nyquist criterion for orthonormal bases

En la seccion anterior vimos que un tren de impulsos de simbolo-a-simbolo con símbolos no correlacionados genera un proceso estocástico (no determinístico) de densidad espectral de potencia $\mathcal{E}\frac{|\psi_\mathcal{F}(f)|^2}{T}$. Donde $\mathcal{E}$ es la energía promedio del simbolo.

Hay que recordar que $\psi(t)$ debe ser ortogonal *"to its T-spaced time translates"*.

Estamos viendo el equivalente en dominio de frecuencia de la condición:

$$\int_{-\infty}^{\infty}\psi(t-nT)\psi^*(t)dt=\mathbb{1}\{n=0\}$$

*"debe ser 0 excepto para n = 0 que vale 1"*.

La transformada de Fourier de un impulso es una constante.

La forma de la derecha suguiere utilizar la relacion de Parseval, haciendolo:

$$\mathbb{1}\{n=0\}=\int_{-\infty}^{\infty}\psi(t-nT)\psi^*(t)dt=...=\int_{-\frac{1}{2T}}^{\frac{1}{2T}}g(f)e^{-j2\pi nTf}df$$

donde $g(f)=\sum_{k\in\mathbb{Z}}|\psi_{\mathcal{F}}(f-\frac{k}{T})|^2$. Nótese que $g(f)$ es una función periódica de periodo $1/T$. Debido a que $A_0=T$ y $A_k=0$ para cada $k\neq0$, la serie de Fourier de $g(f) es la constante $T$.

"Teorema de Nyquist $\neq$ Criterio de Nyquist"

### Nyquist's criterion for orthonormal pulses

Sea $psi(t)$ una funcion $\mathcal{L}_2$. El set $\{\psi(t-jT)\}_{j=-\infty}^\infty$ consiste de funciones ortonormales si y solo si:

$$\operatorname{l.i.m.}\sum_{k=-\infty}^{\infty}|\psi_{\mathcal{F}}(f-\frac{k}{T})|^2=T, \quad f\in\mathbb{R}$$

siendo $\operatorname{l.i.m.}$ el limite en la norma de $\mathcal{L}_2$. Significa que a medida que agregamos mas y mas términos a la suma del lado izquierdo convierte $\mathcal{L}_2$ equivalente a la constante del lado derecho. el $\operatorname{l.i.m}$ es una tecnicidad debido a la Serie de Fourier.

Una función en el dominio de la frecuencia $a_\mathcal{F}(f)$ es dicha que satisface el Criterio de Nyquist con un parámetro $p$ si por cada $f\in\mathbb{R}$, $\operatorname{l.i.m.}\sum_{k=-\infty}^\infty a_\mathcal{F}(f-k/p)=p$

Funciones que satisfacen el criterio de Nyquist:

![[Pasted image 20240529103336.png]]

## Coseno Realzado

Por cada $\beta \in (0,1)$, y cada $T > 0$ la función **coseno realzado**:

![[Pasted image 20240529103508.png]]

cumple el criterio de Nyquist con el parámetro T.

Usando la relación $\frac{1}{2}(1+\cos(\alpha)) = \cos^2(\alpha/2)$ podemos sacar la raíz cuadrada y obtenemos la **raíz de coseno realzado**:

![[Pasted image 20240529104107.png]]

La transformada inversa de Fourier de $psi_\mathcal{F}(f)$, derivada es la respuesta al impulso de la raíz-coseno-realzado:

![[Pasted image 20240611201107.png]]

donde $\operatorname{sinc}(x)=\frac{\sin(\pi x)}{\pi x}$. El impulso se ve abajo:

![[Pasted image 20240529105408.png]]

"Se mandan $\{1,1,-1,1\}$"

"Al proyectar la señal recibida (b) sobre la base (raiz coseno realzado) obtengo la primer señal, para el resto hay que hacer mas cosas"

## Relación de Parseval

Es la energía de la señal en el dominio de la frecuencia.

$$\int a(t)b^*(t)dt=\int a_\mathcal{F}b_\mathcal{F}^*(f)df$$

que establece que $\langle a(t),b(t)\rangle=\langle a_\mathcal{F}(f),b_\mathcal{F}(f)$.

## Diagramas de Ojo

El hecho que $psi(t)$ tenga norma unitaria y sea ortogonal a $psi(t-iT)$ para todo entero $i$ distinto de 0, implica que la funcion autosimilar (self-similarity) $R_\psi(\tau)$ satisface:

![[Pasted image 20240611202031.png]]

La señal sin ruido (noiseless) $w(t)=\sum_is_i\psi(t-iT)$ aplicada a la entrada del filtro apareado de respuesta al impulso $\psi^*(-t)$ produce una salida sin ruido (noiseless) $y(t)=\sum_i s_iR_\psi(t-iT)$, que al ser muestreado en $t=jT$, muestra/despliega/implica (yields) $y(jT)=\sum_is_iR_\psi((j-i)T)=s_j$.

Nota: si $psi(t)$ no es ortogonal a $psi(t-iT)$, que puede ocurrir cuando el pulso truncado es muy corto, entonces $R_\psi(iT)$ será distinta de 0 para varios integrales $i$.

Si definimos $l_i=R_\psi(iT)$, entonces podemos escribir $y(jT)=\sum_is_il_{j-i}$.

El hecho de que la salida $y(jT)$ sin ruido depende de multiples simbolos es referido como "interferencia intra-simbolo" (inter-symbol interference (ISI)). 

Hay 2 causas principales del ISI. La primera es cuando $R_\psi(\tau)$
es distinta de 0 para mas de una muestra. ISI tambien ocurre si la salida del filtro apareado no está muestreada en tiempos correctos. En este caso obtenemos $y(jT+\Delta)=\sum_is_iR_\psi((j-i)T+\Delta)$ que es de nuevo de la forma $\sum_is_il_{j-i}$ para $l_i=R_\psi(iT+\Delta)$.

El diagrama de ojo es una técnica que nos permite visualizar si hay ISI y ver que tan critico es que el tiempo de muestreo sea preciso. El diagrama de ojo es obtenido de la salida del filtro apareado antes del muestreo.

Sea $y(t)=\sum_is_iR_\psi(t-iT)$ la salida sin ruido del filtro apareado, con símbolos tomando valor en algún set discreto $\mathcal{S}$. Para obtener el diagrama de ojo, ploteamos la superposición de trazos de la forma $y(t-iT)$, $t\in[-T,T]$ por varios integrales $i$.

![[Pasted image 20240611203813.png]]

Partiendo de un ejemplo $\mathcal{S}=\{±1\}$. Los graficos (a), (c) y (d) no muestran señales de ISI, debido a que todos los trazos pasan por $±1$ en $t=0$, lo que implica que $y(iT)\in\mathcal{S}$.

Notese que el "ojo" (el espacio no trazado en el medio del diagrama de ojo), es mas ancho en (c) que en (a), esto es una ventaja, debido a que el sistema es mas tolerante a pequeñas variaciones (jitter) en el tiempo de muestreo, esta es una caracteristica de un $\beta$ mas largo y es una consecuencia del hecho que a medida que $\beta$ aumenta, el pulso decae las rapidamente en funcion de |t|. Por la misma razon, un pulso con un beta mas largo puede ser truncado a un largo mas corto, al precio de un mayor ancho de banda.

Configuración del Transmisor:

```python
num_bits    = 2**13   # Number of transmitted bits
sps         = 8       # Samples per symbol
span        = 12      # The filter is truncated to span symbols
beta        = 1       # Excess-bandwidth parameter
```

Configuración básica del SDR:

```python
Uri              = "ip:xxx.xxx.x.xx" 
SamplingRate     = 4e6           # Sample rate RX and TX paths[Samples/Sec]
Loopback         = 1             # 0=Disabled, 1=Digital, 2=RF
TxLOFreq         = xxxe6         # Carrier frequency of TX path [Hz]
TxAtten          = -30           # Attenuation TX path, valid range is -90 to 0 dB
TxRfBw           = 4e6           # Bandwidth of front-end analog filter of TX path
RxLOFreq         = TxLOFreq      # Carrier frequency of RX path [Hz]
GainControlModes = "slow_attack" # Receive path AGC Options: slow_attack, fast_attack, manual
RxHardwareGain   = 0             # Gain applied to RX path. Only applicable when gain_control_mode is set to 'manual'    
RxRfBw           = TxRfBw        # Bandwidth of front-end analog filter of RX path [Hz]
RxBufferSize     = 2**20-1
```

Filtro Raíz Coseno Realzado:

```python
def rrcosdesign(beta,span,sps):
    index     = np.arange(-(span*sps)/2,(span*sps)/2+1,1)
    Ts        = sps
    rrcFilter = np.array([])
    
    for n in index:
        if beta == 0:
            aux       = np.sinc(n/Ts)/np.sqrt(Ts)
            rrcFilter = np.append(rrcFilter,aux)
        else:
            if n == Ts/(4*beta) or n == -Ts/(4*beta):
                aux       = beta*((np.pi+2)*np.sin(np.pi/(4*beta))+(np.pi-2)*np.cos(np.pi/(4*beta)))/(np.pi*np.sqrt(2*Ts))
                rrcFilter = np.append(rrcFilter,aux)
            else:
                a         = np.cos((1+beta)*np.pi*n/Ts)
                b         = (1-beta)*np.pi*np.sinc((1-beta)*n/Ts)/(4*beta)
                c         = 4*beta/(np.pi*np.sqrt(Ts))
                aux       = c*(a+b)/(1-(4*beta*n/Ts)**2)
                rrcFilter = np.append(rrcFilter,aux)

    return rrcFilter
```

```python
import numpy as np

def rrcosfilter(t, beta, Ts,iT):    
    return 1/np.sqrt(Ts) * np.sinc((t-iT)/Ts) * np.cos(np.pi*beta*(t-iT)/Ts) / (1 - (2*beta*(t-iT)/Ts) ** 2)

def raiz_coseno_realzado(simbolos, Beta, T, tt):
  sum_sig = 0
  signal = []
  
  for i in range(len(simbolos)):
    signal.append(simbolos[i]*rrcosfilter(tt,Beta,T,i*T))
    sum_sig = sum_sig + signal[i]
    #plt.plot(tt,output[i])
  return sum_sig,signal  
```

Diagrama de ojo:

```pyhon
q_Signal = qRxFilSignal[-lags[Rmax_pos]+2*span*sps:-lags[Rmax_pos]+len(txSignal)-2*span*sps]
dc.eye_plot(q_Signal,L,S)
plt.show()
```
