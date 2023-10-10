import joblib
import pandas as pd
import numpy as np

def algortimo_bitcoin():
    reg_cargado = joblib.load('bitcoin.pkl')
    num = float(input("Digite Low: "))

    precio_bitcoin = pd.DataFrame({'Low': [num]})
    precio_bitcoin['prediccion'] = np.exp(reg_cargado.predict([[1, np.log(num)]]))
    print(f"El precio total del bitcoin con un margen de error de 1% hacia arriba o hacia abajo es de {precio_bitcoin['prediccion'][0]}")


def algortimo_wine():
    reg_cargado = joblib.load('wine.pkl')

    num = float(input("Digite Total Bags: "))

    precio_avocado = pd.DataFrame({'Total Bags': [num]})
    precio_avocado['prediccion'] = reg_cargado.predict([[1, (num)]])
    print(f"El precio total del aguacate con un margen de error de 2% hacia arriba o hacia abajo es de {precio_avocado['prediccion'][0]}")

def algortimo_avocado():
    reg_cargado = joblib.load('avocado.pkl')

    num = float(input("Digite Total Bags: "))

    precio_avocado = pd.DataFrame({'Total Bags': [num]})
    precio_avocado['prediccion'] = reg_cargado.predict([[1, (num)]])
    print(f"El precio total del aguacate con un margen de error de 2% hacia arriba o hacia abajo es de {precio_avocado['prediccion'][0]}")

def algortimo_car():
    reg_cargado = joblib.load('car.pkl')

    num = float(input("Digite Selling_Price: "))

    precio_car = pd.DataFrame({'Selling_Price': [num]})
    precio_car['prediccion'] = reg_cargado.predict([[1,  np.log(num)]])
    print(f"El precio total de automóvil con un margen de error de 23% hacia arriba o hacia abajo es de {precio_car['prediccion'][0]}")

def algortimo_bodyfat():
    reg_cargado = joblib.load('bodyfat.pkl')

    num = float(input("Digite Hip: "))

    bodyfat_patient = pd.DataFrame({'Hip': [num]})
    bodyfat_patient['prediccion'] = reg_cargado.predict([[1,  np.log(num)]])
    print(f"La masa corporal del paciente con un margen de error de 98% hacia arriba o hacia abajo es de {bodyfat_patient['prediccion'][0]}")
