import random

# ----- Datos -----
personajes = [
    "Profesor Plum",
    "Señora Green",
    "Coronel Mustard",
    "Señorita Scarlet",
    "Doctor White"
]

armas = [
    "Candelabro",
    "Cuchillo",
    "Pistola",
    "Cuerda",
    "Llave Inglesa"
]

locaciones = [
    "Biblioteca",
    "Cocina",
    "Salón",
    "Habitación",
    "Jardín"
]

# ----- Función para generar historias -----
def generar_historias(culpable, arma, lugar):
    return [
        f"Historia 1: El {culpable} estaba en la {lugar} usando el {arma} para cometer el crimen.",
        f"Historia 2: Una pista lleva al {culpable} que con el {arma} en la {lugar} dejó evidencia crucial.",
        f"Historia 3: Nadie sospechaba del {culpable} quien escondió el {arma} en la {lugar}.",
        f"Historia 4: El {arma} fue encontrado en la {lugar}, y todo apunta al {culpable}.",
        f"Historia 5: Tras una investigación, se descubre que el {culpable} planeó todo en la {lugar} con el {arma}."
    ]

# ----- Función para jugar un caso con pistas progresivas -----
def jugar_caso():
    culpable = random.choice(personajes)
    arma = random.choice(armas)
    lugar = random.choice(locaciones)
    historias = generar_historias(culpable, arma, lugar)

    print("\n===== NUEVO CASO =====")
    print("Intenta descubrir el culpable, el arma y el lugar del crimen.")
    print("Personajes:", ", ".join(personajes))
    print("Armas:", ", ".join(armas))
    print("Locaciones:", ", ".join(locaciones))

    puntos = 0
    acertado = False

    for i, historia in enumerate(historias):
        print(f"\nPista {i+1}: {historia}")
        puntos += 1  # cada pista consumida resta puntos

        input_culpable = input("¿Quién crees que es el culpable? (deja vacío para no adivinar): ").strip()
        input_arma = input("¿Qué arma se usó? (deja vacío para no adivinar): ").strip()
        input_lugar = input("¿Dónde ocurrió el crimen? (deja vacío para no adivinar): ").strip()

        if (input_culpable.lower() == culpable.lower() and
            input_arma.lower() == arma.lower() and
            input_lugar.lower() == lugar.lower()):
            print("\n¡Correcto! Has resuelto el caso antes de que se mostraran todas las pistas.")
            puntos = max(5 - i, 1)  # más puntos si adivinas antes
            acertado = True
            break
        else:
            print("No es correcto. Puedes intentar de nuevo después de la siguiente pista.")

    if not acertado:
        print("\nSe han mostrado todas las pistas.")
        print(f"La solución era: Culpable: {culpable}, Arma: {arma}, Lugar: {lugar}")
        puntos = 1  # mínimo de puntos si no adivinas

    print(f"Puntos obtenidos en este caso: {puntos}")
    return puntos

# ----- Programa principal -----
def main():
    print("===== SIMULADOR CLUE EN CONSOLA CON PISTAS PROGRESIVAS =====")
    total_puntos = 0
    rondas = 0

    while True:
        jugar = input("\n¿Quieres jugar un nuevo caso? (s/n): ").strip().lower()
        if jugar != "s":
            break
        rondas += 1
        total_puntos += jugar_caso()

    print(f"\nJuego terminado. Jugaste {rondas} rondas y acumulaste {total_puntos} puntos.")
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()
