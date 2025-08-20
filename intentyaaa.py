import serial
import threading
import csv
import time
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import os
import platform
import subprocess
import numpy as np
# Conexión serial: cambia aquí el puerto según tu PC
serial_port = serial.Serial('COM5', 115200, timeout=1)

# Buffers circulares para los datos
MAX_DATOS = 100
valores_adc = deque([0] * MAX_DATOS, maxlen=MAX_DATOS)
tiempos = deque([i * 0.001 for i in range(MAX_DATOS)], maxlen=MAX_DATOS)
valores_gaus = deque([0] * MAX_DATOS, maxlen=MAX_DATOS)
valores_artefac = deque([0] * MAX_DATOS, maxlen=MAX_DATOS)
valores_impul = deque([0] * MAX_DATOS, maxlen=MAX_DATOS)
# Flags de control
programa_activo = True
recolectando = True

# Hilo que escucha el puerto serie
def recibir_serial():
    global programa_activo, recolectando
    while programa_activo:
        if recolectando and serial_port.in_waiting > 0:
            try:
                linea = serial_port.readline()
                if linea:
                    texto = linea.decode('utf-8', errors='ignore').strip()
                    try:
                        numero = float(texto)
                        if 0 <= numero <= 4095:
                            valores_adc.append(numero)
                            tiempos.append(tiempos[-1] + 0.001)
                    except ValueError:
                        print(f"Dato inválido: {texto}")
            except Exception as error:
                print(f"Fallo al leer: {error}")

# Guardar datos en un CSV y abrirlo automáticamente
def exportar_csv():
    global recolectando
    recolectando = False
    time.sleep(0.1)

    nombre_archivo = "lectura_adc.csv"
    with open(nombre_archivo, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Tiempo ", " ADC","G", "A", "I"])
        for t, v,g,a,i in zip(tiempos, valores_adc, valores_gaus,valores_artefac,valores_impul):
            escritor.writerow([f"{t:.3f}", f"{v:.2f}",f"{g:.2f}",f"{a:.2f}",f"{i:.2f}"])

    print(f"Archivo guardado: {nombre_archivo}")

    if platform.system() == "Windows":
        os.startfile(nombre_archivo)
    elif platform.system() == "Darwin":
        subprocess.call(["open", nombre_archivo])
    else:
        subprocess.call(["xdg-open", nombre_archivo])

    recolectando = True

# Salida limpia del programa
def salir():
    global programa_activo
    programa_activo = False
    exportar_csv()
    ventana.destroy()

# Actualiza la gráfica cada cierto intervalo
def graficar_en_vivo(frame):
    plt.cla()
    plt.plot(tiempos, valores_adc, color='red', label="ADC")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor ADC")
    plt.title("Lectura ADC")
    plt.ylim([0, 5000])
    plt.grid(True)
    plt.legend()
         # Copiar datos actuales
    datos_originales = np.array(valores_adc)
    
    # Generar ruido gaussiano suave
    mu = 0       # media
    sigma = 100  # desviación estándar baja
    ruido = np.random.normal(mu, sigma, len(datos_originales))
    # Señal con ruido
    datos_con_ruido = datos_originales + ruido

    plt.plot(tiempos, datos_con_ruido, color='pink', label="ADC con ruido")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor ADC")
    plt.title("Lectura ADC")
    plt.ylim([0, 5000])
    plt.grid(True)
    plt.legend()
 

    # Generar ruido artefacto
    frecuencia = 5   # Hz
    amplitud = 300   # amplitud del artefacto
    artefacto = amplitud * np.sin(2 * np.pi * frecuencia * np.array(tiempos))
    datos_artefacto = datos_originales + artefacto
    # Señal con ruido
    plt.plot(tiempos,  datos_artefacto, color='blue', label = "ADC con artefacto")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor ADC")
    plt.title("Lectura ADC")
    plt.ylim([0, 5000])
    plt.grid(True)
    plt.legend()

        
     # Generar ruido impulso
    # Generar ruido tipo impulso (basado en tiempo)
    amplitud_impulso = 1000  # altura de los impulsos
    probabilidad = 0.05      # 5% de que aparezca un impulso en cada muestra
    
    # Creamos una máscara de impulsos (0 normalmente, 1 aleatoriamente con cierta probabilidad)
    mascara_impulso = np.random.choice([0, 1], size=len(tiempos), p=[1-probabilidad, probabilidad])
    
    # Multiplicamos por una amplitud aleatoria positiva o negativa
    ruido_impulso = mascara_impulso * np.random.choice([amplitud_impulso, -amplitud_impulso], size=len(tiempos))

    # Señal con impulsos
    datos_impulso = datos_originales + ruido_impulso
    
    plt.plot(tiempos,  datos_impulso, color='green', label = "ADC con impulso")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor ADC")
    plt.title("Lectura ADC")
    plt.ylim([0, 5000])
    plt.grid(True)
    plt.legend()
    # === ACTUALIZAR LOS BUFFERS DE RUIDO ===
    for g, a, i in zip(datos_con_ruido, datos_artefacto, datos_impulso):
        valores_gaus.append(g)
        valores_artefac.append(a)
        valores_impul.append(i)

    
# Iniciar hilo de lectura serial
hilo_datos = threading.Thread(target=recibir_serial, daemon=True)
hilo_datos.start()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Monitor Serial ADC")
ventana.geometry("600x300")
ventana.configure(bg="white")
ventana.protocol("WM_DELETE_WINDOW", salir)

# Texto descriptivo
texto_info = tk.Label(ventana, text="Haz clic para guardar los registros",
                      bg="white", font=("Times New Roman", 14, "bold"))
texto_info.pack(pady=30)

# Botón principal
btn_guardar = tk.Button(ventana, text="GUARDAR :)", bg="pink", fg="white",
                        font=("Times New Roman", 20, "bold"), height=2, width=20, command=exportar_csv)
btn_guardar.pack()

# Mostrar gráfico en otro hilo
def lanzar_grafico():
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, graficar_en_vivo, interval=100)
    plt.show()

hilo_grafico = threading.Thread(target=lanzar_grafico, daemon=True)
hilo_grafico.start()

# Iniciar GUI
ventana.mainloop()
