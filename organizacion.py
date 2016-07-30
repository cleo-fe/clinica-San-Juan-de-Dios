import os
import sys
import time
import sqlite3
def menu():
    os.system("cls")
    os.system("color e")
    op = "0"
    opcion= ["Inicio","Servicios","Registro","Staff Medico","Salir"]
    while(op == "0"):
        print("////////////////////////////////////////////////////////////////////////")
        print("\n========================CLINICA SAN JUAN DE DIOS========================\n")
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
    os.system("cls")
    resu =open('inicio.txt','r')
    lineas=resu.readlines()
    for l in lineas:
        print (l)
    resu.close()
    print("")
    input("\t\t--------PRESIONE ENTER PARA REGRESAR AL MENU------")
    menu()

def servicios():
    op = "0"
    ser = ["Hospitalizacion","Maternidad","Farmacia","Laboratorio","Ambulancia","Chequeos Preventivos","Consultorio Externo","Nutricion - cafeteria","Unidad de Cuidados Intensivos","Emergencias","Centro Quirúrgico","Oftalmología","Odontología","Rehabilitación","Video endoscopias","Tomografías","Gabinete Cardiólogo","Gabinete Neurológico ","Esterilización ","Aula Virtual Hospitalaria ","","","","","","","","","","","","","","","","","","",""]
    while(op == "0"):
        print("\n\t\t======SERVICIOS DE LA CLINICA SAN JUAN DE DIOS======")
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
        print("\t=================INSCRIPCION=====================")
        print("\nIngrese los siguentes Datos: ")
        print("Servicio:{0}".format(servicio))
        nombre = str(input("Nombre: "))
        apellidopaterno = str(input( "Apellido Paterno: " ))
        apellidomaterno = str(input( "Apellido Materno: " ))
        dni = str(input("Numero de D.N.I: "))
        edad = int(input("Edad: "))
        peso = str(input( "Peso: " ))
        Especialidad = str(input( "Especialidad a Atenderse: " ))
        médico =  str(input( "Medico que le Atiende: " ))
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("INSERT INTRO registro (Servicio, Nombre, Apellidopaterno,Apellidomaterno, Dni, Edad,Peso,Especialidad,Medico) VALUES ('"+servicio+"','"+nombre+"','"+apellidopaterno+"','"+apellidomaterno+"','"+dni+"','"+edad+"','"+peso+"','"+Especialidad+"','"+médico+"')")
        con.commit()
        print("//////////////////////////////////////////////////////////////////")
        print("//////////////////USTED SE REGISTRO CON EXITO/////////////////////")
        print("")
        input("-------------Presione enter para regresar al menu-----------------")
        os.system("cls")
        con.close()
        registro_menu()

    def mostrar(self):
        os.system("cls")
        print("\t============REGISTRO CLINICA SAN JUAN DE DIOS==============")
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registros")
        for i in cursor:
            print("============================================================")
            print("Historia Clinica Numero:" ,i[0])
            print("Servicio:" , i[1])
            print("Nombre:" ,i[2])
            print("Apellido Paterno:" ,i[3])
            print("Apellido Materno:" ,i[4])
            print("DNI:" ,i[5])
            print("Edad:",i[6])
            print("Peso:" ,i[7])
            print("Especialidad:" ,i[8])
            print("Medico:" ,i[9])
        print("/////////////////////////////////////////////////////////////////////////")
        input("--------------------Presione enter para regresar al menu------------------")
        os.system("cls")
        con.close()
        registro_menu()

    def mostrar_Reg(self):
        os.system("cls")
        print("\t===========MODIFICAR REGISTRO CLINICA SAN JUAN DE DIOS============")
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registros")
        for i in cursor:
            print("Historia Clinica Numero:" ,i[0])
            print("Servicio:" , i[1])
            print("Nombre:" ,i[2])
            print("Apellido Paterno:" ,i[3])
            print("Apellido Materno:" ,i[4])
            print("DNI:" ,i[5])
            print("Edad:",i[6])
            print("Peso:" ,i[7])
            print("Especialidad:" ,i[8])
            print("Medico:" ,i[9])
            print("============================================================")
        codigo=input("Presione Numero de Historia Clinica que desea modificar:  ")
        print("Ingrese los datos a modificar")
        servicio = servicios()
        print("\nIngrese Datos: ")
        print("Servicio:{0}".format(servicio))
        nombre = str(input("Nombre: "))
        apellidopaterno = str(input( "Apellido Paterno: " ))
        apellidomaterno = str(input( "Apellido Materno: " ))
        dni = str(input("Numero de D.N.I: "))
        edad = str(input("Edad: "))
        peso = str(input( "Peso: " ))
        Especialidad = str(input( "Especialidad a Atenderse: " ))
        médico =  str(input( "Medico que le Atiende: " ))
        cursor.execute("update Registros set Servicio ='"+servicio+"', Nombre ='"+nombre+"', Apellidopaterno ='"+apellidopaterno+"',Apellidomaterno ='"+apellidomaterno+"', Dni ='"+dni+"', Edad ='"+edad+"',Peso ='"+peso+"',Especialidad ='"+Especialidad+"',Medico ='"+médico+"' where HistoriaClinicaNumero = '"+codigo+"'")
        con.commit()
        print("Historial clinico Modificado exitosamente ..........")
        input("-------------Presione enter para regresar al menu-----------------")
        os.system("cls")
        con.close()
        registro_menu()

    def eliminar(self):
        os.system("cls")
        print("\t===========ELIMINAR REGISTRO CLINICA SAN JUAN DE DIOS==============")
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registros")
        for i in cursor:
            print("Historia Clinica Numero:" ,i[0])
            print("Servicio:" , i[1])
            print("Nombre:" ,i[2])
            print("Apellido Paterno:" ,i[3])
            print("Apellido Materno:" ,i[4])
            print("DNI:" ,i[5])
            print("Edad:",i[6])
            print("Peso:" ,i[7])
            print("Especialidad:" ,i[8])
            print("Medico:" ,i[9])
            print("============================================================")
        codigo=input("PRESIONE EL NUMERO DE ISTORIAL CLINICO QUE DESEA ELIMINAR:  ")
        cursor.execute("delete from Registros where HistoriaClinicaNumero = '"+codigo+"'")
        con.commit()
        print("Historial Clinico Eliminado exitosamente ......")
        input("-----------------Presione enter para regresar al menu----------------------")
        os.system("cls")
        con.close()
        registro_menu()

