import secrets
import json
from datetime import datetime

class NumerosLoteria:
    def __init__(self):
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.numeros_principales = None
        self.estrellas = None
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        try:
            with open("numeros_loteria.json", "r") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {"duplicados": []}

    def generar_numeros(self):
        self.numeros_principales = [secrets.randbelow(50) + 1 for _ in range(5)]
        self.estrellas = [secrets.randbelow(12) + 1 for _ in range(2)]
        self.numeros_principales = sorted(set(self.numeros_principales))
        self.estrellas = sorted(set(self.estrellas))
        while len(self.numeros_principales) < 5:
            self.numeros_principales.append(secrets.randbelow(50) + 1)
            self.numeros_principales = sorted(set(self.numeros_principales))
        while len(self.estrellas) < 2:
            self.estrellas.append(secrets.randbelow(12) + 1)
            self.estrellas = sorted(set(self.estrellas))

    def verificar_y_guardar(self):
        clave = {"numeros_principales": self.numeros_principales, "estrellas": self.estrellas}
        for entry in self.datos.get("duplicados", []):
            if entry["numeros_principales"] == self.numeros_principales and entry["estrellas"] == self.estrellas:
                entry["Veces generado"] = str(int(entry["Veces generado"]) + 1)
                break
        else:
            self.datos[self.fecha_actual] = clave
            self.datos["duplicados"].append({**clave, "Veces generado": "1"})

        with open("numeros_loteria.json", "w") as archivo:
            json.dump(self.datos, archivo, indent=4)

# Ejemplo de uso de la clase
loteria = NumerosLoteria()
loteria.generar_numeros()
print(f"Números de lotería generados - 5 del 1 al 50: {loteria.numeros_principales}, 2 del 1 al 12: {loteria.estrellas}")
loteria.verificar_y_guardar()