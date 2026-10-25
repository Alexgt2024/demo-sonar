from appdesarrollo import calcular_descuento, es_vacio, leer_archivo


def test_descuento_vip():
    assert calcular_descuento(100, "VIP") == 20.0


def test_descuento_platinum():
    assert calcular_descuento(100, "Platinum") == 30.0


def test_descuento_tipo_desconocido():
    assert calcular_descuento(100, "Otro") == 0.0


def test_leer_archivo_existente(tmp_path):
    archivo = tmp_path / "prueba.txt"
    archivo.write_text("contenido", encoding="utf-8")
    assert leer_archivo(str(archivo)) == "contenido"


def test_leer_archivo_inexistente(tmp_path):
    assert leer_archivo(str(tmp_path / "no_existe.txt")) is None


def test_es_vacio():
    assert es_vacio(None) is True
    assert es_vacio("dato") is False
