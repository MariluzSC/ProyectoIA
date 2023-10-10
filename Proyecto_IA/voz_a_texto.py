from google.cloud import speech
from google.oauth2 import service_account
import json
from tkinter import messagebox
import joblib
import pandas as pd
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from sklearn.metrics import  confusion_matrix, ConfusionMatrixDisplay
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def transcribe_speech(audio_file):
    credentials = service_account.Credentials.from_service_account_file("C:/Users/Belén/Documents/GitHub/Proyecto_IA/credentials.json")

    client = speech.SpeechClient(credentials=credentials)

    with open(audio_file, "rb") as audio_file:
        audio_data = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_data)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="es-ES"
    )

    response = client.recognize(config=config, audio=audio)

    recognized_text = ""
    for result in response.results:
        recognized_text += result.alternatives[0].transcript

    return recognized_text.lower()


def accion_tipo_cambio():
    messagebox.showinfo("Respuesta a Instrucción", "El tipo de cambio es Compra: 533,49 y Venta: 540,31")
    print("El tipo de cambio es Compra: 533,49 y Venta: 540,31")

def accion_capital_colombia():
    messagebox.showinfo("Respuesta a Instrucción", "La Capital de Colombia es Bogotá")
    print("La Capital de Colombia es Bogotá")

def accion_presidente_panama():
    messagebox.showinfo("Respuesta a Instrucción", "El presidente de Panamá es Laurentino Cortizo")
    print("El presidente de Panamá es Laurentino Cortizo")

def accion_colores_bandera_costa_rica():
    messagebox.showinfo("Respuesta a Instrucción", "Los colores de la bandera de Costa Rica son Blanco, Azul y Rojo")
    print("Los colores de la bandera de Costa Rica son Blanco, Azul y Rojo")

def accion_moneda_china():
    messagebox.showinfo("Respuesta a Instrucción", "La moneda de China es el Yua")
    print("La moneda de China es el Yuan")

def accion_comida_tipica_mexico():
    messagebox.showinfo("Respuesta a Instrucción", "La comida típica de Mexico es el mole, pozole y los tacos")
    print("La comida típica de Mexico es el mole, pozole y los tacos")

def algortimo_bitcoin():
    reg_cargado = joblib.load('bitcoin.pkl')
    # num = float(input("Digite Low: "))

    # precio_bitcoin = pd.DataFrame({'Low': [num]})
    # precio_bitcoin['prediccion'] = np.exp(reg_cargado.predict([[1, np.log(num)]]))
    # print(f"El precio total del bitcoin con un margen de error de 1% hacia arriba o hacia abajo es de {precio_bitcoin['prediccion'][0]}")
    def calcular_prediccion():
        try:
            num = float(entry_low.get())
            precio_bitcoin = pd.DataFrame({'Low': [num]})
            precio_bitcoin['prediccion'] = np.exp(reg_cargado.predict([[1, np.log(num)]]))
            prediccion = precio_bitcoin['prediccion'][0]
            mensaje = f"El precio total del bitcoin con un margen de error de 1% hacia arriba o hacia abajo es de {prediccion}"
            messagebox.showinfo("Predicción de precio de Bitcoin", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido para Low.")

    ventana = tk.Tk()
    ventana.title("Predicción de precio de Bitcoin")
    ancho_ventana = 150
    alto_ventana = 150
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
    # Crear un cuadro de entrada para Low
    label_low = tk.Label(ventana, text="Low:")
    label_low.pack()
    entry_low = tk.Entry(ventana)
    entry_low.pack()

    # Crear un botón para calcular la predicción
    boton_calcular = tk.Button(ventana, text="Calcular Predicción", command=calcular_prediccion)
    boton_calcular.pack()

    ventana.mainloop()

    # Configuración de la ventana principal
    

def algortimo_wine():
    def generar_matriz():
        reg_cargado = joblib.load('vino.pkl')

        cm_display = ConfusionMatrixDisplay(reg_cargado, display_labels=['0', '1'])

        # Genera la gráfica de la matriz de confusión
        fig, ax = plt.subplots(figsize=(8, 8))
        cm_display.plot(ax=ax)
        
        plt.show()

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Generar Matriz de Confusión")
    ancho_ventana = 200
    alto_ventana = 50
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}")

    # Crear un botón para generar la matriz de confusión
    boton_generar_matriz = tk.Button(ventana, text="Generar Matriz de Confusión", command=generar_matriz)
    boton_generar_matriz.pack()

    ventana.mainloop()    

