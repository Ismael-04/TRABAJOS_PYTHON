#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una
#contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la
#contraseña es “asdasd”. Además recibe el número de intentos que se ha
#intentado hacer login y si no se ha podido hacer login incremente este valor.
def peticion():
    usu=input("Introduzca su usuario.....")
    contra=input("Introduzca la contraseña.....")
    
    vloga.append(usu)
    vloga.append(contra)
    return vloga

def Login(vloga):

    contra=vloga[1]
    print (contra)
vloga=[]
peticion()
Login(vloga)