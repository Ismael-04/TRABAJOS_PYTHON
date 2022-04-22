#Realizar un programa que comprueba si una cadena leída por teclado comienza
#por una subcadena introducida por teclado.


cadena=input("Dime una cadena de caracteres. ")
subcadena=input("Dime una subcadena de caracteres. ")

cadena.upper


if (subcadena == cadena[0:len(subcadena)]):
    print("La cadena leída por teclado comienza por una subcadena introducida por teclado")
else: print("La cadena leída por teclado no comienza por una subcadena introducida por teclado")