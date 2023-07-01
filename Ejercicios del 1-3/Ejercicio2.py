from pyfiglet import Figlet
import random
figlet = Figlet()
fuentes_disponibles = figlet.getFonts()
fuente = input("Ingrese una fuente a utilizar: ")
if not fuente:
    fuente = random.choice(fuentes_disponibles)
if fuente not in fuentes_disponibles:
    print("Error: Fuente no disponible.")
else:
    texto = input("Ingrese un texto: ")
    figlet.setFont(font=fuente)
    print(figlet.renderText(texto))

    


