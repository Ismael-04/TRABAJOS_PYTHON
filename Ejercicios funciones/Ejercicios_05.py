#Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico 
#y devuelve el valor máximo y el mínimo. Crea un programa que pida números 
#por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
def calcularMaxMin (vector):
    max=vector[0]
    min=vector[0]
    vminmax=[]
    for i in vector:
        if i>max:
            max=i
        if i<min:
            min=i
    vminmax.append(min)
    vminmax.append(max)
    return vminmax


vez=(int)(input("¿Cuantos numeros vas a introduci?: "))

vector=[]
while vez!=0:
    vector.append((int)(input("Introduzca una coordenada del vector ... ")))
    vez=vez-1

print(calcularMaxMin (vector))

