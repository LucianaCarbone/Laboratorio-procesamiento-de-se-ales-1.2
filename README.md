# Laboratorio-procesamiento-de-se-ales-1.2

## Objetivo de la práctica
Analizar estadísticamente una señal fisiológica, calcular sus principales parámetros descriptivos, y comparar los resultados entre señales capturadas con hardware, aplicando también el concepto de relación señal-ruido.

## Procedimiento
### Parte A
1. **Descarga de señal:** Se obtuvo una señal fisiologica de ECG de la base de datos [PhysioNet – MIMIC-IV-ECG: Diagnostic Electrocardiogram Matched Subset] (https://www.physionet.org/content/mimic-iv-ecg/1.0/files/p1860/p18606031/s43496857/43496857.dat). Se uso la señal del registro '43496857' del conjunto **MIMIC-IV-ECG: Diagnostic Electrocardiogram Matched Subset**. En este se encuentran multiples derivaciones ECG, muestreadas a 200 Hz.
2. **Visualización:** Se graficó la señal en el dominio del tiempo
3. **Cálculo de estadísticos descriptivos:**
   - Media: -0.000895
   - Mediana: -0.04
   - Desviación estándar: 0.14938934838361834
   - Coeficiente de variación: -16691.55%
   - Curtosis: 13.133217777426063
4. **Histograma y función de probabilidad:** Se graficó el histograma y se estimó la función de densidad de probabilidad.

<img width="611" height="886" alt="image" src="https://github.com/user-attachments/assets/e33a759f-4540-4345-909a-4583ebda6d47" />

             Imagen 1. Diagrama de flujo parte A

### Parte B
1. **Generación:** Se generó una señal fisiológica con auda del generador de señales biológicas.
2. **Captura:** Se capturó la señal utilizando un microcontrolador STM32 blackpill con su función ADC.
3. **Conversión:** Los datos ADC se transformarorn a voltios.
4. **Análisis estadístico:** Se repitieron los cálculos de la parte A.
   - Media: 0.8804996336996337 
   - Mediana: 0.8356776556776556 
   - Desviación estándar: 0.4758191679603716 
   - Coeficiente de variación: 54.04%
   - Curtosis: 9.784939579218962
5. **Histograma y función de probabilidad:** Nuevamente, se graficó el histograma y se estimó la función de densidad de probabilidad.
   
  <img width="416" height="851" alt="image" src="https://github.com/user-attachments/assets/c89daba3-66ed-42f4-91e2-1e506448260e" />
  
             Imagen 2. Diagrama de flujo parte B

### Parte C
1. **Ruido:** Se contaminó la señal con ruido Gaussiano, ruido por impulsos y ruido tipo artefacto.
2. Se calculó el SNR para cada caso:
   - Ruido Gaussiano: 20.17 dB
   - Ruiedo por impulsos: 14.30 dB
   - Ruido tipo artefacto: 12.38 dB

El ruido que dio una señal mucho más limpia y que dio con menos ruido agregado fue el Gaussiano, el que genero más degradación en la señal fue el ruido de impulso. Esto indica que las señales ECG suelen verse afectadas por artefactos de movimiento o impulsos que por ruido de tipo blanco.

  <img width="376" height="791" alt="image" src="https://github.com/user-attachments/assets/786c11c2-4e4e-49ec-8b00-2dabcda0e0b2" />
  
                Imagen 3. Diagrama de flujo parte C

## Resultados
| Parámetro       | Señal descargada | Señal capturada |
|-----------------|------------------|-----------------|
| Media (V)       | -0.000895        | 0.8804996336996 |
| Mediana (V)     | -0.04            | 0.8356776556776 |
| Desv. estándar (V) | 0.1493893483  | 0.4758191679603 |
| Coef. variacion |  -16691.55%      | 54.04%          |
| Curtosis        | 13.133217777426  | 9.7849395792189 |

La señal real de ECG tiene una media y mediana cercanas a cero, lo cual es normal porque el voltaje suele oscilar alrededor de la línea base (0 V). En cambio, la señal simulada muestra valores mucho más altos (≈ 0.88 V de media), lo que indica un desplazamiento de nivel DC. Esto podría deberse a problemas de calibración del convertidor analógico-digital, al diseño de la señal simulada o a un error en la patura.

La señal real tiene una desviación estándar baja (≈ 0.15 V), lo que indica que sus valores de voltaje son más estables. En cambio, la señal simulada muestra mayor dispersión (≈ 0.48 V). El coeficiente de variación en la señal real es muy alto y negativo porque su media es casi cero, lo que distorsiona el cálculo. En la señal simulada, el CV (54.04%) sí refleja bien la variabilidad.

La señal real tiene una curtosis muy alta (≈ 13.13), lo que indica que su forma es más puntiaguda y con colas pesadas, es decir, hay más valores extremos como los picos del QRS en el ECG. La señal simulada también tiene curtosis alta (≈ 9.78), pero es menor, lo que sugiere que sus picos son menos pronunciados. La señal real representa mejor los picos fisiológicos típicos del corazón, mientras que la simulada es más suave.

## Gráficas
### Graficas ECG
**ECG descargado:**
<img src="https://github.com/user-attachments/assets/d0d94e19-1825-4428-9831-e17861b22302" width="567" height="455" />

                                Imagen 4. ECG desacargado 

**ECG capturado:**
<img src="https://github.com/user-attachments/assets/50ac1d9b-71d4-4b7b-8df3-ce55fcefa5a5" width="567" height="455" />

                               Imagen 5. ECG capturado 

**Ruido en señal ECG:**
<img src="https://github.com/user-attachments/assets/5f253e6c-822a-4cab-b34b-89f34bef5576" width="1189" height="592" />

                              Imagen 6. Ruido de señal ECG

---

### Histogramas

**Histograma ECG descargado:**
<img width="554" height="455" alt="histo_cap" src="https://github.com/user-attachments/assets/cd5b847b-63a9-44e1-ba9e-f49a0b130851" />

                           Imagen 7. Histograma ECG descargado 

**Histograma ECG capturado:**
<img src="https://github.com/user-attachments/assets/6e147507-a1a9-4919-bef2-629968042c05" width="593" height="455" />

                          Imagen 8. Histograma ECG capturado  

## Por:
 - Luciana Carbone Calderón (@LucianaCarbone)
 - Ana María Sanchez Beltran (@estanamsanchezb-netizen)
 - Marya Kathalina Prieto Martinez (@Katha2025)
