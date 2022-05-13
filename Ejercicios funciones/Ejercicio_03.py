#Crear una función que calcule la temperatura media de un día a partir de la
#temperatura máxima y mínima. Crear un programa principal, que utilizando la
#función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y
#vaya mostrando la media. El programa pedirá el número de días que se van a
#introducir.

def tempmedia(dias):
    while dias!=0:
        tempmax=(int)(input("Introduzca La temperatura maxima."))
        tempmin=(int)(input("Introduzca la temperatura min"))
        media=((tempmax+tempmin)/2)
        dias=(int)(dias-1)
        print("La media es", media)
    


dias=(int)(input("¿De cuantos dias vamos a calcular la  temperatura?"))
tempmedia(dias)
