import csv

def cargar_juegos():
    juegos = []

    try:
        with open("juegos.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                juegos.append(fila)

        if len(juegos) == 0:
            print("No hay juegos registrados.")
            return none

        return juegos
    except FileNotFoundError:
        print("Error: No se ha enccontrado la base de datos.")
        return none

