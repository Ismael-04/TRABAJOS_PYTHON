#Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
#muestre las iniciales en mayúsculas.

cadena=input("Introduzca su nombre y apellidos .").lower()

print(cadena[0].upper(), end="")
cont=1

while(cont<len(cadena)):
    if(cadena[cont]==" "):
        print(" ", cadena[cont+1].upper(), end=" ")
        cont=cont+1
    else:
        print(cadena[cont], end=" ")

    cont=cont+1