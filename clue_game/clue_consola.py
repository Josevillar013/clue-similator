# clue_game.py
import random
import os
from IPython.display import display, Image as IPImage  # Solo si quieres mostrar imágenes en notebook

# --- Datos del juego ---
personajes = ["profesor_plum", "senora_green", "coronel_mustard", "senorita_scarlet", "doctor_white"]
armas = ["candelabro", "cuchillo", "pistola", "cuerda", "llave_inglesa"]
locaciones = ["biblioteca", "cocina", "salon", "habitacion", "jardin"]

# --- Función para jugar una ronda ---
def jugar_ronda():
    culpable = random.choice(personajes)
    arma = random.choice(armas)
    lugar = random.choice(locaciones)
    
    print("\nPersonajes:")
    for i, p in enumerate(personajes, 1):
        print(f"{i}. {p}")
    sel_p = int(input("Número del culpable: "))
    
    print("\nArmas:")
    for i, a in enumerate(armas, 1):
        print(f"{i}. {a}")
    sel_a = int(input("Número del arma: "))
    
    print("\nLugares:")
    for i, l in enumerate(locaciones, 1):
        print(f"{i}. {l}")
    sel_l = int(input("Número del lugar: "))
    
    intento = {
        "culpable": personajes[sel_p-1],
        "arma": armas[sel_a-1],
        "lugar": locaciones[sel_l-1]
    }
    
    solucion = {
        "culpable": culpable,
        "arma": arma,
        "lugar": lugar
    }
    
    acertado = (intento == solucion)
    puntos = 3 if acertado else 1
    
    print(f"\nTu intento: {intento}")
    print(f"Solución real: {solucion}")
    print("¡Correcto!" if acertado else "¡Incorrecto!")
    print(f"Puntos obtenidos: {puntos}\n")
    return puntos

# --- Programa principal ---
def main():
    total_puntos = 0
    rondas = 5
    for i in range(rondas):
        print(f"\n===== RONDA {i+1} =====")
        total_puntos += jugar_ronda()
    print(f"\nJuego terminado. Puntaje total: {total_puntos}")

if __name__ == "__main__":
    main()
