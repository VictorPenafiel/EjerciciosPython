from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def calcularEdad(fechaNacimiento):
    listAux= fechaNacimiento.split("/")#["dd","mm","yyyy"]
    listTemp=[]
    listTemp.append([date.today().day,date.today().month,date.today().year])
    if(int(listAux[1]) < listTemp[0][1]): #ya cumplio años
        return listTemp[0][2] - int(listAux[2])
    
    elif(int(listAux[1]) == listTemp[0][1]): #Mismo mes
        if(int(listAux[0]) <= listTemp[0][0]): #ya paso el dia de cumpleños
            return listTemp[0][2] - int(listAux[2])
    
    elif(int(listAux[0]) > listTemp[0][0]): #Mismo mes, pero aún no llega el dia de cumpleaños
        return listTemp[0][2] - int(listAux[2])-1
    
    elif(int(listAux[1]) > listTemp[0][1]): # El mes actual es menor al mes del cumple (aún no cumple años)
        return listTemp[0][2] - int(listAux[2])-1
    

ingresar_fecha= input("ingrese la fecha de nacimiento en el sgte formato dd/mm/aa: ")
print(calcularEdad(ingresar_fecha))