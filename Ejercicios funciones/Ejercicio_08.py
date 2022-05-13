#Crear una función recursiva que permita calcular el factorial de un número.
#Realiza un programa principal donde se lea un entero y se muestre el resultado
#del factorial.
def fact(num):
    cont=1
    mult=0
    while cont!=num:
        mult=mult*cont
        cont=cont+1
    print(mult) 

num=(int)(input("Introduzca un numero :"))
fact(num)
