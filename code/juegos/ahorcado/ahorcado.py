from utils import inicializar_juego, procesar_letra, ya_gano, ya_perdio, mostrar_estado
from estados import mostrar_ahorcado


print("🎮 BIENVENIDO AL JUEGO DEL AHORCADO 🎮")
print("Adivina la palabra antes de que se complete el dibujo.")

# Inicializar juego
# Todo el estado del juego se guarda en el diccionario 'juego'
juego = inicializar_juego()

while True:
    # Mostrar estado actual
    mostrar_ahorcado(juego['intentos_usados'])
    mostrar_estado(juego)

    # Pedir una letra al jugador
    letra = input("\nIngresa una letra (o 'salir' para terminar): ").lower()

    # Verificar si quiere salir
    if letra == 'salir':
        print(f"\nLa palabra era: {juego['palabra_secreta']}")
        print("¡Gracias por jugar!")
        break

    # Validar entrada (solo una letra)
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa UNA sola letra.")
        continue

    # Procesar la letra
    juego = procesar_letra(juego, letra)

    # Verificar si el juego terminó
    if ya_gano(juego):
        print("\n¡FELICIDADES! 🎉")
        break

    if ya_perdio(juego):
        print("\n¡AHORCADO! 😢")
        print(f"La palabra era: {juego['palabra_secreta']}")
        break
