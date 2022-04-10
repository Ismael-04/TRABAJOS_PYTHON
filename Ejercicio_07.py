#Realizar una algoritmo que muestre la tabla de multiplicar de un número
#introducido por teclado.


numero=int(input("Introduzca un número.   "))

print("La tabla del ",numero,"es :")
for i in range(0,11):
    print(i,"x",numero,"=",numero*i)

    