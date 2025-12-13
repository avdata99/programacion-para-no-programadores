from random import choice
# la funcion choice de la libreria random permite elegir
# un elemento al azar de una lista


def inicializar_juego():
    """Inicializa todas las variables del juego"""
    # Diccionario de palabras por categorías (fácil de ampliar)
    palabras = {
        "animales": ["perro", "gato", "elefante", "jirafa", "leon", "tigre"],
        "frutas": ["manzana", "banana", "naranja", "uva", "fresa", "sandia"],
        "paises": ["mexico", "argentina", "españa", "brasil", "colombia"]
    }

    # Elegir una categoría y palabra al azar
    categoria = choice(list(palabras.keys()))
    palabra_secreta = choice(palabras[categoria])

    # Diccionario con el estado del juego
    juego = {
        "palabra_secreta": palabra_secreta,
        "categoria": categoria,
        "letras_adivinadas": [],
        "letras_incorrectas": [],
        "intentos_maximos": 6,
        "intentos_usados": 0,
        # palabra culta mantiene el estado actual del progreso del jugador
        # con las letras adivinadas y guiones para las no adivinadas todavia
        # se inicializa con algo como ["-", "-", "-", "-", "-", "-", "-"]
        "palabra_oculta": ["-"] * len(palabra_secreta)
    }

    return juego


def mostrar_estado(juego):
    """Imprime el estado actual del juego"""
    print(f"Categoría: {juego['categoria'].upper()}")
    palabra_oculta_str = "".join(juego['palabra_oculta'])
    print(f"Palabra: {palabra_oculta_str}")
    print(f"Letras incorrectas: {juego['letras_incorrectas']}")
    print(f"Intentos: {juego['intentos_usados']}/{juego['intentos_maximos']}")


def procesar_letra(juego, letra):
    """Procesa una letra ingresada por el jugador
    1. Verifica si la letra ya fue intentada
    2. Actualiza el estado del juego según si la letra está en la palabra secreta
    Recibe el estado actual del juego y la letra ingresada
    Devuelve el estado actualizado del juego
    """
    letra = letra.lower()

    # Verificar si ya se intentó esta letra
    if letra in juego['letras_adivinadas'] or letra in juego['letras_incorrectas']:
        print(f"¡Ya intentaste la letra '{letra}'!")
        return juego

    # Verificar si la letra está en la palabra secreta
    if letra in juego['palabra_secreta']:
        juego['letras_adivinadas'].append(letra)

        # Revelar la letra en la palabra oculta
        for i, caracter in enumerate(juego['palabra_secreta']):
            if caracter == letra:
                juego['palabra_oculta'][i] = letra
    else:
        juego['letras_incorrectas'].append(letra)
        juego['intentos_usados'] += 1

    return juego


def ya_gano(juego):
    """Verifica si el juego ya se ganó"""
    if "-" not in juego['palabra_oculta']:
        return True
    return False


def ya_perdio(juego):
    """Verifica si el juego ya se perdió"""
    if juego['intentos_usados'] >= juego['intentos_maximos']:
        return True

    return False
