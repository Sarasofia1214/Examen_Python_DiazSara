from modulos import ModuloUsuario, eliminarusuario, mostrarusuario, menu, menuuser
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

menu()
opc=int(":")
if opc==2:
    ModuloUsuario()
    opp=int("")
    if opp==2:
        nomn=input(int("Ingrese el nombre del usuario nuevo:"))
        dicn=input(int("Ingrese la direccion del nuevo usuario:"))
        infon=input(int("Ingrese la informacion de contacto del nuevo cliente:"))

        clientes={
        "Nombre completo":nomn,
        "Direccion:":dicn,
        "Informacion contacto":infon
        }
        clientes.append(clientes)
        guardarJSON

    elif opp==2:
        mostrarusuario()

    elif opp==3:
        usuario=abrirJSON
        doc=int("Ingrese el nombre del usuario al cual quiere eliminar")
        for usuario in clientes:
            usuario.pop()
            eliminarusuario()
    elif opp==4:
        print("")
elif opc==1:
    menuuser()
    opcuser=int(":")
    if opcuser==1:
        Usuario=abrirJSON
        print("Ingrese su numero de usuario:")
        for Usuario in clientes:















  
    
    