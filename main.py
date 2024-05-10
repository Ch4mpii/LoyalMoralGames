import random
import json
from datetime import datetime


class NumerosLoteria:

    def __init__(self):
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.numeros_de_1_a_50 = None
        self.numeros_de_1_a_12 = None

    def generar_numeros(self):
        self.numeros_de_1_a_50 = random.sample(range(
            1, 51), 5)  # Seleccionar 5 números únicos del 1 al 50
        self.numeros_de_1_a_12 = random.sample(range(
            1, 13), 2)  # Seleccionar 2 números únicos del 1 al 12

    def guardar_en_json(self):
        datos = {
            self.fecha_actual: {
                "numeros_de_1_a_50": self.numeros_de_1_a_50,
                "numeros_de_1_a_12": self.numeros_de_1_a_12
            }
        }
        try:
            with open("numeros_loteria.json", "r+") as archivo:
                datos_archivo = json.load(archivo)
                datos_archivo.update(datos)
                archivo.seek(0)
                json.dump(datos_archivo, archivo, indent=4)
        except FileNotFoundError:
            with open("numeros_loteria.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)


# Ejemplo de uso de la clase
loteria = NumerosLoteria()
loteria.generar_numeros()
print(
    f"Números de lotería generados - 5 del 1 al 50: {loteria.numeros_de_1_a_50}, 2 del 1 al 12: {loteria.numeros_de_1_a_12}"
)
loteria.guardar_en_json()
