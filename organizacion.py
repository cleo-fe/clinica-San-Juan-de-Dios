import os
import sys
import time
import sqlite3
def menu():
    os.system("cls")
    os.system("color e")
    op = "0"
    opcion= ["INICIO","SERVICIOS","REGISTRO","STAFF MEDICO","SALIR"]
    while(op == "0"):
        print("////////////////////////////////////////////////////////////////////////")
        print("\n========================CLINICA SAN JUAN DE DIOS========================\n")
        print("/////////////////////////////////////////////////////////////////////////")
        print(" \n 1.- {}\n\n 2.- {}\n\n 3.- {}\n\n 4.- {}\n\n 5.- {}".format(opcion[0],opcion[1],opcion[2],opcion[3],opcion[4]))
        op = str(input("\n  INGRESE UNA OPCION:     "))
        if op not in ["1","2","3","4","5","6","7"]:
            print("============OPCION INCORRECTA VUELVA  INTENTARLO===========")
            time.sleep(2)
            op = "0"
        os.system("cls")
    if (op == "1"):
        inicio()
    elif (op == "2"):
        servicios_menu()
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
    list = ["NUEVO SERVICIO A AGREGAR","MOSTRAR SERVICIOS","MODIFICAR SERVICIOS","ELIMINAR SERVICIO","ATRAS"]
    while(op not in [1,2,3,4,5]):
        print("/////////////////////////////////////////////////////////////////////////")
        print("==============SERVICIOS DE LA CLINICA SAN JUAN DE DIOS=================")
        print("/////////////////////////////////////////////////////////////////////////")
        print("\n 1.- {}\n\n 2.- {}\n\n 3.- {}\n\n 4.- {}\n\n 5.- {}\n\n".format(list[0],list[1],list[2],list[3],list[4]))
        op = input("\n\tINGRESE UNA OPCCION:   ")
        try:
            op = int(op)
            if op not in [1,2,3,4,5]:
                print("\n==========OPCCION INCORECTA VUELVA A INTENTARLO==========")
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
        servicionuevo=input("\n\tINGRESE NUEVO SERVICIO:     \n")
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
        codigo=input("\n\tSELECCIONE NUMERO A MODIFICAR:    ")
        print("\n\t-----INGRESE LOS DATOS A MODIFICAR-----\n")
        servicionuevo=input("\tINGRESE NUEVO SERVICIO:      ")
        cursor.execute("update Registro set Servicios ='"+servicionuevo+"' where ID = '"+codigo+"'")
        con.commit()
        print("\n//////////////////////////////////////////////////////////////////////////")
        print("==================SERVICIO MODIFICADO EXITOSAMENTE=======================")
        print("//////////////////////////////////////////////////////////////////////////\n")
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
#===================================REGISTRO======================================================================#
def registro_menu():
    os.system("cls")
    op = 0
    r = Registro()
    list = ["INSCRIPCCION","MOSTRAR REGISTRO","BUSCAR INSCRIPCCION POR N° D.N.I.","MODIFICAR INSCRIPCION","ELIMINAR INSCRIPCION","ATRAS"]
    while(op not in [1,2,3,4,5,6]):
        print("////////////////////////////////////////////////////////////////////////////////")
        print("=====================REGISTRO DE LA CLINICA SAN JUAN DE DIOS====================")
        print("////////////////////////////////////////////////////////////////////////////////\n")
        print("\n 1.- {}\n\n 2.- {}\n\n 3.- {}\n\n 4.- {}\n\n 5.- {}\n\n 6.- {}\n".format(list[0],list[1],list[2],list[3],list[4],list[5]))
        op = input("\n\tINGRESE OPCION:    ")
        try:
            op = int(op)
            if op not in [1,2,3,4,5,6]:
                print("\n==========OPCCION INCORRECTA VUELVA A INTENTARLO==========")
                time.sleep(2)
                os.system("cls")
        except ValueError:
            print("\n----------INGRESE SOLO DIGITOS----------")
            time.sleep(3)
            os.system("cls")
            op = 0
    if(op == 1):
        r.inscripcion()
    elif(op == 2):
        r.mostrar()
    elif(op == 3):
        r.mostrarpordni()
    elif(op == 4):
        r.mostrar_Reg()
    elif(op == 5):
        r.eliminar()
    elif(op == 6):
        menu()
