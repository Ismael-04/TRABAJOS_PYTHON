#Crea un programa que pida dos número enteros al usuario y diga si alguno de
#ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos
#números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(n1,n2):
    resto= n1%n2
    if resto== 0 :
        return True
    else:
        return False



n1=(int)(input("Introduzca un numero : "))
n2=(int)(input("Introduzca un numero : "))
if EsMultiplo(n1,n2) == True:
    print("Son multiplos.")
else:
    print ("No son multiplos")