def registro_menu():
    os.system("cls")
    op = 0
    r = Registro()
    list = ["Inscripcion","Mostrar Inscripcion","Modificar Inscripcion","Eliminar Inscripcion","Atras"]
    while(op not in [1,2,3,4,5]):
        print("\n\t=======REGISTRO DE LA CLINICA SAN JUAN DE DIOS==========")
        print("")
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
    os.system("cls")
    print("\t\t===========STAFF MEDICO===========")
    print("")
    opc = 0
    esp = ["Alergia e Inmunología","Anestesiología","Cardiología","Cir. Torácica y Cardiovascular","Cirugía Coloproctológica","Cirugía de Cabeza y Cuello","Cirugía General","Cirugía General y Oncológica","Cirugía Oncológica","Cirugía Pediátrica","Cirugía Plastica y Reparadora","Dermatología","Endocrinología","Gastroenterología","Geriatría","Ginecología y Obstetricia","Hematología","Infectología","Medicina Física y Rehabilitación ","Medicina General","Medicina Intensiva","Medicina Intensiva Pediatrica","Medicina Interna","Medico Cirujano","Nefrología","Neumología","Neurocirugía","Neurología","Nutricionista","Obstretricia","Odontología","Oftalmología","Oncologia Medica","Ortopedia y Traumatología","Otorrinolaringología","Pediatría","Psicología","Psiquiatría","Radiología","Reumatología","Urología","Atras"]
    while(opc not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]):
        print("\n\t==ESPECIALIDADES==")
        print("")
        print(" 1.- {}\n 2.- {}\n 3.- {}\n 4.- {}\n 5.- {}\n 6.- {}\n 7.- {}\n 8.- {}\n 9.- {}\n 10.- {}\n 11.- {}\n 12.- {}\n 13.- {}\n 14.- {}\n 15.- {}\n 16.- {}\n 17.- {}\n 18.- {}\n 19.- {}\n 20.- {}\n 21.- {}\n 22.- {}\n 23.- {}\n 24.- {}\n 25.- {}\n 26.- {}\n 27.- {}\n 28.- {}\n 29.- {}\n 30.- {}\n 31.- {}\n 32.- {}\n 33.- {}\n 34.- {}\n 35.- {}\n 36.- {}\n 37.- {}\n 38.- {}\n 39.- {}\n 40.- {}\n 41.- {}\n 42.- {}".format(esp[0],esp[1],esp[2],esp[3],esp[4],esp[5],esp[6],esp[7],esp[8],esp[9],esp[10],esp[11],esp[12],esp[13],esp[14],esp[15],esp[16],esp[17],esp[18],esp[19],esp[20],esp[21],esp[22],esp[23],esp[24],esp[25],esp[26],esp[27],esp[28],esp[29],esp[30],esp[31],esp[32],esp[33],esp[34],esp[35],esp[36],esp[37],esp[38],esp[39],esp[40],esp[41]))
        opc = str(input("\nIngrese un opcion: "))
        try:
            opc = int (opc)
            if opc not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]:
                print("Opcion incorrecta, Vuelva a intentarlo")
                time.sleep(2)
                os.system("cls")
        except ValueError:
            print("Ingrese solo digitos")
            time.sleep(3)
            opc = 0
        os.system("cls")
    if opc == 1:
        print("\t\t====Alergia e Inmunología====")
        print("\n1.-Dr. Félix César Ortiz Herrera\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 2:
        print("\t\t====Anestesiología====")
        print("\n1.-Dr. Félix César Ortiz Herrera\n2.-Dra. Socorro Bedregal Casapia\n3.-Dra. María Soledad Sotomayor Cabrera\n4.-Dra. Bernardina Cecilia Sánchez Gamero\n5.-Dr. Wilfredo Víctor Gutiérrez Manrique\n6.-Dr. Percy Sánchez Bedoya\n7.-Dr. Martin Recabarren Postigo\n8.-Dr. José Alfonso Zuñiga Rodríguez\n9.-Dr. Jorge José Luis Constantini Lazo\n10.-Dr. Hugo Jacinto Calisaya Luque\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 3:
        print("\t\t====Cardiología====")
        print("\n1.-Dra. María Gabriela Zavala Vinces\n2.-Dr. William Pompeyo Mora López\n3.-Dr. Roberto Arnaldo Salazar Huajardo\n4.-Dr. Ranuldo Roberto Bottazzi Alvarez\n5.-Dr. Percy Arrieta Alarcón\n6.-Dr. Pedro Torres Eguiluz\n7.-Dr. Néstor Camargo Salcedo\n8.-Dr. Nassip Carlojusto Llerena Navarro\n9.-Dr. Juan Carlos Gonzales Altamirano\n10.-Dr. Héctor Eduardo Molina Calle\n11.-Dr. Helard Luna Rivera\n12.-Dr. Elvis Prado Quintanilla\n13.-Dr. Alfredo Gama Medrano\n14.-Dr. Alejandro Boza Revilla\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 4:
        print("\t\t====Cir. Torácica y Cardiovascular====")
        print("\n1.- Dr. Rodolfo Jesús Alarcón Pinto\n2.-Dr. Rafael Arrarte Congrains\n3.-Dr. Juan Orlando Alca Salazar\n4.-Dr. Guillermo Rodríguez Chirinos\n5.-Dr. Félix Fernando Bustinza Menéndez\n6.-Dr. Ernesto Alonzo Rafael León Bejarano\n7.-Dr. Edgar Custodio Gaspar Montanchez Carazas\n8.-Dr. Aurelio Franklin Merello Vela\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 5:
        print("\t\t====Cirugía Coloproctológica====")
        print("\n1.-Dr. Edgar Rivera Díaz")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 6:
        print("\t\t====Cirugía de Cabeza y Cuello====")
        print("\n1.-Dr. Ricardo Rene Gomez Galindo\n2.-Dr. Luis Ricardo Marca Bueno\n3.-Dr. Jimmy Rubén Vilca Vargas\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 7:
        print("\t\t====Cirugía General====")
        print("\n1.-Dr. Teodoro Guillermo Vargas Bernal\n2.-Dr. Pedro Manuel Tamayo Tapia\n3.-Dr. Marco Antonio Merma Carpio\n4.-Dr. Marco Antonio Delgado Gonzáles\n5.-Dr. Lazaro Eliud Barriga Valencia\n6.-Dr. José Antonio Linarez Tejada\n7.-Dr. Ignacio Ballón Landa\n8.-Dr. Hernan Simón Barreda Tamayo\n9.-Dr. Fernando René Marquez Muñoz\n10.-Dr. Eugenio Ernesto Plazolles Del Carpio\n11.-Dr. Duilio Arnoulfo Valdivia Tejada\n12.-Dr. César Arturo Vargas Muñoz\n13.-Dr. Cristóbal José Eduardo La Torre Gallegos\n14.-Dr. Alvaro Enrique Valdez Galdos\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 8:
        print("\t\t====Cirugía General y Oncológica====")
        print("\n1.-Dr. Luis Enrique Medina Fernández\n2.-Dr. Adolfo Lucio Morán Cárdenaz\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 9:
        print("\t\t====Cirugía Oncológica====")
        print("\n1.-Dr. Walter Grimaldo Fernandez Mendoza\n2.-Dr. Edwin Jesús Gonzáles Chávez\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 10:
        print("\t\t====Cirugía Pediátrica====")
        print("\n1.-Dr. Jorge Valdivia Tejada")
        input("\t--------Presione enter para regresar--------")
        staff_medico()

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

