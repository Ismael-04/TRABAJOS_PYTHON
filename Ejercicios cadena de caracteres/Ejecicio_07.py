#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
#sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena=input("Introduzca una cadena de caracteres ")
cadena2=""

caracter=input ("Introduce un caracter ").upper()
caracter= ord(caracter)
if (caracter>=65 and caracter<=90):
    print("Caracter es valido ")


caracter2=input ("Introduce un caracter ").upper()
caracter2= ord(caracter2)
if (caracter2>=65 and caracter2<=90):
    print("El segundo caracter es valido ")


i=0
tam=len(cadena)
while i<tam:
    if cadena[i]==chr(caracter).lower():
       cadena2=cadena2+chr(caracter2).lower()
    else:
        cadena2=cadena2+cadena[i]
    i=i+1    

print(cadena2)