def algortimo_avocado():
    # reg_cargado = joblib.load('avocado.pkl')

    # num = float(input("Digite Total Bags: "))

    # precio_avocado = pd.DataFrame({'Total Bags': [num]})
    # precio_avocado['prediccion'] = reg_cargado.predict([[1, (num)]])
    # print(f"El precio total del aguacate con un margen de error de 2% hacia arriba o hacia abajo es de {precio_avocado['prediccion'][0]}")

    def calcular_prediccion_avocado():
        try:
            num = float(entry_total_bags.get())
            precio_avocado = pd.DataFrame({'Total Bags': [num]})
            precio_avocado['prediccion'] = reg_cargado.predict([[1, num]])
            prediccion = precio_avocado['prediccion'][0]
            mensaje = f"El precio total del aguacate con un margen de error de 2% hacia arriba o hacia abajo es de {prediccion}"
            messagebox.showinfo("Predicción de precio de Aguacate", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido para Total Bags.")
    # Cargar el modelo para aguacate
    reg_cargado = joblib.load('avocado.pkl')

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Predicción de precio de Aguacate")
    ancho_ventana = 150
    alto_ventana = 150
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}")

    # Crear un cuadro de entrada para Total Bags
    label_total_bags = tk.Label(ventana, text="Total Bags:")
    label_total_bags.pack()
    entry_total_bags = tk.Entry(ventana)
    entry_total_bags.pack()

    # Crear un botón para calcular la predicción
    boton_calcular_avocado = tk.Button(ventana, text="Calcular Predicción", command=calcular_prediccion_avocado)
    boton_calcular_avocado.pack()

    ventana.mainloop()


def algortimo_car():
    # reg_cargado = joblib.load('car.pkl')

    # num = float(input("Digite Selling_Price: "))

    # precio_car = pd.DataFrame({'Selling_Price': [num]})
    # precio_car['prediccion'] = reg_cargado.predict([[1,  np.log(num)]])
    # print(f"El precio total de automóvil con un margen de error de 23% hacia arriba o hacia abajo es de {precio_car['prediccion'][0]}")
    def calcular_prediccion_car():
        try:
            num = float(entry_selling_price.get())
            precio_car = pd.DataFrame({'Selling_Price': [num]})
            precio_car['prediccion'] = reg_cargado.predict([[1, np.log(num)]])
            prediccion = precio_car['prediccion'][0]
            mensaje = f"El precio total de automóvil con un margen de error de 23% hacia arriba o hacia abajo es de {prediccion}"
            messagebox.showinfo("Predicción de precio de Automóvil", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido para Selling_Price.")

    # Cargar el modelo para automóvil
    reg_cargado = joblib.load('car.pkl')

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Predicción de precio de Automóvil")
    ancho_ventana = 150
    alto_ventana = 150
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}")

    # Crear un cuadro de entrada para Selling_Price
    label_selling_price = tk.Label(ventana, text="Selling_Price:")
    label_selling_price.pack()
    entry_selling_price = tk.Entry(ventana)
    entry_selling_price.pack()

    # Crear un botón para calcular la predicción
    boton_calcular_car = tk.Button(ventana, text="Calcular Predicción", command=calcular_prediccion_car)
    boton_calcular_car.pack()

    ventana.mainloop()
