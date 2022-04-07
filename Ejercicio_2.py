import random

numero=random.randint(0,100)
intentos=10
numerointro=-1

numerointro = (int)(input("Dime un número"))

while intentos>0:
    numerointro=(int)(input("Dime un número"))

    intentos=intentos-1

    if numerointro==numero:
        break
    if numerointro>numero :
        print("El numero que estoy pensando es menor al introducido")
    if numerointro>numero :
        print("El numero que estoy pensando es mayor al introducido")

