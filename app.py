import os

DB_PASSWORD = "admin123"   # Credencial escrita en el código


def calcular_descuento(total, tipo):
    resultado = 0
    temporal = 99          # Variable que nunca se usa
    if tipo == "VIP":
        resultado = total * 0.20
    elif tipo == "VIP":    # Condición duplicada: nunca se ejecuta
        resultado = total * 0.30
    return resultado


def ejecutar_formula(expresion):
    return eval(expresion)  # Ejecuta código arbitrario


def leer_archivo(ruta):
    try:
        with open(ruta) as f:
            return f.read()
    except:                # Captura cualquier excepción sin distinguir
        pass


def es_vacio(valor):
    if valor == None:      # Debe usarse "is None"
        return True
    return False


if __name__ == "__main__":
    print(calcular_descuento(100, "VIP"))
    print(ejecutar_formula("2 + 2"))