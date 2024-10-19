import os
os.system("cls")

hora24 = input ("Ingrese la hora (HH:MM): ")

horas = int(hora24[0:2])
minutos = int(hora24[3:5])

if horas >= 0 and horas <= 23 and minutos >= 0 and minutos <= 59:
    if horas == 0:
        print("Es 12:", minutos, "AM")
    elif horas < 12:
        print("Es", horas, ":", minutos, "AM")
    elif horas == 12:
        print("Es 12:", minutos, "PM")
    else:
        print("Es", horas - 12, ":", minutos, "PM")

else:
    print("Hora invalida")

