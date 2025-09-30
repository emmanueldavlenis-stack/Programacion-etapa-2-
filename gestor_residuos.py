from menu_utils import separator, title_style, default_text, options, INPUT_CHAR
from enum import Enum

tipos_residuos = {1: "Organico", 2:"Inorganico", 3: "Peligroso", 4:"Reciclable"}
metodos_tratamiento = {1: "Reciclaje", 2: "Incineración", 3: "Compostaje", 4: "Relleno sanitario"}

class Residuo():
    def __init__(self, nombre, tipo, tratamiento, peso, recuperacion):
        self.nombre = nombre
        self.tipo = tipo
        self.tratamiento = tratamiento,
        self.peso = peso
        self.recuperacion = recuperacion

class GestorResiduos:
    def __init__(self):
        self.residuos: list[Residuo] = []

    def registrar_residuo(self):
        print(separator())
        print(title_style("Registrar residuo individual"))
        print(separator())
        print(default_text("Nombre:"))
        nombre = input(INPUT_CHAR + " ")
        print(default_text("Tipo de residuo:"))
        tipo = options(*tipos_residuos.values())
        print(default_text("Método de tratamiento:"))
        tratamiento = options(*metodos_tratamiento.values())
        print(default_text("Peso en kilogramos (sin kg):"))
        peso = input(INPUT_CHAR + " ")
        print(default_text("Porcentaje de recuperación estimado:"))
        recuperacion = input(INPUT_CHAR + " ")

        try:
            residuo = Residuo(nombre, tipo, tratamiento, int(peso), float(recuperacion))
            self.residuos.append(residuo)
            print()
            print(default_text("Residuo sólido registrado correctamente"))
        except Exception as e:
            print(f"Error: {e}")