def algortimo_bodyfat():
    # reg_cargado = joblib.load('bodyfat.pkl')

    # num = float(input("Digite Hip: "))

    # bodyfat_patient = pd.DataFrame({'Hip': [num]})
    # bodyfat_patient['prediccion'] = reg_cargado.predict([[1,  np.log(num)]])
    # print(f"La masa corporal del paciente con un margen de error de 98% hacia arriba o hacia abajo es de {bodyfat_patient['prediccion'][0]}")

    def calcular_prediccion_bodyfat():
        try:
            num = float(entry_hip.get())
            bodyfat_patient = pd.DataFrame({'Hip': [num]})
            bodyfat_patient['prediccion'] = reg_cargado.predict([[1, num]])
            prediccion = bodyfat_patient['prediccion'][0]
            mensaje = f"La masa corporal del paciente con un margen de error de 98% hacia arriba o hacia abajo es de {prediccion}"
            messagebox.showinfo("Predicción de masa corporal", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido para Hip.")

    # Cargar el modelo para la estimación de masa corporal
    reg_cargado = joblib.load('bodyfat.pkl')

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Predicción de masa corporal del paciente")
    ancho_ventana = 150
    alto_ventana = 150
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}")

    # Crear un cuadro de entrada para Hip
    label_hip = tk.Label(ventana, text="Hip:")
    label_hip.pack()
    entry_hip = tk.Entry(ventana)
    entry_hip.pack()

    # Crear un botón para calcular la predicción
    boton_calcular_bodyfat = tk.Button(ventana, text="Calcular Predicción", command=calcular_prediccion_bodyfat)
    boton_calcular_bodyfat.pack()

    ventana.mainloop()
def modelo_tarifas_viajes():
    try:
        # Carga el modelo previamente entrenado
        modelo = joblib.load('bicicleta.pkl')

        #Solicitar características
        distancia = int(input("Distancia: "))
        propina = int(input("Propina: "))
        
        variables = [[distancia, propina]]

        # Realiza la predicción utilizando el modelo
        precio_predicho = modelo.predict(variables)

        mensaje = f"La tarifa predicha es: ${precio_predicho[0]:.2f}"
        print(mensaje)

    except Exception as e:
        # En caso de error, maneja la excepción
        print("Error en la predicción:", str(e))
        return None

def modelo_inventario():
    try:
        # Cargar el modelo
        modelo = joblib.load('inventario.pkl')

        # Solicitar características al usuario
        store = int(input("Ingresa el ID de la tienda: "))
        item = int(input("Ingresa el ID del artículo: "))
        month = int(input("Ingresa el mes: "))
        day_of_week = int(input("Ingresa el día de la semana: "))

        # Preparar las características en un formato adecuado para el modelo
        caracteristicas = [[store, item, month, day_of_week]]

        # Realizar la predicción con el modelo
        precio_predicho = modelo.predict(caracteristicas)

        mensaje = f"La cantidad de inventario predicha es: ${precio_predicho[0]:.2f}"
        print(mensaje)

    except Exception as e:
        mensaje_error = "Ocurrió un error al realizar la predicción. Verifica que el modelo y los datos sean correctos."
        print("Error en la predicción:", str(e))

def modelo_cerebrovascular():
    try:
        # Cargar el modelo
        modelo = joblib.load('cerebrovascular.pkl')

        # Solicitar características al usuario
        avg_glucose_level = int(input("Ingresa el nivel de glucosa: "))
        bmi = int(input("Ingresa el IMC: "))
        age = int(input("Ingresa la edad: "))

        # Preparar las características en un formato adecuado para el modelo
        caracteristicas = [[avg_glucose_level, bmi, age]]

        # Realizar la predicción con el modelo
        precio_predicho = modelo.predict(caracteristicas)

        mensaje = f"Tendrá un accidente cerebrovascular: ${precio_predicho[0]:.2f}"
        print(mensaje)

    except Exception as e:
        mensaje_error = "Ocurrió un error al realizar la predicción. Verifica que el modelo y los datos sean correctos."
        print("Error en la predicción:", str(e))

