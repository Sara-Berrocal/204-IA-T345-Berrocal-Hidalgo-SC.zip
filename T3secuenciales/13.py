import os, math
os.system("cls")

a = float(input("Ingrese el valor del primer cateto: "))
b = float(input("Ingrese el valor del segundo cateto: "))

hipotenusa = math.sqrt(a**2 + b**2)

print(f"La hipotenusa del triangulo es: {hipotenusa:.2f}")
