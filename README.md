[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=David84595/MSFProyecto)

# Proyecto Final — Modelado y control del sistema respiratorio (Asma)

## Información del equipo
* **Prado Acosta Briseida** · `23210715` · L23210715@tijuana.tecnm.mx
* **Cerano Fuentes David Esaú** · `23210696` · L23210696@tijuana.tecnm.mx
* **Contreras Jiménez Kenia Yasdit** · `23212188` · L23212188@tijuana.tecnm.mx

**Asignatura:** Modelado de Sistemas Fisiológicos  
**Programa:** Ingeniería Biomédica  
**Docente:** Dr. Paul Antonio Valle Trujillo (`paul.valle@tectijuana.edu.mx`)  
**Institución:** Tecnológico Nacional de México / Instituto Tecnológico de Tijuana  
**Sede:** Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

---

## Contenido

1. [Resumen y objetivo del proyecto](#resumen-y-objetivo-del-proyecto)
2. [Descripción fisiológica y enfermedad seleccionada (Asma)](#descripción-fisiológica-y-enfermedad-seleccionada-asma)
3. [Diagrama fisiológico (BioRender) y circuito equivalente](#diagrama-fisiológico-biorender-y-circuito-equivalente)
4. [Analogía eléctrica y parámetros (Control vs. Caso)](#analogía-eléctrica-y-parámetros-control-vs-caso)
5. [Desarrollo matemático](#desarrollo-matemático)
6. [Experimentación in silico en lazo abierto](#experimentación-in-silico-en-lazo-abierto)
7. [Diseño del sistema de control en lazo cerrado (PID)](#diseño-del-sistema-de-control-en-lazo-cerrado-pid)
8. [Interpretación fisiológica del control y discusión](#interpretación-fisiológica-del-control-y-discusión)
9. [Estructura del repositorio y entregables](#estructura-del-repositorio-y-entregables)
10. [Declaración de uso de LLM](#declaración-de-uso-de-llm)
11. [Referencias](#referencias)

---

## Resumen y objetivo del proyecto

Este proyecto final integra el modelado fisiológico, el análisis de circuitos eléctricos RLC, la formulación de ecuaciones diferenciales y funciones de transferencia, el análisis de estabilidad, la simulación computacional (*MATLAB/Simulink*, *Simscape Electrical* y *Python*) y el diseño de estrategias de control clásico.

### Objetivo general
Diseñar un modelo matemático didáctico de segundo orden del **sistema respiratorio** mediante una analogía eléctrica basada en un circuito RLC, con la finalidad de comparar la respuesta dinámica correspondiente a un individuo sano (**control**) frente a un escenario patológico de **asma** (**caso**), y diseñar un controlador PID que reduzca la diferencia entre ambas respuestas.

> **Alcance académico:** El modelo desarrollado tiene una finalidad estrictamente didáctica y académica, incluyendo simplificaciones y condiciones ideales de operación. Los valores eléctricos de resistencia, capacitancia e inductancia actúan como parámetros equivalentes del modelo y no representan mediciones clínicas directas ni herramientas de diagnóstico o tratamiento médico.

**Palabras clave:** Sistema respiratorio; Analogía eléctrica RLC; Función de transferencia; Asma; Controlador PID;.

---

## Descripción fisiológica y enfermedad seleccionada (Asma)

### Fisiología del sistema respiratorio
La mecánica ventilatoria consiste en el desplazamiento del aire desde la atmósfera hasta los alvéolos pulmonares a través de las vías aéreas de conducción (tráquea, bronquios y bronquiolos), impulsado por gradientes de presión generados por los músculos respiratorios. Durante este proceso intervienen propiedades resistivas (oposición al flujo aéreo en las vías conductoras y el tejido), capacitivas (compliancia o distensibilidad pulmonar y alveolar) e inductivas (inertancia del aire y del tejido pulmonar ante cambios rápidos de flujo).

### Alteración fisiopatológica: Asma bronquial
El **asma** es una enfermedad inflamatoria crónica de las vías respiratorias caracterizada por hiperreactividad bronquial, edema de la mucosa, hipersecreción de moco y broncoconstricción del músculo liso bronquial. Fisiológicamente, este estrechamiento de la luz bronquial provoca un **incremento significativo en la resistencia al flujo aéreo ($R_2$)**, reduciendo el flujo de aire hacia los alvéolos y alterando la respuesta ventilatoria ante un estímulo respiratorio.

* **Escenario Control (Individuo sano):** Resistencia bronquial normal, flujo aéreo adecuado y respuesta respiratoria estable.
* **Escenario Caso (Asma):** Incremento en la resistencia bronquial ($R_2$), disminución del flujo aéreo efectivo y caída en la respuesta de presión/ventilación alveolar.

---

## Diagrama fisiológico (BioRender) y circuito equivalente

### 1. Diagrama biológico del sistema respiratorio (BioRender)

<img width="1256" height="892" alt="image" src="https://github.com/user-attachments/assets/b47d7cd2-db35-4c9b-abb7-132739097b5f" />


*Figura 1.* Representación anatómica y funcional del sistema respiratorio en condiciones normales (Control) y con asma (Caso), mostrando la correspondencia de los elementos eléctricos ($V_e(t)$, $R_1$, $R_2$, $R_3$, $C$, $L$, $I_1(t)$ y $V_s(t)$). Elaborado en BioRender.com.

### 2. Circuito eléctrico equivalente de segundo orden

<img width="768" height="326" alt="image" src="https://github.com/user-attachments/assets/32b59f5f-b7b2-4b88-acf4-45f774cec187" />


*Figura 2.* Topología del circuito eléctrico equivalente propuesto para el modelado del sistema respiratorio ($R_1$, $C$, $L$, $R_2$, $R_3$), identificando la entrada $V_e(t)$, los nodos $V_1$, $V_2$ y la salida $V_s(t)$.

---

## Analogía eléctrica y parámetros (Control vs. Caso)

La siguiente tabla resume las correspondencias fisiológicas propuestas, los valores numéricos asignados para el individuo sano (*control*) y el paciente con asma (*caso*), así como sus unidades equivalentes:

| Elemento | Interpretación fisiológica | Valor Control (Sano) | Valor Caso (Asma) | Unidad eléctrica | Analogía fisiológica | Origen del parámetro |
| --- | --- | --- | --- | --- | --- | --- |
| $V_e(t)$ | Presión motriz / Estímulo inspiratorio de entrada | $1$ | $1$ | $\mathrm{V}$ | $\mathrm{cmH_2O}$ | Selección didáctica (escalón unitario) |
| $R_1$ | Resistencia de las vías aéreas superiores (Tráquea) | $2 \times 10^2$ ($200$) | $2 \times 10^2$ ($200$) | $\Omega$ | $\mathrm{cmH_2O \cdot s \cdot L^{-1}}$ | Selección didáctica equivalente |
| $R_2$ | Resistencia de las vías aéreas medias (Bronquios) — **Parámetro alterado en asma** | $1 \times 10^2$ ($100$) | $8 \times 10^2$ ($800$) | $\Omega$ | $\mathrm{cmH_2O \cdot s \cdot L^{-1}}$ | Incremento por broncoconstricción asmática |
| $R_3$ | Resistencia viscosa del tejido pulmonar / intercambio | $1 \times 10^3$ ($1000$) | $1 \times 10^3$ ($1000$) | $\Omega$ | $\mathrm{cmH_2O \cdot s \cdot L^{-1}}$ | Selección didáctica equivalente |
| $C$ | Compliancia / Distensibilidad de bronquiolos y alvéolos | $1 \times 10^{-3}$ ($1\,\mathrm{mF}$) | $1 \times 10^{-3}$ ($1\,\mathrm{mF}$) | $\mathrm{F}$ | $\mathrm{L \cdot cmH_2O^{-1}}$ | Selección didáctica equivalente |
| $L$ | Inertancia del flujo aéreo y masa de tejido pulmonar | $1 \times 10^{-5}$ ($10\,\mu\mathrm{H}$) | $1 \times 10^{-5}$ ($10\,\mu\mathrm{H}$) | $\mathrm{H}$ | $\mathrm{cmH_2O \cdot s^2 \cdot L^{-1}}$ | Selección didáctica equivalente |
| $V_s(t)$ | Presión / Respuesta ventilatoria efectiva en el tejido | Salida | Salida | $\mathrm{V}$ | $\mathrm{cmH_2O}$ | Variable de salida medida sobre $R_3$ |

### Justificación de la señal de entrada
Se selecciona una **entrada escalón unitario** $V_e(t) = u(t)$ ($1\,\mathrm{V}$), la cual representa un esfuerzo inspiratorio sostenido aplicado sobre el sistema respiratorio para evaluar tanto la velocidad de llenado/respuesta transitoria como el nivel ventilatorio alcanzado en estado estacionario.

---

## Desarrollo matemático

### 1. Ecuaciones en el dominio del tiempo y Leyes de Kirchhoff

El circuito presenta dos elementos independientes de almacenamiento de energía ($C$ y $L$), por lo que constituye un **sistema dinámico de segundo orden**. Definiendo los nodos $V_1(t)$ (nodo del capacitor $C$) y $V_2(t) = V_s(t)$ (nodo de salida sobre $R_3$), se tiene que la corriente por la rama de salida es:

$$I_2(t) = \frac{V_2(t)}{R_3}.$$

La caída de tensión a través de la rama serie $L$–$R_2$ está dada por:

$$V_1(t) - V_2(t) = L \frac{d I_2(t)}{dt} + R_2 I_2(t) = \frac{L}{R_3} \frac{d V_2(t)}{dt} + \frac{R_2}{R_3} V_2(t).$$

Aplicando la Ley de Corrientes de Kirchhoff (LCK) en el nodo 1:

$$\frac{V_e(t) - V_1(t)}{R_1} = C \frac{d V_1(t)}{dt} + I_2(t) = C \frac{d V_1(t)}{dt} + \frac{V_2(t)}{R_3}.$$

### 2. Modelo mediante ecuaciones integro-diferenciales (EID)

De manera equivalente, planteando las ecuaciones de malla en función de las corrientes $i_1(t)$ e $i_2(t)$ para su implementación en bloques de Simulink:

$$V_e(t) = R_1 i_1(t) + \frac{1}{C} \int \left[i_1(t) - i_2(t)\right] dt$$

$$0 = L \frac{d i_2(t)}{dt} + R_2 i_2(t) + R_3 i_2(t) + \frac{1}{C} \int \left[i_2(t) - i_1(t)\right] dt$$

$$V_s(t) = R_3 i_2(t).$$

### 3. Obtención de la función de transferencia general

Aplicando la transformada de Laplace con condiciones iniciales nulas a las ecuaciones nodales:

$$\frac{V_e(s) - V_1(s)}{R_1} = s C V_1(s) + \frac{V_2(s)}{R_3}$$

Despejando $V_e(s)$:

$$V_e(s) = (1 + R_1 C s) V_1(s) + \frac{R_1}{R_3} V_2(s).$$

De la relación entre $V_1(s)$ y $V_2(s)$ en la rama serie $L$–$R_2$:

$$V_1(s) = \left(\frac{s L + R_2 + R_3}{R_3}\right) V_2(s).$$

Sustituyendo $V_1(s)$ en la expresión de $V_e(s)$ y multiplicando ambos lados por $R_3$:

$$R_3 V_e(s) = \left[ (1 + R_1 C s)(s L + R_2 + R_3) + R_1 \right] V_2(s)$$

$$R_3 V_e(s) = \left[ R_1 C L s^2 + \left(L + R_1 C (R_2 + R_3)\right) s + (R_1 + R_2 + R_3) \right] V_2(s).$$

Dado que $V_s(s) = V_2(s)$, la **función de transferencia general** del sistema respiratorio es:

$$\boxed{G(s) = \frac{V_s(s)}{V_e(s)} = \frac{R_3}{R_1 C L s^2 + \left[L + R_1 C (R_2 + R_3)\right] s + (R_1 + R_2 + R_3)}}$$

### 4. Sustitución de parámetros: Control (Sano) vs. Caso (Asma)

#### Escenario Control (Individuo sano)
Sustituyendo $R_1 = 200\,\Omega$, $R_2 = 100\,\Omega$, $R_3 = 1000\,\Omega$, $C = 1 \times 10^{-3}\,\mathrm{F}$ y $L = 1 \times 10^{-5}\,\mathrm{H}$:
* $R_1 C L = (200)(10^{-3})(10^{-5}) = 2 \times 10^{-6}$
* $L + R_1 C (R_2 + R_3) = 10^{-5} + (200)(10^{-3})(100 + 1000) = 220.00001$
* $R_1 + R_2 + R_3 = 200 + 100 + 1000 = 1300$

$$G_{\mathrm{control}}(s) = \frac{1000}{2 \times 10^{-6} s^2 + 220.00001 s + 1300}.$$

#### Escenario Caso (Asma)
Sustituyendo $R_1 = 200\,\Omega$, $R_2 = 800\,\Omega$, $R_3 = 1000\,\Omega$, $C = 1 \times 10^{-3}\,\mathrm{F}$ y $L = 1 \times 10^{-5}\,\mathrm{H}$:
* $R_1 C L = (200)(10^{-3})(10^{-5}) = 2 \times 10^{-6}$
* $L + R_1 C (R_2 + R_3) = 10^{-5} + (200)(10^{-3})(800 + 1000) = 360.00001$
* $R_1 + R_2 + R_3 = 200 + 800 + 1000 = 2000$

$$G_{\mathrm{caso}}(s) = \frac{1000}{2 \times 10^{-6} s^2 + 360.00001 s + 2000}.$$

### 5. Cálculo del error en estado estacionario

Aplicando el Teorema del Valor Final ante una entrada escalón unitario $V_e(s) = \frac{1}{s}$:

$$e_{\mathrm{ss}} = \lim_{s \to 0} s \left(\frac{1}{s}\right) \left[1 - G(s)\right] = 1 - G(0).$$

**Para el escenario Control (Individuo sano):**

$$G_{\mathrm{control}}(0) = \frac{1000}{1300} \approx 0.7692\,\mathrm{V} \quad \Rightarrow \quad e_{\mathrm{ss,control}} = 1 - \frac{1000}{1300} = \frac{300}{1300} \approx 0.2308\,\mathrm{V} \quad (23.08\,\%).$$

**Para el escenario Caso (Asma):**

$$G_{\mathrm{caso}}(0) = \frac{1000}{2000} = 0.5000\,\mathrm{V} \quad \Rightarrow \quad e_{\mathrm{ss,caso}} = 1 - \frac{1000}{2000} = 0.5000\,\mathrm{V} \quad (50.00\,\%).$$

La broncoconstricción simulada al aumentar $R_2$ de $100\,\Omega$ a $800\,\Omega$ reduce la ganancia en estado estacionario de $0.7692\,\mathrm{V}$ ($76.92\,\%$) a $0.5000\,\mathrm{V}$ ($50.00\,\%$), provocando un déficit ventilatorio estacionario de $0.2692\,\mathrm{V}$ respecto al individuo sano.

### 6. Análisis de estabilidad y cálculo de polos en lazo abierto

Calculando las raíces del denominador $a s^2 + b s + c = 0$ mediante la fórmula general:

**Polos para el Control:**

$$s = \frac{-220.00001 \pm \sqrt{(220.00001)^2 - 4(2 \times 10^{-6})(1300)}}{2(2 \times 10^{-6})}$$

$$s_1 \approx -5.909, \qquad s_2 \approx -1.10 \times 10^8.$$

**Polos para el Caso:**

$$s = \frac{-360.00001 \pm \sqrt{(360.00001)^2 - 4(2 \times 10^{-6})(2000)}}{2(2 \times 10^{-6})}$$

$$s_1 \approx -5.556, \qquad s_2 \approx -1.80 \times 10^8.$$

**Conclusión de estabilidad:** En ambos escenarios, los dos polos son reales, distintos y estrictamente negativos (ubicados en el semiplano izquierdo del plano $s$). Por lo tanto, **ambos sistemas son estables en lazo abierto y presentan una respuesta sobreamortiguada** sin oscilaciones. El polo dominante del caso ($s_1 \approx -5.556$) se desplaza ligeramente hacia el origen respecto al control ($s_1 \approx -5.909$), reflejando una constante de tiempo mayor (respuesta más lenta) además de la caída de amplitud.

---

## Experimentación in silico en lazo abierto

Para ambos escenarios (*control* y *caso*) se implementan y verifican de manera independiente tres representaciones equivalentes en **MATLAB/Simulink**:
1. **Ecuaciones integro-diferenciales (EID):** Diagrama de bloques construido a partir de integradores, ganancias y sumadores.
2. **Función de transferencia:** Bloques `Transfer Fcn` con los coeficientes calculados de $G_{\mathrm{control}}(s)$ y $G_{\mathrm{caso}}(s)$.
3. **Circuito eléctrico equivalente:** Modelo físico implementado en **Simscape Electrical**.

---

## Diseño del sistema de control en lazo cerrado (PID)

Con el objetivo de compensar la pérdida de respuesta ventilatoria causada por el asma, se implementa un lazo de retroalimentación negativa tomando la respuesta del individuo sano como señal de referencia:

$$r(t) = V_{s,\mathrm{control}}(t), \qquad e(t) = V_{s,\mathrm{control}}(t) - V_{s,\mathrm{caso}}(t).$$

La ley de control PID está dada por:

$$C(s) = k_P + \frac{k_I}{s} + k_D s.$$

### Parámetros de sintonización (Herramienta *Tune* de Simulink)

| Parámetro / Métrica de desempeño | Valor obtenido |
| --- | --- |
| Ganancia proporcional ($k_P$) | 289.557|
| Ganancia integral ($k_I$) | 70561.079 |
| Ganancia derivativa ($k_D$) | 0.038 |

---

## Interpretación fisiológica del control y discusión

* **Variable fisiológica controlada:** El nivel de presión y flujo aéreo efectivo que alcanza el compartimento alveolar/tejido pulmonar ($V_s(t)$), el cual se ve disminuido por la resistencia bronquial en el caso asmático.
* **Analogía terapéutica:** La acción del controlador PID representa conceptualmente una intervención broncodilatadora de rescate (como la administración de agonistas $\beta_2$-adrenérgicos inhalados, p. ej., salbutamol), cuyo mecanismo consiste en relajar el músculo liso bronquial para compensar el aumento de resistencia ($R_2$) y restaurar el flujo aéreo hacia los valores de un individuo sano.
* **Limitaciones del modelo:** El circuito RLC constituye una aproximación lineal concentrada de parámetros constantes; en la fisiología real, la resistencia de las vías aéreas depende del volumen pulmonar y del flujo (no linealidad), y la acción farmacológica tiene tiempos de absorción y metabolización que difieren de un controlador matemático ideal.

---

