import os

DB_PASSWORD = "admin123"   # Credencial escrita en el código


def calcular_descuento(total, tipo):
    if tipo == "VIP":
        return total * 0.20
    elif tipo == "Platinum":
        return total * 0.30
    elif tipo == "Gold":
        return total * 0.15
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
    print("Estudiante: Ronal Torres")
    print("Carné: 6990-098377")
    print("Curso: Aseguramiento de la Calidad de Software")
    print("Sección: A")
    print()

    print("Descuento Gold:", calcular_descuento(100, "Gold"))
    print(ejecutar_formula("2 + 2"))