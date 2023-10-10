import cv2
import tkinter as tk
from tkinter import Label, Button, Frame, Listbox, Scrollbar, messagebox
import requests
import os
from dotenv import load_dotenv
from tkinter import ttk

# Función para capturar una imagen desde la cámara
def capturar_imagen():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captura.png", frame)
        cap.release()
        mostrar_imagen()
        analizar_button.config(state=tk.NORMAL)  # Habilitar el botón de analizar después de capturar la imagen

# Función para mostrar la imagen capturada en la pantalla principal
def mostrar_imagen():
    imagen = tk.PhotoImage(file="captura.png")
    img_label.config(image=imagen)
    img_label.image = imagen

# Función para analizar las emociones en la imagen y mostrarlas en un cuadro de mensaje
def analizar_emociones():
    with open("captura.png", 'rb') as f:
        files = {'image_file': ('captura.png', f)}
        payload = {
            'api_key': API_KEY,
            'api_secret': API_SECRET,
            'return_attributes': 'emotion',
        }
        response = requests.post(API_URL, data=payload, files=files)
        data = response.json()

        if 'faces' in data:
            emociones = data['faces'][0]['attributes']['emotion']
            mostrar_emociones(emociones)

# Función para mostrar las emociones en un cuadro de mensaje
def mostrar_emociones(emociones):
    emociones_str = "Emociones detectadas:\n"
    for emocion, valor in emociones.items():
        emociones_str += f"{emocion}: {valor}\n"

    messagebox.showinfo("Resultados de Emociones", emociones_str)

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las claves de API de Face++ desde las variables de entorno
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

if not API_KEY or not API_SECRET:
    raise ValueError("API_KEY y API_SECRET deben estar configurados en el archivo .env")

# URL de la API de Face++
API_URL = 'https://api-us.faceplusplus.com/facepp/v3/detect'

# Crear una ventana de Tkinter
root = tk.Tk()
root.title("Captura y Análisis de Emociones")
root.geometry("600x400")  # Cambiar el tamaño de la ventana principal

# Establecer el fondo de la ventana principal con un color sólido
root.configure(bg="lightblue")  # Cambiar el color de fondo según tus preferencias

# Crear un Frame para contener los botones
button_frame = Frame(root, bg="lightblue")
button_frame.pack(side=tk.TOP, pady=10)

# Botones con estilo
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", font=("Arial", 12))
capturar_button = ttk.Button(button_frame, text="Capturar Imagen", command=capturar_imagen)
analizar_button = ttk.Button(button_frame, text="Analizar Emociones", command=analizar_emociones, state=tk.DISABLED)
capturar_button.grid(row=0, column=0, padx=10)
analizar_button.grid(row=0, column=1, padx=10)

# Label para mostrar la imagen capturada
img_label = Label(root, bg="lightblue")
img_label.pack(side=tk.LEFT, padx=10)

# Ejecutar la interfaz de usuario
root.mainloop()
