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
        print("/////////////////////////////////////////////////////////////////////////")
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

#=======================================INICIO=================================================================#

def inicio():
    os.system("cls")
    print("/////////////////////////////////////////////////////////////////////////\n")
    resu =open('inicio.txt','r')
    lineas=resu.readlines()
    for l in lineas:
        print (l)
    resu.close()
    print("")
    input("\t\t--------PRESIONE ENTER PARA REGRESAR AL MENU------")
    menu()
#=====================================SERVICIOS================================================================#
def servicios_menu():
    os.system("cls")
    op = 0
    s = Servicios()
    list = ["Nuevo Servicio a Agregar  ","Mostrar Servicios  ","Modificar Servicios ","Eliminar Servicio  ","Atras  "]
    while(op not in [1,2,3,4,5]):
        print("/////////////////////////////////////////////////////////////////////////")
        print("\n==============SERVICIOS DE LA CLINICA SAN JUAN DE DIOS=================\n")
        print("/////////////////////////////////////////////////////////////////////////")
        print("\n1.- {}\n\n2.- {}\n\n3.- {}\n\n4.- {}\n\n5.- {}\n\n".format(list[0],list[1],list[2],list[3],list[4]))
        op = input("\n\tIngrese una opcion: ")
        try:
            op = int(op)
            if op not in [1,2,3,4,5]:
                print("\n\tOpcion incorrecta, Vuelva a intentarlo\n")
                time.sleep(2)
                os.system("cls")
        except ValueError:
            print("\n==========================INGRESE SOLO DIGITOS===========================\n")
            time.sleep(3)
            os.system("cls")
            op = 0
    if(op == 1):
        s.NuevoServicio()
    elif(op == 2):
        s.MostrarServicio()
    elif(op == 3):
        s.ModificarServicio()
    elif(op == 4):
        s.EliminarServicio()
    elif(op == 5):
        menu()
