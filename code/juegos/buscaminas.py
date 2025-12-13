import random


def crear_tablero(filas, columnas, minas):
    """Crea un tablero vacío y coloca minas al azar"""
    # Crear tablero visible para el jugador (lo que ve)
    tablero_visible = [['-' for _ in range(columnas)] for _ in range(filas)]

    # Crear tablero oculto con las minas
    tablero_oculto = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Colocar minas al azar
    minas_colocadas = 0
    while minas_colocadas < minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        # Si no hay mina en esa posición, colocar una
        if tablero_oculto[fila][columna] != 'M':
            tablero_oculto[fila][columna] = 'M'
            minas_colocadas += 1

            # Incrementar números alrededor de la mina
            for f in range(max(0, fila-1), min(filas, fila+2)):
                for c in range(max(0, columna-1), min(columnas, columna+2)):
                    if tablero_oculto[f][c] != 'M':
                        tablero_oculto[f][c] += 1

    return tablero_visible, tablero_oculto


def mostrar_tablero(tablero):
    """Muestra el tablero en la consola con coordenadas"""
    print("\n   " + " ".join(str(i) for i in range(len(tablero[0]))))
    print("  " + "-" * (len(tablero[0]) * 2 + 1))

    for i, fila in enumerate(tablero):
        print(f"{i}| " + " ".join(str(celda) for celda in fila) + " |")


def jugar_turno(tablero_visible, tablero_oculto, filas, columnas):
    """Pide coordenadas al usuario y revela la casilla"""
    while True:
        try:
            entrada = input("\nIngresa coordenadas (fila columna): ")
            if entrada.lower() == 'salir':
                return None, None, True

            coords = entrada.split()
            if len(coords) != 2:
                print("Debes ingresar dos números separados por espacio")
                continue

            fila = int(coords[0])
            columna = int(coords[1])

            if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
                print(f"Coordenadas fuera de rango. Usa filas 0-{filas-1} y columnas 0-{columnas-1}")
                continue

            if tablero_visible[fila][columna] != '-':
                print("¡Ya revelaste esa casilla! Elige otra.")
                continue

            # Revelar la casilla
            valor = tablero_oculto[fila][columna]

            if valor == 'M':
                tablero_visible[fila][columna] = '💣'
                return tablero_visible, tablero_oculto, False  # Perdió
            else:
                tablero_visible[fila][columna] = valor if valor > 0 else ' '

                # Si es una casilla vacía (0), revelar vecinos automáticamente
                if valor == 0:
                    revelar_vecinos(tablero_visible, tablero_oculto, fila, columna, filas, columnas)

                return tablero_visible, tablero_oculto, True  # Continúa jugando

        except ValueError:
            print("Por favor, ingresa números válidos")
        except Exception as e:
            print(f"Error: {e}")


def revelar_vecinos(tablero_visible, tablero_oculto, fila, columna, filas, columnas):
    """Revela automáticamente casillas vecinas cuando se encuentra un 0"""
    # Usamos una pila para revelar todas las casillas conectadas de valor 0
    pila = [(fila, columna)]

    while pila:
        f, c = pila.pop()

        # Revisar todas las casillas alrededor
        for fi in range(max(0, f-1), min(filas, f+2)):
            for ci in range(max(0, c-1), min(columnas, c+2)):
                if tablero_visible[fi][ci] == '-':  # Solo si no está revelada
                    valor = tablero_oculto[fi][ci]
                    if valor == 0:
                        tablero_visible[fi][ci] = ' '
                        pila.append((fi, ci))
                    elif valor != 'M':  # Si es un número (1-8)
                        tablero_visible[fi][ci] = valor


def verificar_victoria(tablero_visible, tablero_oculto, minas):
    """Verifica si el jugador ha ganado"""
    casillas_sin_revelar = 0
    for i in range(len(tablero_visible)):
        for j in range(len(tablero_visible[0])):
            if tablero_visible[i][j] == '-':
                casillas_sin_revelar += 1

    # Gana si solo quedan sin revelar las minas
    return casillas_sin_revelar == minas


def main():
    """Función principal del juego"""
    print("=== BUSCAMINAS ===")
    print("Revela todas las casillas sin minas para ganar.")
    print("Ingresa 'salir' para terminar el juego.\n")

    # Configuración inicial (los estudiantes pueden modificar estos valores)
    FILAS = 5
    COLUMNAS = 5
    MINAS = 3

    # Crear tableros
    tablero_visible, tablero_oculto = crear_tablero(FILAS, COLUMNAS, MINAS)

    juego_activo = True
    victoria = False

    while juego_activo:
        # Mostrar estado actual
        mostrar_tablero(tablero_visible)
        print(f"\nMinas: {MINAS} | Tablero: {FILAS}x{COLUMNAS}")

        # Jugar un turno
        tablero_visible, tablero_oculto, continuar = jugar_turno(
            tablero_visible, tablero_oculto, FILAS, COLUMNAS
        )

        if not continuar:  # El usuario escribió 'salir'
            print("\n¡Juego terminado!")
            break

        if tablero_visible is None:  # Perdió (pisó una mina)
            print("\n¡BOOM! ¡Pisaste una mina!")
            print("Tablero completo:")
            mostrar_tablero(tablero_oculto)
            juego_activo = False
        else:
            # Verificar si ganó
            if verificar_victoria(tablero_visible, tablero_oculto, MINAS):
                print("\n¡FELICIDADES! ¡Ganaste el juego!")
                print("Tablero completo:")
                mostrar_tablero(tablero_oculto)
                victoria = True
                juego_activo = False

    if not victoria and tablero_visible is not None:
        print("\n¡Mejor suerte la próxima vez!")


if __name__ == "__main__":
    main()
