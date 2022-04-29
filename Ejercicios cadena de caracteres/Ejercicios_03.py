#Pide una cadena y un carácter por teclado (valida que sea un carácter) y
#muestra cuantas veces aparece el carácter en la cadena.
#Pide una cadena y un carácter por teclado (valida que sea un carácter) y 
#muestra cuantas veces aparece el carácter en la cadena.

cadena=input("Introduzca una cadena de caracteres ")
caracter=input ("Introduce un caracter ").upper()
caracter= ord(caracter)
cont=0

if (caracter>=65 and caracter<=90):
    print("Caracter es valido ")
    for aux in cadena:
        if (ord(aux.upper()) == caracter):
            cont=cont+1
caracter = chr(caracter)
print("La letra ", caracter,"ha sido introducida ", cont," veces.")