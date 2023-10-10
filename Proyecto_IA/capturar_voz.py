import pyaudio
import numpy as np
import wave
import os
import threading
import time
from threading import Event
from tkinter import messagebox

# Bandera para indicar si la captura debe detenerse
captura_activa = True

# Evento para señalar cuando la captura está completada
capture_completed_event = Event()

# Función para detener la captura
def detener_captura():
    global captura_activa
    captura_activa = False

# Función para capturar la voz
def capturar_voz():
    global captura_activa

    if os.path.exists('captura_audio.wav'):
        os.remove('captura_audio.wav')

    # Configuración de PyAudio
    FORMAT = pyaudio.paInt16  # Formato de la muestra de audio
    CHANNELS = 1  # Mono: 1 canal de audio
    RATE = 44100  # Tasa de muestreo en Hz
    CHUNK = 1024  # Tamaño del bloque de audio a leer
    THRESHOLD_ENERGY = 5000  # Umbral de energía para detectar ruido (ajusta según sea necesario)
    DURACION_CAPTURA = 5  # Duración de la captura en segundos

    # Inicializar PyAudio
    audio = pyaudio.PyAudio()

    # Abrir el flujo de audio desde el micrófono
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    messagebox.showinfo("Comenzar a Grabar", "Capturar voz en tiempo real durante 5 segundos.")  
    frames = []
    try:
        start_time = time.time()  # Tiempo de inicio
        while time.time() - start_time < DURACION_CAPTURA and captura_activa:
            audio_data = stream.read(CHUNK, exception_on_overflow=False)
            
            # Convertir los datos de audio en un array NumPy
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
            
            # Calcular la energía de la señal de audio
            energy = np.sum(audio_array**2) / len(audio_array)

            frames.append(audio_data)

        # Guardar el audio en un archivo .wav
        audio_wave = wave.open('captura_audio.wav', 'wb')
        audio_wave.setnchannels(1)  # Mono
        audio_wave.setsampwidth(audio.get_sample_size(FORMAT))  # Ancho de muestra
        audio_wave.setframerate(RATE)
        audio_wave.writeframes(b''.join(frames))  # Escribir todos los fotogramas acumulados
        audio_wave.close()

        # Señalar que la captura está completada
        capture_completed_event.set()

    except KeyboardInterrupt:
        print("Captura de voz detenida.")

    # Detener y cerrar el flujo de audio
    stream.stop_stream()
    stream.close()

    # Cerrar PyAudio
    audio.terminate()

# Iniciar la captura en un hilo separado
audio_thread = threading.Thread(target=capturar_voz)
audio_thread.start()
