import os 
os.system("cls")

mes = int(input("Ingrese el nùmero del mes: "))
año = int(input("Ingrese el año: "))

bisiesto = 0
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            bisiesto = 1
    else:
        bisiesto = 1

nombmes =""
dias = 0

if mes == 1:
    nombmes = "Enero"
    dias = 31
if mes == 2:
    nombmes = "Febrero"
    if bisiesto == 1:
        dias = 29
    else:
        dias = 28
if mes == 3:
    nombmes = "Marzo"
    dias = 31
if mes == 4:
    nombmes = "Abril"
    dias = 30
if mes == 5:
    nombmes = "Mayo"
    dias = 31
if mes == 6:
    nombmes = "Junio"
    dias = 30
if mes == 7:
    nombmes = "Julio"
    dias = 31
if mes == 8:
    nombmes = "Agosto"
    dias = 31
if mes == 9:
    nombmes = "Septiembre"
    dias = 30
if mes == 10:
    nombmes = "Octubre"
    dias = 31
if mes == 11:
    nombmes = "Noviembre"
    dias = 30
if mes == 12:
    nombmes = "Diciembre"
    dias = 31

print("El mes de", nombmes, "del año", año, "tiene", dias, "dias.")

