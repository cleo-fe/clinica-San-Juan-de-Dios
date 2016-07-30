import os
import sys
import time
import sqlite3

def menu():
    op = "0"
    opcion= ["Inicio","Servicios","Registro","Staff Medico","Salir"]
    while(op == "0"):
        print("\nClinica San Juan de Dios\n")
        print(" 1.- {}\n 2.- {}\n 3.- {}\n 4.- {}\n 5.- {}".format(opcion[0],opcion[1],opcion[2],opcion[3],opcion[4]))
        op = str(input("\nIngrese un opcion: "))
        if op not in ["1","2","3","4","5","6","7"]:
            print("Opcion incorrecta, Vuelva a intentarlo!")
            time.sleep(2)
            op = "0"
        os.system("cls")
    if (op == "1"):
        inicio()
    elif (op == "2"):
        servicios()
    elif (op == "3"):
        registro_menu()
    elif (op == "4"):
        staff_medico()
    elif (op == "5"):
        salir()


def inicio():

    resu =open('inicio.txt','r')
    lineas=resu.readlines()
    for l in lineas:
        print (l)
    resu.close()

def servicios():
    op = "0"
    ser = ["Hospitalizacion","Maternidad","Farmacia","Laboratorio","Ambulancia","Chequeos Preventivos","Consultorio Externo","Nutricion - cafeteria","Unidad de Cuidados Intensivos","Emergencias","Centro Quirúrgico","Oftalmología","Odontología","Rehabilitación","Video endoscopias","Tomografías","Gabinete Cardiólogo","Gabinete Neurológico ","Esterilización ","Aula Virtual Hospitalaria ","","","","","","","","","","","","","","","","","","",""]
    while(op == "0"):
        print("\n\tSERVICIOS DE LA CLINICA SAN JUAN DE DIOS:")
        print("")
        print(" 1.- {}\n 2.- {}\n 3.- {}\n 4.- {}\n 5.- {}\n 6.- {}\n 7.- {}\n 8.- {}\n 9.- {}\n 10.- {}\n 11.- {}\n 12.- {}\n 13.- {}\n 14.- {}\n 15.- {}\n 16.- {}\n 17.- {}\n 18.- {}\n 19.- {}\n 20.- {}".format(ser[0],ser[1],ser[2],ser[3],ser[4],ser[5],ser[6],ser[7],ser[8],ser[9],ser[10],ser[11],ser[12],ser[13],ser[14],ser[15],ser[16],ser[17],ser[18],ser[19]))
        op = str(input("\nIngrese un opcion: "))
        if op not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
            print("Opcion incorrecta, Vuelva a intentarlo")
            time.sleep(2)
            op = "0"
        os.system("cls")
    aux = int(op)-1
    cont = ser[aux]
    return cont

class Registro:
    def __init__(self):
        self.Servicio = ""
        self.Nombre = ""
        self.Apellido = ""
        self.Dni = ""
        self.Edad = ""

    def inscripcion(self):
        os.system("cls")
        servicio = servicios()
        print("\n Ingrese los siguentes Datos: ")
        print("Servicio:{0}".format(servicio))
        nombre = str(input("Nombre: "))
        apellido = str(input("Apellido: "))
        dni = str(input("Numero de D.N.I: "))
        edad = int(input("Edad: "))

        con = sqlite3.connect("pacientito.s3db")
        cursor = con.cursor()
        cursor.execute("INSERT INTRO registro (Servicio, Nombre, Apellido, Dni, Edad) VALUES ('"+servicio+"','"+nombre+"','"+apellido+"','"+dni+"','"+edad+"')")
        con.commit()
        con.close()
        print("Usted se registro con exito")

    def mostrar(self):
        os.system("cls")
        cont = servicios()

def registro_menu():
    op = 0
    r = Registro()
    list = ["Inscripcion","Mostrar Inscripcion","Modificar Inscripcion","Eliminar Inscripcion","Atras"]
    while(op not in [1,2,3,4,5]):
        print("\n\tREGISTRO")
        print(" 1.- {}\n 2.- {}\n 3.- {}\n 4.- {}\n 5.- {}\n".format(list[0],list[1],list[2],list[3],list[4]))
        op = input("Ingrese una opcion: ")
        try:
            op = int(op)
            if op not in [1,2,3,4,5]:
                print("Opcion incorrecta, Vuelva a intentarlo")
                time.sleep(2)
                os.system("cls")
        except ValueError:
            print("Ingrese solo digitos")
            time.sleep(5)
            op = 0

    if(op == 1):
        r.inscripcion()
    elif(op == 2):
        r.mostrar()
    elif(op == 3):
        r.mostrar_Reg()
    elif(op == 4):
        r.eliminar()
    elif(op == 5):
        menu()

def staff_medico():
    print("")
def salir():
    b = 0
    while b == 0:
        os.system("cls")
        opp = input("Esta seguro que desea salir: (Escriba Si/No ): ")
        print()
        if opp.lower() == "si":
            b=1
            print("El programa esta cerrandose ...")
            time.sleep(2)
            sys.exit(1)
        elif opp.lower() == "no":
            b=1
        else:
            b=0
    menu()

