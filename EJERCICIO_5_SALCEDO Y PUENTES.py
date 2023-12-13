#Comentario 1: PREGUNTA EL RANGO DE PALABRAS INGRESADAS  
palabra = []

import random
from unittest import case
random.shuffle(palabra)
for i in range(20):
    palabra=input(f"Ingrese la palabra")

#Comentario 2: DEFINE EL ORDEN DE LAS PALABRAS 

def ordernar_por_tamaño(palabra):
    return sorted (palabra,key=len, reverse=True)

#Comentario 3: PREGUNTA AL USUARIO EN QUE ORDEN QUIERE SUS PALABRAS

while True:
     print("Seleccione una opcion")
     print ("1. Orden alfabetico")
     print("2. Orden de tamaño, de la mas larga a la mas corta")
     print("3. Orden aleatorio")
     print("4. Orden inverso al ingresado")
     print("5. Orden igual al ingresado")
     print("6. Salir")
     
     
     seleccion = input(f"Elija una opcion")
     match seleccion:
         case "1":
             print(palabras_ordenadas =sorted(input("palabra")))
         case "2":
             print(palabras_ordenadas = ordernar_por_tamaño(input("palabra")))
         case "3": 
             import random 
             random.shuffle(palabra)
             print(palabras_ordenadas = "palabra")
         case "4": 
             print(palabras_ordenadas = list(reversed(input("palabra"))))
         case "5":
             print(palabras_ordenadas = input ("palabras"))
         case"6":
            break
         case _ :
             print("Opcion no valida. Elija una opcion del 1 al 6")
             continue


#Comentario 4: NOS DA UN RESULTADO FINAL COMO LO INDICO EL USUARIO 
print("\nPalabras ordenadas:")
for palabra in palabras_ordenadas:
    print(palabra)
