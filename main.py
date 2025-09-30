from menu_utils import title_style, default_text, separator, options, INPUT_CHAR
from gestor_residuos import GestorResiduos
import csv_utils
import pdf_pro

def main():
    gestor = GestorResiduos()
    while True:
        print(separator())
        print(title_style("MENU PRINCIPAL"))
        print(separator())
        option = options(
            "Registrar residuo",
            "Listar residuos por tipo",
            "Listar residuos por método de tratamiento",
            "Generar resumen estadístico",
            "Exportar resumen (txt/pdf)",
            "Generar CSV con residuos simulados",
            "Cargar residuos desde CSV",
            "Exportar reporte profesional (PDF)",
            "Salir"
        )
        match option:
            case "1":
                gestor.registrar_residuo()
            case "2":
                gestor.listar_tipo()
            case "3":
                gestor.listar_tratamiento()
            case "4":
                gestor.generar_resumen()
            case "5":
                gestor.exportar_resumen()
            case "6":
                print(default_text("Nombre del archivo CSV (sin .csv):"))
                nombre = input(INPUT_CHAR + " ")
                print(default_text("Cantidad de frutas a generar:"))
                cantidad = int(input(INPUT_CHAR + " "))
                csv_utils.generar_csv_residuos(nombre, cantidad)
            case "7":
                print(default_text("Nombre del archivo CSV a cargar (sin .csv):"))
                nombre = input(INPUT_CHAR + " ")
                csv_utils.cargar_residuos_desde_csv(nombre, gestor)
            case "8":
                print(default_text("Nombre del archivo PDF (sin .pdf):"))
                nombre = input(INPUT_CHAR + " ")
                pdf_pro.exportar_reporte_profesional(nombre, gestor)
            case "9":
                print(default_text("\nHasta luego!"))
                break

if __name__ == "__main__":
    main()