class Servicios:
    def __init__(self):
        self.servicio=""
        self.adicional=""

    def NuevoServicio(self):
        os.system("cls")
        print("/////////////////////////////////////////////////////////////////////////")
        print("=======================NUEVO SERVICIO A AGREGAR==========================")
        print("/////////////////////////////////////////////////////////////////////////")
        servicionuevo=input("\m\tIngrese nuevo servicio:   \n")
        con = sqlite3.connect("Clinica-San-Juan-de-Dios.s3db")
        cursor = con.cursor()
        cursor.execute("insert into Registro (Servicios) values ('"+servicionuevo+"')")
        con.commit()
        con.close()
        print("\n//////////////////////////////////////////////////////////////////////////")
        print("\n//////////////////NUEVO SERVICIO REGISTRADO CON EXITO/////////////////////\n")
        print("//////////////////////////////////////////////////////////////////////////")
        input("\n------------------Presione enter para regresar al menu--------------------\n")
        os.system("cls")
        servicios_menu()

    def MostrarServicio(self):
        os.system("cls")
        print("//////////////////////////////////////////////////////////////////////////")
        print("===============SERVICIOS DE LA CLINICA SAN JUAN DE DIOS===================")
        print("//////////////////////////////////////////////////////////////////////////")
        con = sqlite3.connect("Clinica-San-Juan-de-Dios.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registro")
        print("\n==========================================================================\n")
        print("=================NUMERO=====================SERVICIO======================\n")
        for i in cursor:
            print("\t\t   ",i[0],"\t\t\t",i[1])
        con.close()
        print("\n/////////////////////////////////////////////////////////////////////////")
        input("\n-------------------Presione enter para regresar al menu------------------")
        os.system("cls")
        servicios_menu()
    def ModificarServicio(self):
        os.system("cls")
        print("/////////////////////////////////////////////////////////////////////////")
        print("=============MODIFICAR SERVICICIOS CLINICA SAN JUAN DE DIOS==============")
        print("/////////////////////////////////////////////////////////////////////////")
        con = sqlite3.connect("Clinica-San-Juan-de-Dios.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registro")
        print("\n==========================================================================\n")
        print("=================NUMERO=====================SERVICIO======================\n")
        for i in cursor:
            print("  \t\t",i[0],"\t\t\t",i[1])
        print("")
        codigo=input("\n\tSeleccione numero a modificar:  ")
        print("\n\tIngrese los datos a modificar\n")
        servicionuevo=input("\tIngrese nuevo servicio:   ")
        cursor.execute("update Registro set Servicios ='"+servicionuevo+"' where ID = '"+codigo+"'")
        con.commit()
        print("\n//////////////////////////////////////////////////////////////////////////")
        print("\n==================SERVICIO MODIFICADO EXITOSAMENTE=======================\n")
        print("\n//////////////////////////////////////////////////////////////////////////")
        input("-----------------Presione enter para regresar al menu--------------------")
        os.system("cls")
        con.close()
        servicios_menu()

    def EliminarServicio(self):
        os.system("cls")
        print("/////////////////////////////////////////////////////////////////////////")
        print("===============ELIMINAR SERVICIO CLINICA SAN JUAN DE DIOS================")
        print("/////////////////////////////////////////////////////////////////////////\n")
        con = sqlite3.connect("Clinica-San-Juan-de-Dios.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registro")
        print("=================NUMERO=====================SERVICIO======================\n")
        for i in cursor:
            print("  \t\t",i[0],"\t\t\t",i[1])
        print("\n===========================================================================\n")
        codigo=input("\tELIJA EL SERVICIO QUE DESEA ELIMINAR:  ")
        cursor.execute("delete from Registro where ID = '"+codigo+"'")
        con.commit()
        print("\n//////////////////////////////////////////////////////////////////////////")
        print("=====================SERVICIO ELIMINADO EXITOSAMENTE=======================")
        print("///////////////////////////////////////////////////////////////////////////")
        input("\n-----------------Presione enter para regresar al menu----------------------")
        os.system("cls")
        con.close()
        registro_menu()

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
        print("////////////////////////////////////////////////////////////////////////////////")
        print("\t=================INSCRIPCION=====================")
        print("////////////////////////////////////////////////////////////////////////////////\n")
        print("\n\tINGRESE LOS SIGUIENTES DATOS ")
        apellidopaterno = str(input( "\nApellido Paterno: " ))
        apellidomaterno = str(input( "\nApellido Materno: " ))
        nombre = str(input("\nNombre: "))
        dni = str(input("\nD.N.I: "))
        edad = str(input("\nEdad: "))
        print("Servicio:{0}".format(servicio))
        os.system("cls")
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("insert into Registros (ApellidoPaterno,ApellidoMaterno,Nombre,Dni,Edad,Servicio) VALUES ('"+apellidopaterno+"','"+apellidomaterno+"','"+nombre+"','"+dni+"','"+edad+"','"+servicio+"')")
        con.commit()
        print("\n////////////////////////////////////////////////////////////////////////////////")
        print("/////////////////////////USTED SE REGISTRO CON EXITO////////////////////////////")
        print("////////////////////////////////////////////////////////////////////////////////")
        input("\n-------------Presione enter para regresar al menu-----------------")
        os.system("cls")
        con.close()
        registro_menu()

    def mostrar(self):
        os.system("cls")
        print("///////////////////////////////////////////////////////////////////////////////")
        print("=======================REGISTRO CLINICA SAN JUAN DE DIOS=======================")
        print("///////////////////////////////////////////////////////////////////////////////")
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registros")
        print("\nNUMERO=============NOMBRES================DNI=========EDAD=========SERVICIO== \n")
        for i in cursor:
            print(" ",i[0],"    ",i[1],"",i[2],"",i[3],"      ",i[4],"      ",i[5],"    ",i[6])
        print("\n///////////////////////////////////////////////////////////////////////////////")
        input("\n--------------------Presione enter para regresar al menu-----------------------")
        os.system("cls")
        con.close()
        registro_menu()

    def mostrar_Reg(self):
        os.system("cls")
        print("///////////////////////////////////////////////////////////////////////////////")
        print("==================MODIFICAR REGISTRO CLINICA SAN JUAN DE DIOS==================")
        print("///////////////////////////////////////////////////////////////////////////////")
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registros")
        print("\nNUMERO=============NOMBRES================DNI=========EDAD=========SERVICIO== \n")
        for i in cursor:
            print(" ",i[0],"    ",i[1],"",i[2],"",i[3],"      ",i[4],"      ",i[5],"    ",i[6])
        print("\n////////////////////////////////////////////////////////////////////////////////")
        codigo=input("\n\t\tINDIQUE EL REGISTRO QUE DESEA MODIFICAR")
        print("\nIngrese los datos a modificar")
        print("\nIngrese Datos: ")
        apellidopaterno = str(input( "\nApellido Paterno: " ))
        apellidomaterno = str(input( "\nApellido Materno: " ))
        nombre = str(input("\nNombre: "))
        dni = str(input("\nNumero de D.N.I: "))
        edad = int(input("\nEdad: "))
        servicio = servicios()
        print("Servicio:{0}".format(servicio))
        cursor.execute("update Registros set ApellidoPaterno ='"+apellidopaterno+"',ApellidoMaterno ='"+apellidomaterno+"',Nombre ='"+nombre+"',Dni ='"+dni+"', Edad ='"+edad+"'Servicio ='"+servicio+"' where ID = '"+codigo+"'")
        con.commit()
        print("\n///////////////////////////////////////////////////////////////////////////////")
        print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
        print("///////////////////////////////////////////////////////////////////////////////")
        input("\n---------------------Presione enter para regresar al menu----------------------")
        os.system("cls")
        con.close()
        registro_menu()

    def eliminar(self):
        os.system("cls")
        print("///////////////////////////////////////////////////////////////////////////////")
        print("==================ELIMINAR REGISTRO CLINICA SAN JUAN DE DIOS===================")
        print("///////////////////////////////////////////////////////////////////////////////")
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registros")
        print("\nNUMERO=============NOMBRES================DNI=========EDAD=========SERVICIO== \n")
        for i in cursor:
            print(" ",i[0],"    ",i[1],"",i[2],"",i[3],"      ",i[4],"      ",i[5],"    ",i[6])
        print("\n////////////////////////////////////////////////////////////////////////////////")
        codigo=input("\n\tINDIQUE QUE REGISTRO DESEA ELIMINAR :  ")
        cursor.execute("delete from Registros where ID = '"+codigo+"'")
        con.commit()
        print("\n///////////////////////////////////////////////////////////////////////////////")
        print("====================HISTORIA CLINICA ELIMINADA EXITOSAMENTE====================")
        print("///////////////////////////////////////////////////////////////////////////////")
        input("\n---------------------Presione enter para regresar al menu----------------------")
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
#========================================STAFF MEDICO==================================================================#
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
    elif opc == 11:
        print("\t\t====Cirugía Plastica y Reparadora====")
        print("\n1.-Dra. Segunda Pascuala Rubio Barrios\n2.-Dr. Salvador Rodríguez Suca\n3.-Dr. Ralph Renato Almonte Velarde\n4.-Dr. José Manuel Zegarra Lopez\n5.-Dr. Abraham Americo Ocharan Miranda\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 12:
        print("\t\t====Dermatología====")
        print("\n1.-Dra. Lilia Zapata Carcamo\n2.-Dra. Claudia Karen Salas Ortega\n3.-Dr. Robert Edwin Zegarra Del Carpio\n4.-Dr. Pablo Renia Butron Bernal\n5.-Dr. Marcial Rios Flores\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 13:
        print("\t\t====Endocrinología====")
        print("\n1.-Dr. Ricardo Paolo Jiménez Orbegoso\n2.-Dr. Fernando Maximiliano Beltrán Castañeda\n3.-Dr. César Martín Delgado Torres\n4.-Dr. César Manuel Delgado Butrón\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 14:
        print("\t\t====Gastroenterología====")
        print("\n1.-Dra. Amparo Albina Medina Velarde\n2.-Dr. Luis Arce Cordero\n3.-Dr. Juan Manuel Carpio Patra\n4.-Dr. Jorge Isaac Del Carpio Lazo\n5.-Dr. Dennis Perea Alvarado\n6.-Dr. Delfín García Juarez\n7.-Dr. Cesar Augusto Esquia Medina\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 15:
        print("\t\t====Geriatría====")
        print("\n1.-Dra. Miriham Esperanza Camargo Pantoja\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 16:
        print("\t\t====Ginecología y Obstetricia====")
        print("\n1.-Dra. Rina Eleana Cuadros Salas\n2.-Dra. María Elena Esquivel Gonzáles\n3.-Dr. Miguel Montes Cáceres\n4.-Dr. Luis Alfredo Medina Gonzáles\n5.-Dr. Julio Damián Aguilar Flores\n6.-Dr. Julio César Belaúnde Portugal\n7.-Dr. German Benildo López Chávez\n8.-Dr. Francisco Alfredo Rivera Gallegos\n9.-Dr. Fernando Nicolás Jarufe Palao\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 17:
        print("\t\t====Hematología====")
        print("\n1.-Dr. Víctor Raúl Rivera Gallegos\n2.-Dr. Manuel Orlando Rivas Chávez\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 18:
        print("\t\t====Infectología====")
        print("\n1.-Dr. Mario Cornejo Giraldo\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 19:
        print("\t\t====Medicina Física y Rehabilitación====")
        print("\n1.-Dra. Ruth Yubana Vera Luna\n2.-Dr. Siles Reynel Rodriguez Rodríguez\n3.-Dr. Miguel Angel Espinoza Pinto\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 20:
        print("\t\t====Medicina General====")
        print("\n1.-Dr. César Arturo Gonzáles Pérez\n2.-Dr. Alberto Bivian Salinas Portugal\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()

def salir():
    b = 0
    while b == 0:
        os.system("cls")
        print("/////////////////////////////////////////////////////////////////////////")
        opp = input("\n====================ESTA SEGURO QUE DESEA SALIR ?=======================\n \n\t\t\t (Escriba Si/No ):\n\t\t\t\t ")
        print()
        if opp.lower() == "si":
            b=1
            print("===================EL PROGRAMA ESTA CERRANDOSE===========================\n")
            print("/////////////////////////////////////////////////////////////////////////")
            time.sleep(2)
            sys.exit(1)
        elif opp.lower() == "no":
            b=1
        else:
            b=0
    menu()

