import random
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# ----- Datos -----
personajes = ["Profesor Plum", "Señora Green", "Coronel Mustard", "Señorita Scarlet", "Doctor White"]
armas = ["Candelabro", "Cuchillo", "Pistola", "Cuerda", "Llave Inglesa"]
locaciones = ["Biblioteca", "Cocina", "Salón", "Habitación", "Jardín"]

# ----- Función para generar imagen -----
def generar_imagen(personaje, arma, lugar, acertado):
    img = Image.new('RGB', (500, 300), color='white')
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    d.text((10, 10), f"Personaje: {personaje}", fill=(0,0,0), font=font)
    d.text((10, 50), f"Arma: {arma}", fill=(0,0,0), font=font)
    d.text((10, 90), f"Lugar: {lugar}", fill=(0,0,0), font=font)
    mensaje = "¡Correcto!" if acertado else "¡Incorrecto!"
    color = (0,150,0) if acertado else (200,0,0)
    d.text((10, 150), mensaje, fill=color, font=font)
    return img

# ----- Función para elegir opción por menú -----
def elegir_opcion(lista, nombre_tipo):
    print(f"\nSelecciona {nombre_tipo}:")
    for i, opcion in enumerate(lista, 1):
        print(f"{i}. {opcion}")
    while True:
        try:
            eleccion = int(input(f"Ingrese el número de tu {nombre_tipo}: "))
            if 1 <= eleccion <= len(lista):
                return lista[eleccion-1]
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

# ----- Función para jugar una ronda -----
def jugar_caso():
    culpable = random.choice(personajes)
    arma = random.choice(armas)
    lugar = random.choice(locaciones)

    print("\n===== NUEVO CASO =====")
    eleccion_culpable = elegir_opcion(personajes, "culpable")
    eleccion_arma = elegir_opcion(armas, "arma")
    eleccion_lugar = elegir_opcion(locaciones, "lugar")

    acertado = (eleccion_culpable == culpable and
                eleccion_arma == arma and
                eleccion_lugar == lugar)
    
    puntos = 3 if acertado else 1

    # Generar imagen y mostrar con matplotlib
    img = generar_imagen(eleccion_culpable, eleccion_arma, eleccion_lugar, acertado)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print("\nResultado del caso:")
    if acertado:
        print("¡Correcto!")
    else:
        print("No es correcto.")
    print(f"Solución real: {culpable}, {arma}, {lugar}")
    print(f"Puntos obtenidos: {puntos}")

    return {
        "intento_usuario": {
            "culpable": eleccion_culpable,
            "arma": eleccion_arma,
            "lugar": eleccion_lugar
        },
        "solucion": {
            "culpable": culpable,
            "arma": arma,
            "lugar": lugar
        },
        "acierto": acertado,
        "puntos": puntos
    }

# ----- Programa principal -----
def main():
    print("===== CLUE CONSOLA - CON IMÁGENES =====")
    total_puntos = 0
    rondas = 0
    historial = []

    while True:
        jugar = input("\n¿Quieres jugar un nuevo caso? (s/n): ").strip().lower()
        if jugar != "s":
            break
        rondas += 1
        resultado = jugar_caso()
        historial.append(resultado)
        total_puntos += resultado["puntos"]

    print("\n===== REPORTE FINAL =====")
    for idx, r in enumerate(historial, 1):
        print(f"\nRonda {idx}:")
        print(f"Intento: {r['intento_usuario']}")
        print(f"Solución: {r['solucion']}")
        print(f"Acierto: {'Sí' if r['acierto'] else 'No'}")
        print(f"Puntos: {r['puntos']}")

    print(f"\nJuego terminado. Jugaste {rondas} rondas, total puntos: {total_puntos}")
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()
