
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
    with open("./quejas.json",'w') as outFile:
        json.dump(dic,outFile)

clientes=abrirJSON
quejas=abrirJSON
booleano=True
while booleano==True:
    print("Como desea ingresar")
    print("1. Usuario")
    print("2. Coordinador")
    print("3. Salir del programa")
    opc=int(input(":"))
    if opc==2:
        print("1. Crear un nuevo usuario")
        print("2. Mostrar los usuarios")
        print("3. Eliminar un usuario")
        print("4. Asignar categoria de usuario")
        print("5. Modulo Gestion Servicios")
        print("6. Modulo reportes")
        print("5. Salir del programa")
        opp=int(input(":"))
        if opp==2:
            nomn=int(input("Ingrese el nombre del usuario nuevo:"))
            dicn=int(input("Ingrese la direccion del nuevo usuario:"))
            infon=int(input("Ingrese la informacion de contacto del nuevo cliente:"))
            clientes={
            "Nombre completo":nomn,
            "Direccion:":dicn,
            "Informacion contacto":infon
            }
            clientes.append(clientes)
            guardarJSON
            print("Estudiante gaurdado exitosamente")

        elif opp==2:
            opcc=input(int("Ingrese su nombre"))
            if (opcc in clientes):
                print(["Nombre"])
                for cliente in clientes:
                    nomcli={"Nombre"}
                    print(len("Los clientes son:", nomcli) )

        elif opp==3:
            usuario=abrirJSON
            doc=int(input("Ingrese el nombre del usuario al cual quiere eliminar"))
            for usuario in clientes:
                usuario.pop()
                clientes=abrirJSON
                for usuario in clientes:
                    print("")
        elif opp==4:
            for categoria in clientes:
                print("")
        
        elif opp==5:
            print("Agregar")






    elif opc==1:
            print("Bienvenido usuario:")
            print("Ingrese el numero de la opcion a escoger:")
            print("1. Ingresar al perfil")
            print("2. Realizar reclamaciones, sugerencias o consultas")
            print("3. Salir del programa")
            opcuser=int(input(":"))
            if opcuser==1:
                Usuario=abrirJSON
                print("Ingrese su numero de usuario:")
                for Usuario in clientes:
                    print({clientes})

    elif opc==3:
        break















  
    
    