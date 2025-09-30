from menu_utils import separator, title_style, default_text, options, INPUT_CHAR
from enum import Enum

tipos_residuos = {1: "Organico", 2:"Inorganico", 3: "Peligroso", 4:"Reciclable"}
metodos_tratamiento = {1: "Reciclaje", 2: "Incineración", 3: "Compostaje", 4: "Relleno sanitario"}

class Residuo():
    def __init__(self, nombre, tipo, tratamiento, peso, recuperacion):
        assert isinstance(nombre, str) and nombre.strip(), "El texto debe ser un nombre válido."
        assert isinstance(tipo, int) and tipo in tipos_residuos, "Ese tipo de residuo no existe."
        assert isinstance(tratamiento, int) and tratamiento in metodos_tratamiento, "Ese método de tratamiento no existe."
        assert isinstance(peso, int) and peso > 0, "Peso inválido. Debe ser un número entero positivo"
        assert isinstance(recuperacion, float) and 0 <= recuperacion <= 100, "Porcentaje inválido. Debe ser un numero entre 0 y 100"
        self.nombre = nombre
        self.tipo = tipos_residuos[tipo]
        self.tratamiento = metodos_tratamiento[tratamiento]
        self.peso = peso
        self.recuperacion = recuperacion

    def __str__(self):
        return (f"Nombre: {self.nombre} | Tipo: {self.tipo} | Método de tratamiento: {self.tratamiento} | "
                f"Peso: {self.peso}kg | Porcentaje de recuperacion: {self.recuperacion:.1f}%")

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
        print(default_text("Porcentaje de recuperación estimado (sin %):"))
        recuperacion = input(INPUT_CHAR + " ")

        try:
            residuo = Residuo(nombre, int(tipo), int(tratamiento), int(peso), float(recuperacion))
            self.residuos.append(residuo)
            print()
            print(default_text("Residuo sólido registrado correctamente"))
            input("\nPresione enter para continuar...")
        except Exception as e:
            print(f"Error: {e}")

    def listar_tipo(self):
        print(default_text("Tipo de residuo:"))
        try:
            tipo = int(options(*tipos_residuos.values()))
            if not tipo in tipos_residuos:
                print("Opción inválida, inténtelo de nuevo")
                return
            tipo = tipos_residuos[tipo]
            print(separator())
            print(title_style(f"Lista de residuos de tipo {tipo}"))
            print(separator())
            filtrado = [residuo for residuo in self.residuos if residuo.tipo == tipo]
            for i, residuo in enumerate(filtrado):
                print(f"{i + 1}. {residuo}")
            input("\nPresione enter para continuar...")
        except Exception as e:
            print(f"Error: {e}")