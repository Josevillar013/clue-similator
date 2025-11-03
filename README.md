# clue-similator

🕵️‍♂️ CLUE SIMULATOR - Juego de Misterio en Python
🎯 Descripción del proyecto

Este proyecto es un simulador del clásico juego de mesa “Clue” (Cluedo), desarrollado en Python.
El jugador debe adivinar quién fue el culpable, con qué arma y en qué lugar se cometió el crimen.
Cada partida genera imágenes visuales del resultado, mostrando si la elección fue correcta o incorrecta.

El proyecto incluye dos versiones:

🎮 Versión consola (clue.py): se juega por texto, compatible con cualquier terminal.

💻 Versión Notebook (clue_final.ipynb): incluye visualización de imágenes con PIL y matplotlib.

🧩 Características principales

5 personajes con profesiones distintas.

5 armas posibles del crimen.

5 locaciones donde puede haber ocurrido el hecho.

Generación aleatoria del culpable, arma y lugar.

Muestra imágenes aunque el jugador acierte o falle.

Puntaje automático y reporte de rondas.

Compatible con VS Code, GitHub Codespaces y Jupyter Notebook.

🧠 Cómo jugar

Clona el repositorio en tu entorno local o Codespaces:

git clone https://github.com/tuusuario/clue-simulator.git
cd clue-simulator


Asegúrate de tener Python instalado y las dependencias necesarias:

pip install pillow matplotlib ipywidgets


Si quieres jugar en consola, ejecuta:

python clue.py


Si prefieres la versión interactiva con imágenes, abre el archivo:

clue_final.ipynb


y ejecuta todas las celdas en Jupyter Notebook o Codespaces.

🖼️ Estructura del proyecto
clue-simulator/
│
├── clue.py                  # Versión de consola del juego
├── clue_final.ipynb         # Versión interactiva con imágenes
├── imagenes/                # Carpeta con personajes, armas y lugares
│   ├── personajes/
│   ├── armas/
│   └── lugares/
├── README.md                # Manual y descripción del proyecto
└── manual_usuario.pdf       # Reporte estilo manual de usuario

🧑‍💻 Tecnologías utilizadas

Python 3.10+

Pillow (PIL) – Para generar y manipular imágenes

Matplotlib – Para mostrar las imágenes en el notebook

Ipywidgets – Para botones e interacción en Jupyter Notebook

🧾 Puntaje del juego
Resultado	Descripción	Puntos
✅ Correcto	Adivina culpable, arma y lugar	3
❌ Incorrecto	Falla en alguno	1
🕹️ Ejemplo de partida

Jugador elige:

Culpable: Señorita Scarlet
Arma: Cuchillo
Lugar: Biblioteca

Resultado:

❌ Incorrecto
La solución real era: Profesor Plum con la Llave Inglesa en la Cocina.