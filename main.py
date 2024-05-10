import secrets
import json
from datetime import datetime

class NumerosLoteria:
    def __init__(self):
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        try:
            with open("numeros_loteria.json", "r") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {}

    def generar_numeros_unicos(self, cantidad, rango):
        return sorted(secrets.SystemRandom().sample(range(1, rango + 1), cantidad))

    def generar_numeros(self):
        self.numeros_principales = self.generar_numeros_unicos(5, 50)
        self.estrellas = self.generar_numeros_unicos(2, 12)

    def verificar_y_guardar(self):
        clave = tuple(self.numeros_principales + self.estrellas)
        clave_str = f"{clave}"

        if clave_str in self.datos:
            self.datos["duplicados"] = self.datos.get("duplicados", {})
            self.datos["duplicados"][clave_str] = self.datos["duplicados"].get(clave_str, 0) + 1
        else:
            self.datos[clave_str] = {
                "fecha": self.fecha_actual,
                "numeros_principales": self.numeros_principales,
                "estrellas": self.estrellas
            }

        with open("numeros_loteria.json", "w") as archivo:
            json.dump(self.datos, archivo, indent=4)

# Ejemplo de uso de la clase
loteria = NumerosLoteria()
loteria.generar_numeros()
print(f"Números de lotería generados - 5 del 1 al 50: {loteria.numeros_principales}, 2 del 1 al 12: {loteria.estrellas}")
loteria.verificar_y_guardar()
