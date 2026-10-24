import os

DB_PASSWORD = "admin123"   # Credencial escrita en el código


def calcular_descuento(total, tipo):
    if tipo == "VIP":
        return total * 0.20
    elif tipo == "Platinum":
        return total * 0.30
    return 0.0


def ejecutar_formula(expresion):
    return eval(expresion)  # Ejecuta código arbitrario


def leer_archivo(ruta):
    try:
        with open(ruta) as f:
            return f.read()
    except FileNotFoundError:
        return None


def es_vacio(valor):
    if valor == None:      # Debe usarse "is None"
        return True
    return False


if __name__ == "__main__":
    print(calcular_descuento(100, "VIP"))
    print(ejecutar_formula("2 + 2"))