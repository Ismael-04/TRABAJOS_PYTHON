#Suponiendo que hemos introducido una cadena por teclado que representa una 
#frase (palabras separadas por espacios), realiza un programa que cuente 
#cuantas palabras tiene.


cadena=input("Introduzca una cadena de caracteres ")
contador=0

for i in cadena:
    if(i==" "):
        contador=contador+1

print("La cadena tiene ", contador+1,"palabras")
