import os 
os.system("cls")

num1 = float(input("Ingrese el primer numero (num1): "))
num2 = float(input("Ingrese el segundo numro (num2): "))
num3 = float(input("Ingrese el tercer numero (num3): "))

if num1 < num2 < num3:
    orden = "ascendente"
elif num1 > num2 > num3:
    orden = "descendente"
else:
    orden = "desorden" 
print(f"Los nùmeros fueron ingresados en orden {orden}. ")

 