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
  
### Parte C
1. **Ruido:** Se contaminó la señal con ruido Gaussiano, ruido por impulsos y ruido tipo artefacto.
2. Se calculó el SNR para cada caso:
   - Ruido Gaussiano: 20.17 dB
   - Ruiedo por impulsos: 14.30 dB
   - Ruido tipo artefacto: 12.38 dB
El ruido que dio una señal mucho más limpia y que dio con menos ruido agregado fue el Gaussiano, el que genero más degradación en la señal fue el ruido de impulso
  
## Resultados
| Parámetro       | Señal descargada | Señal capturada |
|-----------------|------------------|-----------------|
| Media (V)       | -0.000895        | 0.8804996336996 |
| Mediana (V)     | -0.04            | 0.8356776556776 |
| Desv. estándar (V) | 0.1493893483  | 0.4758191679603 |
| Coef. variacion |  -16691.55%      | 54.04%          |
| Curtosis        | 13.133217777426  | 9.7849395792189 |

## Gráficas
###Graficas ECG
<img width="567" height="455" alt="grafica_ecg_1" src="https://github.com/user-attachments/assets/d0d94e19-1825-4428-9831-e17861b22302" />
Grafica ECG descargado.
<img width="567" height="455" alt="grafica_ecg_2" src="https://github.com/user-attachments/assets/50ac1d9b-71d4-4b7b-8df3-ce55fcefa5a5" />
Gráfica ECG capturado.
<img width="1189" height="592" alt="ecg_ruidos" src="https://github.com/user-attachments/assets/5f253e6c-822a-4cab-b34b-89f34bef5576" />
Gráficas de los ruidos.

###Histogramas
<img width="1189" height="592" alt="ecg_ruidos" sr<img width="554" height="455" alt="histo_cap" src="https://github.com/user-attachments/assets/4db0ced5-f9d3-49ec-b6fd-a63b617ca7be" />
c="https://github.com/user-attachments/assets/5f253e6c-822a-4cab-b34b-89f34bef5576" />
Histograma ECG descargado.
<img width="593" height="455" alt="lab 1 4" src="https://github.com/user-attachments/assets/6e147507-a1a9-4919-bef2-629968042c05" />
Histograma ECG capturado.

## Por:
 - Luciana Carbone Calderón (@LucianaCarbone)
 - Ana María Sanchez Beltran (@estanamsanchezb-netizen)
 - Marya Kathalina Prieto Martinez (@Katha2025)
