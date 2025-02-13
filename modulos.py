import json
def abrirJSON():
    dicFinal={}
    with open('./clientes','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./clientes.json",'w') as outFile:
        json.dump(dic,outFile)
def abrirJSON():
    dicFinal={}
    with open('./quejas','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./qiejas.json",'w') as outFile:
        json.dump(dic,outFile)

clientes=abrirJSON
quejas=abrirJSON
def menu():
    print("Como desea ingresar")
    print("1. Usuario")
    print("2. Coordinador")

def ModuloUsuario():
    print("1. Crear un nuevo usuario")
    print("2. Mostrar los usuarios")
    print("3. Eliminar un usuario")
    print("4. Asignar categoria de usuario")
    print("5. Salir del programa")
    opp=int("")


def mostrarusuario():
cliente={
    "Nombre":nomn}
    
for cliente in clientes:
    nomcli={"Nombre"}
    print(len("Los clientes son:", nomcli) )



def eliminarusuario():
for usuario in clientes:
    print("")

def menuuser ():
    print("Bienvenido usuario:")
    print("Ingrese el numero de la opcion a escoger:")
    print("1. Ingresar al perfil")
    print("2. Realizar reclamaciones, sugerencias o consultas")