#Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y
#lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista:
#deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el
#mensaje utilizando el carácter =.
def centrado(parametro):
    tamcadena=len(parametro)
    tamespaciado=(int)((170-tamcadena)/2)
    textocentrado=""
    for i in range(0,tamespaciado):
        textocentrado= textocentrado + " "
    print(textocentrado + parametro)

parametro=input("Introduzca un parametro :")
centrado(parametro)

