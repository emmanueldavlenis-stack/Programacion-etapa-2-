from menu_utils import title_style, default_text, separator, options
from gestor_residuos import GestorResiduos

def main():
    gestor = GestorResiduos()
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
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass

if __name__ == "__main__":
    main()