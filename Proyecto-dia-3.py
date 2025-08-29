print("**** BIENVENIDO A PROYECTO 3 ******")

texto1 = input("Ingresa un texto, parrafo, frase celebre o lo que tu quieras: ")
print(f"este es tu texto: {texto1}")
print()
#Convirtiendo a minusculas #
textoFormateado = texto1.lower()
#Convirtiendo texto a una lista
textoLista = texto1.split()
# invirtiendo el texto
textoInvertido = texto1[::-1]
#Buscando si una palabra se encuentra en el texto en este caso era "python"
textoBusqueda = "python" in texto1
#presentando la respues al usuario convertido a "No" o "Si" dependiendo del texto
diccionario1 = {True : "Si", False: "No"}
print("Ahora ingresa una letra diferente cada vez que se te pida")
print()
letra1 = input("Ingresa la primer letra: ").lower()
letra2 = input("Ingresa la segundo letra: ").lower()
letra3 = input("Ingresa la tercer letra: ").lower()

print("A continuacion te mostrare algunas cosas interesantes de tu texto")
input("Press enter to continue")

print (f"Estas son tus tres letras: {letra1}, {letra2}, {letra3}")
print()
input("Press enter to continue")
print(f"La letra {letra1}, aparece {textoFormateado.count(letra1)} veces en el texto.")
print(f"La letra {letra2}, aparece {textoFormateado.count(letra2)} veces en el texto.")
print(f"La letra {letra3}, aparece {textoFormateado.count(letra3)} veces en el texto.")
input("Press enter to continue")
print()
print(f"El texto tiene en total {len(textoLista)} palabras.")
input("Press enter to continue")
print()
print(f"La primera letra del texto es {texto1[0]} y la ultima es {texto1[-1]}")
input("Press enter to continue")
print()
print(f"Aqui puedes ver las letras invertidas de todo el texto: {textoInvertido}")
input("Press enter to continue")
print()
print(f"la palabra Python {diccionario1[textoBusqueda == "python"]} se encuentra en el texto")
print()
input("Press enter to continue")
input("Espero te haya gustado el analisis, \npresiona enter para finalizar el programa")

