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
            return None

        return juegos
    except FileNotFoundError:
        print("Error: No se ha encontrado la base de datos.")
        return None

def bienvenida():

    print("="*45)
    print("          Bienvenido a SteamAI")
    print("="*45)

    print("\nHola. Soy SteamAI.")
    print("Voy a ayudarte a encontrar el juego ideal.")
    print("\nEscribí 'salir' cuando quieras finalizar.\n")

def preguntar(texto, opciones):

    while True:

        print("\n"+texto)

        for opcion in opciones:
            print("-", opcion)

        respuesta = input("> ").strip().lower()

        if respuesta == "salir":
            return "salir"

        for opcion in opciones:

            if respuesta == opcion.lower():
                return opcion

        print("\nOpción inválida.")

def filtrar(juegos, columna, valor):

    filtrados = []

    for juego in juegos:

        if juego[columna].lower() == valor.lower():
            filtrados.append(juego)

    return filtrados

def mostrar_resultados(juegos):

    print("\n================================")

    if len(juegos) == 1:

        print("Listo. Encontré un juego que puede gustarte:\n")

    else:

        print("Encontré estos juegos podrían gustarte:\n")

    for juego in juegos[:3]:

        print("-", juego["nombre"])

    print("================================")




