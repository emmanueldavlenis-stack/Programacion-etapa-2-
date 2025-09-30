import random 
import csv
from gestor_residuos import Residuo, GestorResiduos, tipos_residuos, metodos_tratamiento
from menu_utils import default_text

def generar_csv_residuos(nombre_archivo, cantidad):
    with open(nombre_archivo + ".csv", mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Residuo", "Tipo", "Metodo tratamiento", "Peso", "Porcentaje de recuperacion"])
        for _ in range(cantidad):
            tipo = random.choice(list(tipos_residuos.keys()))
            match tipo:
                case 1:
                    caso = random.choice([
                "Cáscaras de frutas",
                "Restos de comida",
                "Hojas secas",
                "Bolsas de té",
                "Pan duro",
                "Cáscaras de huevo"
                    ])
                case 2:
                    caso = random.choice ([
                "Escombros",
                "Cerámica rota",
                "Pañales desechables",
                "Colillas de cigarro",
                "Toallas sanitarias",
                "Servilletas sucias"
                    ])
                case 3:
                    caso = random.choice([
                "Pilas usadas",
                "Medicamentos vencidos",
                "Aerosoles vacíos",
                "Aceite de motor",
                "Disolventes químicos",
                "Lámparas fluorescentes"
                    ])
                case 4:
                    caso = random.choice([
                "Botellas plásticas",
                "Latas de aluminio",
                "Cartón",
                "Papel limpio",
                "Vidrio",
                ])
                case _:
                    print("Error")
            peso = random.randint(1, 15)
            porcentaje = random.randint(1,100)
            escritor.writerow([
                caso,
                tipos_residuos[tipo],
                random.choice(list(metodos_tratamiento.values())),
                peso, 
                porcentaje
            ])
    print(default_text(f"Datos generados con éxito en '{nombre_archivo + ".csv"}'"))
    input("\nPresione enter para continuar...")
    

def cargar_residuos_desde_csv(nombre_archivo, gestor: GestorResiduos):
    with open(nombre_archivo + ".csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                residuo = Residuo(
                    fila["Residuo"],
                    fila["Tipo"],
                    fila["Metodo tratamiento"],
                    float(fila["Peso"]),
                    float(fila["Porcentaje de recuperacion"])
                )
                gestor.residuos.append(residuo)
            except Exception as e:
                print(f"Error en fila {fila}: {e}")
    print(default_text(f"Se terminaron de cargar todos los residuos desde '{nombre_archivo + ".csv"}'"))
    input("\nPresione enter para continuar...")
