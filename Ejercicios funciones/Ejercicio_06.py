#Diseñar una función que calcule el área y el perímetro de una circunferencia. 
#Utiliza dicha función en un programa principal que lea el radio de una 
#circunferencia y muestre su área y perímetro

def ayp(rad):
    print("El perimetro es ",(rad*rad)*3.14)
    print("El area es ", 2*3.14*rad)


rad=(int)(input("Introduzca el radio de la circunferencia : "))
ayp(rad)