def menu ():
    print("1-Ejercicio 1")
    print("2-Ejercicio 2")
    print("3-Salir")
def seleccionopcion():
    menu()
    opcion=0
    while (opcion<1 or opcion>3):
        opcion=(int)(input("Dame una opcion : "))
    return opcion


print("****Ejercicios con funciones****")
opc= 0

while (opc!=3):
    opc= seleccionopcion()
    match opc:
        case 1:
            print("Ejercicio 1")
        case 2:
            print("Ejercicio 2")
        case _:
            print("Adios")

    

