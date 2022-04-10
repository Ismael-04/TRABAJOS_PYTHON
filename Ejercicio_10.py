#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

numero=0

while numero!=5:
    numero=numero+1
    for i in range(0,11):
        print(i,"x",numero,"=",numero*i)

    