import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow

# ----- Datos -----
personajes = [
    {"nombre": "Profesor Plum", "profesion": "Profesor", "imagen": "imagenes/profesor_plum.png"},
    {"nombre": "Señora Green", "profesion": "Banquera", "imagen": "imagenes/senora_green.png"},
    {"nombre": "Coronel Mustard", "profesion": "Militar", "imagen": "imagenes/coronel_mustard.png"},
    {"nombre": "Señorita Scarlet", "profesion": "Actriz", "imagen": "imagenes/senorita_scarlet.png"},
    {"nombre": "Doctor White", "profesion": "Médico", "imagen": "imagenes/doctor_white.png"}
]

armas = [
    {"nombre": "Candelabro", "imagen": "imagenes/candelabro.png"},
    {"nombre": "Cuchillo", "imagen": "imagenes/cuchillo.png"},
    {"nombre": "Pistola", "imagen": "imagenes/pistola.png"},
    {"nombre": "Cuerda", "imagen": "imagenes/cuerda.png"},
    {"nombre": "Llave Inglesa", "imagen": "imagenes/llave_inglesa.png"}
]

locaciones = [
    {"nombre": "Biblioteca", "imagen": "imagenes/biblioteca.png"},
    {"nombre": "Cocina", "imagen": "imagenes/cocina.png"},
    {"nombre": "Salón", "imagen": "imagenes/salon.png"},
    {"nombre": "Habitación", "imagen": "imagenes/habitacion.png"},
    {"nombre": "Jardín", "imagen": "imagenes/jardin.png"}
]

# ----- Funciones -----
def generar_historia(culpable, arma, lugar):
    historias = [
        f"Historia 1: El {culpable['nombre']} estaba en la {lugar['nombre']} usando el {arma['nombre']} para cometer el crimen.",
        f"Historia 2: Una pista lleva al {culpable['nombre']} que con el {arma['nombre']} en la {lugar['nombre']} dejó evidencia crucial.",
        f"Historia 3: Nadie sospechaba del {culpable['nombre']} quien escondió el {arma['nombre']} en la {lugar['nombre']}.",
        f"Historia 4: El {arma['nombre']} fue encontrado en la {lugar['nombre']}, y todo apunta al {culpable['nombre']}.",
        f"Historia 5: Tras una investigación, se descubre que el {culpable['nombre']} planeó todo en la {lugar['nombre']} con el {arma['nombre']}."
    ]
    return historias

# ----- Selección aleatoria -----
culpable = random.choice(personajes)
arma = random.choice(armas)
lugar = random.choice(locaciones)
historias = generar_historia(culpable, arma, lugar)

# ----- GUI -----
root = tk.Tk()
root.title("Clue Final - Miniaturas")
root.geometry("700x800")
root.configure(bg="#f5f5dc")

tk.Label(root, text="SIMULADOR CLUE", font=("Arial", 24, "bold"), bg="#f5f5dc").pack(pady=10)

# Mostrar historias
historia_text = tk.StringVar()
tk.Label(root, textvariable=historia_text, justify="left", wraplength=650, bg="#f5f5dc").pack(pady=10)

def mostrar_historias():
    historia_text.set("")
    for i, h in enumerate(historias):
        root.after(i*500, lambda h=h: historia_text.set(h))

tk.Button(root, text="Mostrar historias posibles", command=mostrar_historias, bg="#4caf50", fg="white").pack(pady=5)

# ----- Cargar imágenes -----
def cargar_imagen(ruta, w=100, h=100):
    img = Image.open(ruta)
    img = img.resize((w, h))
    return ImageTk.PhotoImage(img)

# ----- Variables de selección -----
selected_culpable = tk.StringVar()
selected_arma = tk.StringVar()
selected_lugar = tk.StringVar()

# ----- Mostrar miniaturas -----
frame_culpable = tk.Frame(root, bg="#f5f5dc")
frame_culpable.pack(pady=10)
tk.Label(frame_culpable, text="Selecciona al culpable:", bg="#f5f5dc").pack()
culpable_imgs = []

def seleccionar_culpable(nombre, img_label):
    selected_culpable.set(nombre)
    img_label.config(bg="#d1ffd1")

for p in personajes:
    img = cargar_imagen(p['imagen'], 80, 80)
    culpable_imgs.append(img)
    lbl = tk.Label(frame_culpable, image=img, bd=2, relief="solid")
    lbl.pack(side="left", padx=5)
    lbl.bind("<Button-1>", lambda e, n=p['nombre'], l=lbl: seleccionar_culpable(n, l))

frame_arma = tk.Frame(root, bg="#f5f5dc")
frame_arma.pack(pady=10)
tk.Label(frame_arma, text="Selecciona el arma:", bg="#f5f5dc").pack()
arma_imgs = []

def seleccionar_arma(nombre, img_label):
    selected_arma.set(nombre)
    img_label.config(bg="#d1ffd1")

for a in armas:
    img = cargar_imagen(a['imagen'], 80, 80)
    arma_imgs.append(img)
    lbl = tk.Label(frame_arma, image=img, bd=2, relief="solid")
    lbl.pack(side="left", padx=5)
    lbl.bind("<Button-1>", lambda e, n=a['nombre'], l=lbl: seleccionar_arma(n, l))

frame_lugar = tk.Frame(root, bg="#f5f5dc")
frame_lugar.pack(pady=10)
tk.Label(frame_lugar, text="Selecciona el lugar:", bg="#f5f5dc").pack()
lugar_imgs = []

def seleccionar_lugar(nombre, img_label):
    selected_lugar.set(nombre)
    img_label.config(bg="#d1ffd1")

for l in locaciones:
    img = cargar_imagen(l['imagen'], 80, 80)
    lugar_imgs.append(img)
    lbl = tk.Label(frame_lugar, image=img, bd=2, relief="solid")
    lbl.pack(side="left", padx=5)
    lbl.bind("<Button-1>", lambda e, n=l['nombre'], lab=lbl: seleccionar_lugar(n, lab))

# ----- Verificar respuesta -----
def verificar_respuesta():
    if (selected_culpable.get() == culpable['nombre'] and
        selected_arma.get() == arma['nombre'] and
        selected_lugar.get() == lugar['nombre']):
        messagebox.showinfo("Resultado", "¡Felicidades! Has adivinado correctamente el caso.")
    else:
        solucion = f"Culpable: {culpable['nombre']}\nArma: {arma['nombre']}\nLugar: {lugar['nombre']}"
        messagebox.showinfo("Resultado", f"No es correcto. La solución era:\n{solucion}")

tk.Button(root, text="Verificar respuesta", command=verificar_respuesta, bg="#2196f3", fg="white").pack(pady=15)

root.mainloop()
