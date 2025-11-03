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

# ----- Selección aleatoria del caso -----
culpable = random.choice(personajes)
arma = random.choice(armas)
lugar = random.choice(locaciones)
historias = generar_historias(culpable, arma, lugar)

# ----- Interfaz de consola -----
print("===== SIMULADOR CLUE (CONSOLA) =====")
print("\nHistorias posibles:")
for h in historias:
    print("- " + h)

print("\nIntenta adivinar el caso:")
print("Personajes:", ", ".join(personajes))
print("Armas:", ", ".join(armas))
print("Locaciones:", ", ".join(locaciones))

input_culpable = input("¿Quién es el culpable? ")
input_arma = input("¿Qué arma se usó? ")
input_lugar = input("¿Dónde ocurrió el crimen? ")

# ----- Verificación -----
if (input_culpable.strip().lower() == culpable.lower() and
    input_arma.strip().lower() == arma.lower() and
    input_lugar.strip().lower() == lugar.lower()):
    print("\n¡Felicidades! Has adivinado correctamente el caso.")
else:
    print("\nNo es correcto. La solución era:")
    print(f"Culpable: {culpable}")
    print(f"Arma: {arma}")
    print(f"Lugar: {lugar}")
