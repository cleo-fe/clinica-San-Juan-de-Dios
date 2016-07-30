import os
import sys
import time
import sqlite3
def menu():
    os.system("cls")
    print("\t\t--MENU--")
    print()
    print("\t1.-Nuevo Ingreso")
    print("\t2.-Buscar por N° de historia clinica")
    print("\t3.-Buscar por N° de DNI")
    print("\t4.-Buscar por Apellido Paterno y Nombre")
    print("\t5.-Salir")
    print()
    opcion=int(input("Digite una opcion: "))
    if opcion==1:
        os.system("cls")
        nuevo()
    elif opcion==2:
        os.system("cls")
        historia()
    elif opcion==3:
        os.system("cls")
        dnii()
    elif opcion==4:
        os.system("cls")
        apeynom()
    elif opcion==5:
        os.system()
        salir()
    else:
        print("Opcion incorrecta vuelva a ingresar")
        time.sleep(2)
        menu()

def nuevo():
    print("Nuevo Paciente")
    print()
    print("Ingrese los datos:")
    dni=input("DNI: ")
    apellidopaterno=input("Apellido Paterno: ")
    apellidomaterno=input("Apellido Materno: ")
    nombre=input("Nombre: ")
    edad=input("Edad: ")
    peso=input("Peso: ")
    especialidad=input("Espacialidad en la que se atiende: ")
    medico=input("Medico con el que se atiende: ")
    con=sqlite3.connect("pacientes.s3db")
    cursor=con.cursor()
    cursor.execute("insert into Registros(DNI, ApellidoPaterno, ApellidoMaterno, Nombre, Edad, Peso, Especialidad, Medico) values ('"+dni+"','"+apellidopaterno+"','"+apellidomaterno+"','"+nombre+"','"+edad+"','"+peso+"','"+especialidad+"','"+medico+"')")
    con.commit()
    con.close()
    print()
    print("¡Paciente registrado exitosamente!")

def historia():
    print("historia")

def dnii():
    print("deni")

def apeynom():
    print("apeynom")

def salir():
    opcion2=input("¿Esta seguro que desea salir?(si/no): ")
    if opcion2.lower()=='si':
        print("El programa se esta cerrando...")
        time.sleep(2)
        sys.exit(1)
    elif opcion2.lower()=='no':
            os.system("cls")
            menu()