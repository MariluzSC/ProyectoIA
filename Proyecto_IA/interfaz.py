import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def capturar_camara():
    # Implementa la lógica para capturar desde la cámara
    #messagebox.showinfo("Capturar Cámara", "Capturando desde la cámara")
    subprocess.run(["python", "emociones.py"])

def capturar_voz():
    # Implementa la lógica para capturar voz
    subprocess.run(["python", "capturar_voz.py"])  # Llama al script capturar_voz.py
    messagebox.showinfo("Audio terminado", "Captura de voz finalizada") 
    subprocess.run(["python", "voz_a_texto.py"])  # Llama al script transcribe_audio.py

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Captura")

# Ajustar el tamaño de la ventana principal
ancho_ventana = 400
alto_ventana = 250
root.geometry(f"{ancho_ventana}x{alto_ventana}")

# Configurar el fondo con una imagen
background_image = tk.PhotoImage(file="ia1.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Crear una etiqueta para el título
titulo_label = tk.Label(root, text="Proyecto de IA", font=("Roboto", 16, "bold"))
titulo_label.pack(pady=(0, 20))
titulo_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Botón para capturar desde la cámara
boton_camara = tk.Button(root, text="Capturar Cámara", command=capturar_camara)
boton_camara.pack(side=tk.LEFT, padx=20)

# Botón para capturar voz
boton_voz = tk.Button(root, text="Capturar Voz", command=capturar_voz)
boton_voz.pack(side=tk.RIGHT, padx=20)

def on_closing():
    if os.path.exists('captura_audio.wav'):
        os.remove('captura_audio.wav')
    if os.path.exists('captura_camara.png'):
        os.remove('captura_camara.png')
    root.destroy()

# Configurar la acción al cerrar la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