def modelo_cirrosis():
    try:
        # Cargar el modelo
        modelo = joblib.load('cirrosis.pkl')

        # Solicitar características al usuario

        N_Days = int(input("dias sin ir al hospital: "))
        Bilirubin = int(input("Bilirubina: "))
        id = int(input("ID: "))
        Copper = int(input("Cobre: "))
        Cholesterol= int(input("Colesterol: "))
        Prothrombin= int(input("Prothrombin: "))
        SGOT= int(input("SGOT: "))
        Alk_Phos= int(input("Alk_Phos: "))
        Age= int(input("Edad: "))
        Tryglicerides= int(input("Tryglicerides: "))


        # Preparar las características en un formato adecuado para el modelo
        caracteristicas = [[N_Days, Bilirubin, id, Copper,Cholesterol,Prothrombin,SGOT,Alk_Phos,Age,Tryglicerides]]

        # Realizar la predicción con el modelo
        precio_predicho = modelo.predict(caracteristicas)

        mensaje = f"Tipo de cirrosis: ${precio_predicho[0]:.2f}"
        print(mensaje)

    except Exception as e:
        mensaje_error = "Ocurrió un error al realizar la predicción. Verifica que el modelo y los datos sean correctos."
        print("Error en la predicción:", str(e))

def modelo_obesidad():
    try:
        # Cargar el modelo
        modelo = joblib.load('obesidad.pkl')

        # Solicitar características al usuario
        Density = int(input("Densidad: "))
        Weight = int(input("Peso: "))
        Knee = int(input("Medida de rodilla: "))


        # Preparar las características en un formato adecuado para el modelo
        caracteristicas = [[Density, Weight, Knee]]

        # Realizar la predicción con el modelo
        precio_predicho = modelo.predict(caracteristicas)

        mensaje = f"El calculo de la obesidad del paciente es: ${precio_predicho[0]:.2f}"
        print(mensaje)

    except Exception as e:
        mensaje_error = "Ocurrió un error al realizar la predicción. Verifica que el modelo y los datos sean correctos."
        print("Error en la predicción:", str(e))
        

if __name__ == "__main__":
    try:
        # Obtener el texto reconocido del audio
        texto_reconocido = transcribe_speech('captura_audio.wav')

        print(texto_reconocido)
        # Comandos y acciones asociadas
        comandos_acciones = {
            "tipo de cambio para mañana": accion_tipo_cambio,
            "capital de colombia": accion_capital_colombia,
            "presidente de panamá": accion_presidente_panama,
            "colores de la bandera de costa rica": accion_colores_bandera_costa_rica,
            "moneda de china": accion_moneda_china,
            "comida típica de méxico": accion_comida_tipica_mexico,
            "modelo criptomoneda": algortimo_bitcoin,
            "modelo vino": algortimo_wine,
            "modelo aguacate": algortimo_avocado,
            "modelo carro": algortimo_car,
            "modelo masa muscular": algortimo_bodyfat,
            "modelo inventario": modelo_inventario,
            "modelo cerebrovascular": modelo_cerebrovascular,
            "modelo cirrosis": modelo_cirrosis,
            "modelo obesidad": modelo_obesidad,
            "modelo tarifas de viajes": modelo_tarifas_viajes
            # Puedes agregar más comandos y acciones aquí
        }

        # Ejecutar la acción asociada al comando
        if texto_reconocido in comandos_acciones:
            comandos_acciones[texto_reconocido]()
        else:
            messagebox.showinfo("Comando desconocido", "Comando no reconocido:", texto_reconocido)
            print("Comando no reconocido:", texto_reconocido)

    except Exception as e:
        messagebox.showinfo("Error", "Se produjo un error:")
        print("Se produjo un error:", str(e))