class Registro:
    def __init__(self):
        self.Servicio = ""
        self.Nombre = ""
        self.Apellido = ""
        self.Dni = ""
        self.Edad = ""

    def inscripcion(self):
        os.system("cls")
        print("///////////////////////////////////////////////////////////////////////////////")
        print("==================================INSCRIPCION==================================")
        print("///////////////////////////////////////////////////////////////////////////////\n")
        print("\n\tINGRESE LOS SIGUIENTES DATOS ")
        apellidopaterno = str(input( "\n APELLIDO PATERNO:   " ))
        apellidomaterno = str(input( "\n AELLIDO MATERNO:   " ))
        nombre = str(input("\n NOMBRE:   "))
        dni = str(input("\n D.N.I:   "))
        edad =str(input("\n EDAD:   "))


        servicio = servicios()
        con = sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("insert into Registros (ApellidoPaterno,ApellidoMaterno,Nombre,Dni,Edad,Servicio) VALUES ('"+apellidopaterno+"','"+apellidomaterno+"','"+nombre+"','"+dni+"','"+edad+"','"+servicio+"')")
        con.commit()
        print("\n///////////////////////////////////////////////////////////////////////////////")
        print("/////////////////////////USTED SE REGISTRO CON EXITO///////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////")
        input("\n-----------------------Presione enter para regresar al menu--------------------")
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
        for i in cursor:
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("\tNUMERO DE REGISTRO:      ",i[0])
            print("\tAPELLIDO PATERNO:        ",i[1])
            print("\tAPELLIDO MATERNO:        ",i[2])
            print("\tNOMBRE:                  ",i[3])
            print("\tDNI:                     ",i[4])
            print("\tEDAD:                    ",i[5])
            print("\tSERVICIO:                ",i[6])
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
        for i in cursor:
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("\tNUMERO DE REGISTRO:      ",i[0])
            print("\tAPELLIDO PATERNO:        ",i[1])
            print("\tAPELLIDO MATERNO:        ",i[2])
            print("\tNOMBRE:                  ",i[3])
            print("\tDNI:                     ",i[4])
            print("\tEDAD:                    ",i[5])
            print("\tSERVICIO:                ",i[6])
        print("\n////////////////////////////////////////////////////////////////////////////////")
        codigo=input("\n\t\tINDIQUE EL REGISTRO QUE DESEA MODIFICAR:     ")
        print("\nINGRESE LOS DATOS A MODIFICAR")
        op = "0"
        opcion= ["TODOS LOS CAMPOS","AELLIDO PATERNO","APELLIDO MATERNO","NOMBRE","DNI","EDAD","SERVICIO","SALIR"]
        while(op == "0"):
            print("\n  1.- {}\n\n  2.- {}\n\n  3.- {} \n\n  4.- {}\n\n  5.- {}\n\n  6.- {}\n\n  7.- {}\n\n  8.- {}".format(opcion[0],opcion[1],opcion[2],opcion[3],opcion[4],opcion[5],opcion[6],opcion[7]))
            op = str(input("\n\tINGRESE UNA OPCION:     "))
            if op not in ["1","2","3","4","5","6","7","8"]:
                print("\t\n==========OPCION INCORRECTA VUELVA A INTENTARLO==========!")
                time.sleep(2)
                op = "0"

        if (op == "1"):
            print("\n-------INGRESE DATOS A CONTINUACION------ ")
            apellidopaterno = input( "\n APELLIDO PATERNO:   " )
            apellidomaterno = input( "\n APELLIDO MATERNO:   " )
            nombre = input("\n NOMBRE:   ")
            dni = input("\n NUMERO DE D.N.I:   ")
            edad = input("\n EDAD:   ")
            servicio = servicios()
            cursor.execute("update Registros set ApellidoPaterno ='"+apellidopaterno+"',ApellidoMaterno ='"+apellidomaterno+"',Nombre ='"+nombre+"',Dni ='"+dni+"', Edad ='"+edad+"',Servicio ='"+servicio+"' where ID = '"+codigo+"'")
            con.commit()
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
            print("///////////////////////////////////////////////////////////////////////////////")
            input("\n---------------------Presione enter para regresar al menu----------------------")
            os.system("cls")
            con.close()
            registro_menu()
        elif (op == "2"):
            print("\n-------INGRESE DATOS A CONTINUACION------ ")
            apellidopaterno = input( "\n APELLIDO PATERNO:   " )
            cursor.execute("update Registros set ApellidoPaterno ='"+apellidopaterno+"' where ID = '"+codigo+"'")
            con.commit()
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
            print("///////////////////////////////////////////////////////////////////////////////")
            input("\n---------------------Presione enter para regresar al menu----------------------")
            os.system("cls")
            con.close()
            registro_menu()
        elif (op == "3"):
            print("\n-------INGRESE DATOS A CONTINUACION------ ")
            apellidomaterno = input( "\n APELLIDO MATERNO:   " )
            cursor.execute("update Registros set ApellidoMaterno ='"+apellidomaterno+"' where ID = '"+codigo+"'")
            con.commit()
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
            print("///////////////////////////////////////////////////////////////////////////////")
            input("\n---------------------Presione enter para regresar al menu----------------------")
            os.system("cls")
            con.close()
            registro_menu()
        elif (op == "4"):
            print("\n-------INGRESE DATOS A CONTINUACION------ ")
            nombre = input("\n NOMBRE:   ")
            cursor.execute("update Registros set Nombre ='"+nombre+"' where ID = '"+codigo+"'")
            con.commit()
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
            print("///////////////////////////////////////////////////////////////////////////////")
            input("\n---------------------Presione enter para regresar al menu----------------------")
            os.system("cls")
            con.close()
            registro_menu()
        elif (op == "5"):
            print("\n-------INGRESE DATOS A CONTINUACION------ ")
            dni = input("\n NUMERO DE D.N.I:   ")
            cursor.execute("update Registros set Dni ='"+dni+"' where ID = '"+codigo+"'")
            con.commit()
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
            print("///////////////////////////////////////////////////////////////////////////////")
            input("\n---------------------Presione enter para regresar al menu----------------------")
            os.system("cls")
            con.close()
            registro_menu()
        elif (op == "6"):
            print("\n-------INGRESE DATOS A CONTINUACION------ ")
            edad = input("\n EDAD:   ")
            cursor.execute("update Registros set Edad ='"+edad+"' where ID = '"+codigo+"'")
            con.commit()
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
            print("///////////////////////////////////////////////////////////////////////////////")
            input("\n---------------------Presione enter para regresar al menu----------------------")
            os.system("cls")
            con.close()
            registro_menu()
        elif (op == "7"):
            print("\n-------INGRESE DATOS A CONTINUACION------ ")
            servicio = servicios()
            cursor.execute("update Registros set Servicio ='"+servicio+"' where ID = '"+codigo+"'")
            con.commit()
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("=====================REGISTRO MODIFICADO EXITOSAMENTE==========================")
            print("///////////////////////////////////////////////////////////////////////////////")
            input("\n---------------------Presione enter para regresar al menu----------------------")
            os.system("cls")
            con.close()
            registro_menu()
        elif(op == "8"):
            registro_menu()

    def mostrarpordni(self):
        dni= input("\n\tINDIQUE SU NUMERO DE D.N.I.:    ")
        con=sqlite3.connect("pacientes.s3db")
        cursor = con.cursor()
        cursor.execute("SELECT * from Registros WHERE DNI = '"+dni+"'")
        for i in cursor:
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("\tNUMERO DE REGISTRO:      ",i[0])
            print("\tAPELLIDO PATERNO:        ",i[1])
            print("\tAPELLIDO MATERNO:        ",i[2])
            print("\tNOMBRE:                  ",i[3])
            print("\tDNI:                     ",i[4])
            print("\tEDAD:                    ",i[5])
            print("\tSERVICIO:                ",i[6])
        print("\n////////////////////////////////////////////////////////////////////////////////")
        input("\n--------------------Presione enter para regresar al menu-----------------------")
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
        for i in cursor:
            print("\n///////////////////////////////////////////////////////////////////////////////")
            print("\tNUMERO DE REGISTRO:      ",i[0])
            print("\tAPELLIDO PATERNO:        ",i[1])
            print("\tAPELLIDO MATERNO:        ",i[2])
            print("\tNOMBRE:                  ",i[3])
            print("\tDNI:                     ",i[4])
            print("\tEDAD:                    ",i[5])
            print("\tSERVICIO:                ",i[6])
        print("\n////////////////////////////////////////////////////////////////////////////////")
        codigo=input("\n\tINDIQUE QUE REGISTRO DESEA ELIMINAR :  ")
        cursor.execute("delete from Registros where ID = '"+codigo+"'")
        con.commit()
        print("\n\n///////////////////////////////////////////////////////////////////////////////")
        print("=====================REGISTRO ELIMINADO EXITOSAMENTE==========================")
        print("///////////////////////////////////////////////////////////////////////////////")
        input("\n---------------------Presione enter para regresar al menu----------------------")
        os.system("cls")
        con.close()
        registro_menu()

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
    elif opc == 21:
        print("\t\t====Medicina Intensiva====")
        print("\n1.-Dr. Rafael Fredy Tapia Pérez\n2.-Dr. Miguel Barreda de la Cruz\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 22:
        print("\t\t====Medicina Intensiva Pediatrica====")
        print("\n1.-Dr. Víctor Hugo Calderón Arenas\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 23:
        print("\t\t====Medicina Interna====")
        print("\n1.-Dra. Luz Mercedes Mujica Calderón\n2.-Dra. Luz * Mujica Calderón\n3.-Dra. Lourdes Jesús Quiroa Muñoz\n4.-Dr. Raúl Lazarte Cárdenas\n5.-Dr. Pedro Emilio Alcazar Zuzunaga\n6.-Dr. Luis Linares Morante\n7.-Dr. Luis Francisco Fajardo Karlo\n8.-Dr. Luis * Linares Morante\n9.-Dr. Javier Torres Angles\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 24:
        print("\t\t====Medico Cirujano====")
        print("\n1.-Dr. Jorge Perea Espinoza\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 25:
        print("\t\t====Nefrología====")
        print("\n1.-Dr. Raúl Hernán Hinojosa Obando\n2.-Dr. Jorge Erman Sánchez Sánchez\n3.-Dr. César Augusto Trillo Rodríguez\n4.-Dr. Adán Edgar Bahamondes Palacios\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 26:
        print("\t\t====Neumología====")
        print("\n1.-Dr. Miguel Fernando Farfán Delgado\n2.-Dr. Arturo Recabarren Lozada\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 27:
        print("\t\t====Neurocirugía====")
        print("\n1.-Dra. Marleny Isabel Llerena Velarde\n2.-Dr. Víctor Gamero Ramírez\n3.-Dr. Luis Enrique Mendoza Huerta\n4.-Dr. Jorge Uldarico Cabrera Zuñiga\n5.-Dr. Jorge Santiago Pino Cisneros\n6.-Dr. Hernan José Valdivia Sosa\n7.-Dr. Gonzalo Erasmo Ramírez Gamarra\n8.-Dr. Francisco Javier Salinas Málaga\n9.-Dr. Danny Fuentes Reynoso\n10.-Dr. Crisogono Francisco Rubio Barrios\n11.-Dr. Carlos Suarez Málaga\n12.-Dr. Benjamin Eudocio Castillo de la Flor Delgado\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 28:
        print("\t\t====Neurología====")
        print("\n1.-Dra. Yanet Astete Juarez\n2.-Dra. Jesús Yeliza Jovic Muñoz\n3.-Dra. Isabel Paola Camargo Salazar\n4.-Dra. Claudia Zea Villena\n5.-Dr. Julio Cesar Nisiama Vera\n6.-Dr. José Fernando Aguilar Flores\n7.-Dr. Hugo Yuen Oviedo	Neurología\n8.-Dr. Antero Peralta Mestas\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 29:
        print("\t\t====Nutricionista====")
        print("\n1.-Lic. Yanett Ccorahua Meza\n2.-Lic. Jesús Martinez Rodriguez\n3.-Lic. Gloria Salas Nuñez\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 30:
        print("\t\t====Obstretricia====")
        print("\n1.- Obs. Patricia Valdivia Carazas\n2.-Obs. Eliana Cáceres Cáceres\n3.-Obs. Eleana Romero Castillo\n4.-Obs. Boni Marianela Sánchez Cárdenas\n5.-Obs. Ana Cecilia Oviedo Carrazco\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 31:
        print("\t\t====Odontología====")
        print("\n1.-Dr. Jaime Velarde Flores\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 32:
        print("\t\t====Oftalmología====")
        print("\n1.-Dra. Milagros Torres Zavala\n2.-Dra. Lucia Fajardo Karlo\n3.-Dra. Giuliana Guillén Chavez\n4.-Dr. Víctor Sánchez Elguera\n5.-Dr. José Chavez Flores\n6.-Dr. Héctor Augusto Guillén Tamayo\n7.-Dr. Hugo Jimenez Herrera\n8.-Dr. Elard González Galeano\n9.-Dr. Antonio Herrera Pacheco\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 33:
        print("\t\t====Oncologia Medica====")
        print("\n1.-Dr. Renzo Alvarez Barreda\n2.-Dr. Hernán David Morón Escobar\n3.-Dr. Jorge Aldo Becerra Giraldez\n4.-Dr. Ernesto Andrés Vargas Quezada\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 34:
        print("\t\t====Ortopedia y Traumatología====")
        print("\n1.- Dr. Walter Juan Vargas Rodríguez\n2.-Dr. Víctor Clodoaldo Salas Corrales\n3.-Dr. Sergio Edwing Valdivia Rojas\n4.-Dr. Percy César Barrionuevo Silva\n5.-Dr. Percy Anibal Valdivia Lazo de la Vega\n6.-Dr. Percy Alberto Montesinos Valencia\n7.-Dr. Néctor Hugo Castelo García\n8.-Dr. Mauricio Rivera Bendezú\n9.-Dr. Manuel Jesús Luque Aguirre\n10.-Dr. Manuel Isaac Vera Salas\n11.-Dr. Luis Alberto Domingo Dongo Mardini\n12.-Dr. Lizardo Lozada Melgar\n13.-Dr. Julio César Vega Urrutia\n14.-Dr. Julio Aquino Apaza\n15.-Dr. Juan Manuel Pastor Sánchez\n16.-Dr. Juan Gualberto Cárdenas Moscoso\n17.-Dr. Juan Alberto Zeballos Medina\n18.-Dr. Jorge Cáceres Aucaylle\n19.-Dr. Hugo Jimmy Benavente Rojas\n20.-Dr. Edgardo Uldarico López Ortiz\n21.-Dr. Christiam Alfredo Gutierrez Corrales\n22.-Dr. Carlos Berckholtz Arispe\n23.-Dr. Carlos Alfonso Vargas Muñoz\n24.-Dr. Alfonso Guerra Pacheco\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 35:
        print("\t\t====Otorrinolaringología====")
        print("\n1.-Dra. Gina Elisa Chávez Torres\n2.-Dr. Roberto Orlando Núñez Quiroz\n3.-Dr. Octavio Daniel Zevallos Urday\n4.-Dr. Jorge Martínez Marcos\n5.-Dr. Hernan Callata Casani\n6.-Dr. Félix Hernan Jesús Paredes Vásquezn7.-Dr. Francisco Alejandro Martínez Benavides\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 36:
        print("\t\t====Pediatría====")
        print("\n1.-Dra. Olga Rocio Huaman Prado\n2.-Dra. Nuvia Leonor Valdivia Málaga\n3.-Dra. Nancy Elizabeth Zegarra Montoya\n4.-Dra. María Isabel Chavez Salinas\n5.-Dra. Martha Cecilia Chávez Vargas\n6.-Dra. Julia Delgado Palacios\n7.-Dra. Eliana María Peralta Martini\n8.-Dra. Ada Molina Portillo\n9.-Dr. Víctor Emigdio Chura Ortiz\n10.-Dr. Víctor Calderón Arenas\n11.-Dr. Pedro Raúl Zuñiga López\n12.-Dr. Pablo Polanco Aguilar\n13.-Dr. Nassip * Llerena Navarro\n14.-Dr. Miguel Pinto Villavicencio\n15.-Dr. Juan Nicolás Corrales Gallegos\n16.-Dr. Juan Andrés Begazo Bueno\n17.-Dr. José Luis Seijas Mogrovejo\n18.-Dr. Edwin Martín Lazo Rivera\n19.-Dr. Eddy Hernan Villafuerte Rivera\n20.-Dr. César Guillermo Alpaca Esquivel\n21.-Dr. Cesar Guillermo Alpaca Cano\n22.-Dr. Carlos Alberto Jara Gutierrez\n23.-Dr. Arturo Recabarren Lozada\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc ==37:
        print("\t\t====Psicología====")
        print("\n1.-Dra. Mileny Pamea Gastulo Vera\n2.-Dra. Elsa Flora Rodríguez Valero\n3.-Dra. Eleana María Cervantes Quezada\n4.-Dra. Diana Carolina Paz Romainville\n5.-Dra. Desire Zeballos Buscaglia\n6.-Dr. Octavio Salinas Gutiérrez\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 38:
        print("\t\t====Psiquiatría====")
        print("\n1.-Dra. Carla Elizabeth Málaga Pinto\n2.-Dr. Víctor Emilio Valdivia Murillo\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 39:
        print("\t\t====Radiología====")
        print("\n1.-Dra. Ivonne Elizabeth Rodríguez Fernández\n2.-Dra. Alejandra Mercado Ojeda de Calla\n3.-Dr. Víctor Ernesto Gamero Medina\n4.-Dr. Marco Antonio Medina Gonzáles\n5.-Dr. Gustavo Ramiro Medina Rivera\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 40:
        print("\t\t====Reumatología====")
        print("\n1.-Dra. Ruth Patricia Poblete Huertas\n2.-Dr. Simón Alfredo Gutiérrez Chávez\n3.-Dr. Luis Fernando Mateo Bellatín Vargas\n4.-Dr. Alejandro Miranda Pinto\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 41:
        print("\t\t====Urología====")
        print("\n1.-Dr. Roger Hugo Gutiérrez Córdova\n2.-Dr. Luciano Benjamin Torrico Herrera\n3.-Dr. Julio Suárez Cueva\n4.-Dr. Juan Herón Frisancho Espinoza\n5.-Dr. Jaime Hernani Cuba\n6.-Dr. Fernando Rolando Diaz Gallegos	\n7.-Dr. Alejandro Gabriel Quiroa Mesias\n8.-Dr. Alejandro Escalante Álvaro\n")
        input("\t--------Presione enter para regresar--------")
        staff_medico()
    elif opc == 42:
        menu()
def servicios():
    op = "0"
    ser = ["Hospitalizacion","Maternidad","Farmacia","Laboratorio","Ambulancia","Chequeos Preventivos","Consultorio Externo","Nutricion - cafeteria","Unidad de Cuidados Intensivos","Emergencias","Centro Quirúrgico","Oftalmología","Odontología","Rehabilitación","Video endoscopias","Tomografías","Gabinete Cardiólogo","Gabinete Neurológico ","Esterilización ","Aula Virtual Hospitalaria ","","","","","","","","","","","","","","","","","","",""]
    while(op == "0"):
        print("////////////////////////////////////////////////////////////////////////////////")
        print("===========================SERVICIOS A REGISTRARSE==============================")
        print("\n 1.- {}\n 2.- {}\n 3.- {}\n 4.- {}\n 5.- {}\n 6.- {}\n 7.- {}\n 8.- {}\n 9.- {}\n 10.- {}\n 11.- {}\n 12.- {}\n 13.- {}\n 14.- {}\n 15.- {}\n 16.- {}\n 17.- {}\n 18.- {}\n 19.- {}\n 20.- {}".format(ser[0],ser[1],ser[2],ser[3],ser[4],ser[5],ser[6],ser[7],ser[8],ser[9],ser[10],ser[11],ser[12],ser[13],ser[14],ser[15],ser[16],ser[17],ser[18],ser[19]))
        op = str(input("\n\tINGRESE OPCCION : "))
        if op not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
            print("\n--------OPCCION INCORRECTA VUELVA  INTENTARLO--------")
            time.sleep(2)
            op = "0"
    aux = int(op)-1
    cont = ser[aux]
    return cont

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

