from menu_utils import separator, title_style, default_text, options, INPUT_CHAR
from enum import Enum
import os
from datetime import datetime
from fpdf import FPDF

formatos = {"1":"TXT", "2":"PDF"}
tipos_residuos = {1: "Organico", 2:"Inorganico", 3: "Peligroso", 4:"Reciclable"}
metodos_tratamiento = {1: "Reciclaje", 2: "Incineración", 3: "Compostaje", 4: "Relleno sanitario"}

class Residuo():
    def __init__(self, nombre, tipo, tratamiento, peso, recuperacion):
        assert isinstance(nombre, str) and nombre.strip(), "El texto debe ser un nombre válido."
        assert isinstance(tipo, (int, str)) and (tipo in tipos_residuos or tipos_residuos.values()), "Ese tipo de residuo no existe."
        assert isinstance(tratamiento, (int, str)) and (tratamiento in metodos_tratamiento or metodos_tratamiento.values), "Ese método de tratamiento no existe."
        assert isinstance(peso, (float, int)) and peso > 0, "Peso inválido. Debe ser un número positivo"
        assert isinstance(recuperacion, float) and 0 <= recuperacion <= 100, "Porcentaje inválido. Debe ser un numero entre 0 y 100"
        self.nombre = nombre
        self.tipo = tipos_residuos[tipo] if isinstance(tipo, int) else tipo
        self.tratamiento = metodos_tratamiento[tratamiento] if isinstance(tratamiento, int) else tratamiento
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
        print(default_text("Tipo:"))
        tipo = options(*tipos_residuos.values())
        print(default_text("Método de tratamiento:"))
        tratamiento = options(*metodos_tratamiento.values())
        print(default_text("Peso en kilogramos (sin kg):"))
        peso = input(INPUT_CHAR + " ")
        print(default_text("Porcentaje de recuperación estimado (sin %):"))
        recuperacion = input(INPUT_CHAR + " ")

        try:
            residuo = Residuo(nombre, int(tipo), int(tratamiento), float(peso), float(recuperacion))
            self.residuos.append(residuo)
            print()
            print(default_text("Residuo sólido registrado correctamente"))
            input("\nPresione enter para continuar...")
        except Exception as e:
            print(f"Error: {e}")

    def listar_tipo(self):
        if len(self.residuos) == 0:
            print("No hay residuos sólidos registrados")
            return
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

    def listar_tratamiento(self):
        if len(self.residuos) == 0:
            print("No hay residuos sólidos registrados")
            return
        print(default_text("Método de tratamiento:"))
        try:
            tratamiento = int(options(*metodos_tratamiento.values()))
            if not tratamiento in metodos_tratamiento:
                print("Opción inválida, inténtelo de nuevo")
                return
            tratamiento = metodos_tratamiento[tratamiento]
            print(separator())
            print(title_style(f"Lista de residuos con el método de tratamiento: \"{tratamiento}\""))
            print(separator())
            filtrado = [residuo for residuo in self.residuos if residuo.tratamiento == tratamiento]
            for i, residuo in enumerate(filtrado):  
                print(f"{i + 1}. {residuo}", margin=0)
            input("\nPresione enter para continuar...")
        except Exception as e:
            print(f"Error: {e}")

    def generar_resumen(self):
        if len(self.residuos) == 0:
            print("No hay residuos sólidos registrados")
            return
        tipos = [r.tipo for r in self.residuos]
        tratamientos = [r.tratamiento for r in self.residuos]
        print(default_text("Residuos por tipo:"))
        for tipo in set(tipos):
            print(f"    {tipo}: {tipos.count(tipo)}")
        print(default_text("Promedio de peso por tipo:"))
        for tipo in set(tipos):
            pesos = [r.peso for r in self.residuos if r.tipo == tipo]
            promedio = sum(pesos) / len(pesos)
            print(f"    {tipo}: {promedio:.2f}kg")
        print(default_text("Promedio de recuperación por tratamiento:"))
        for t in set(tratamientos):
            recuperaciones = [r.recuperacion for r in self.residuos if r.tratamiento == t]
            promedio = sum(recuperaciones) / len(recuperaciones)
            print(f"    {t}: {promedio:.2f}%")
        input("\nPresione enter para continuar...")

    def exportar_resumen(self):
        if len(self.residuos) == 0:
            print("No hay residuos sólidos registrados")
            return
        print(default_text("Seleccion el formato de exportación:"))
        formato = options("TXT", "PDF")
        if not formato in formatos:
            print("Opción inválida, inténtelo de nuevo")
            return
        carpeta = "reportes"
        os.makedirs(carpeta, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        nombre_archivo = f"reporte_residuos_{timestamp}.{formatos[formato]}"
        ruta = os.path.join(carpeta, nombre_archivo)

        contenido = []

        tipos = [r.tipo for r in self.residuos]
        tratamientos = [r.tratamiento for r in self.residuos]
        contenido.append(default_text("Residuos por tipo:"))
        for tipo in set(tipos):
            contenido.append(f"    {tipo}: {tipos.count(tipo)}")
        contenido.append(default_text("Promedio de peso por tipo:"))
        for tipo in set(tipos):
            pesos = [r.peso for r in self.residuos if r.tipo == tipo]
            promedio = sum(pesos) / len(pesos)
            contenido.append(f"    {tipo}: {promedio:.2f}kg")
        contenido.append(default_text("Promedio de recuperación por tratamiento:"))
        for t in set(tratamientos):
            recuperaciones = [r.recuperacion for r in self.residuos if r.tratamiento == t]
            promedio = sum(recuperaciones) / len(recuperaciones)
            contenido.append(f"    {t}: {promedio:.2f}%")

        match formato:
            case "1":
                with open(ruta, "w") as f:
                    f.write("".join(contenido))
                print(f"Reporte exportado como '{ruta}'")
                input("\nPresione enter para continuar...")
            case "2":
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for text in contenido:
                    for linea in text.split("\n"):
                        pdf.cell(200, 10, txt=linea, ln=True)
                pdf.output(ruta)
                print(f"Reporte exportado como '{ruta}'")
                input("\nPresione enter para continuar...")
            case _:
                print(f"Formato inválido. Los únicos formatos válidos son: {formatos}")
