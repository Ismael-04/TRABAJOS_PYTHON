#Realizar un programa que dada una cadena de caracteres por caracteres, 
#genere otra cadena resultado de invertir la primera

cadena=input("Introduzca una cadena de caracteres.")
tam=len(cadena)-1
while (tam>=0):
    print(cadena[tam],end="")
    tam=tam-1