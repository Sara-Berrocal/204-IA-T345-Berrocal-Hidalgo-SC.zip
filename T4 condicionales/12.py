import os 
os.system("cls")

dia = int(input("Ingrese un número (1-7) que corresponda a un dia de la semana: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia ==3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Número no válido. Ingresa un número entre 1 y 7.")
