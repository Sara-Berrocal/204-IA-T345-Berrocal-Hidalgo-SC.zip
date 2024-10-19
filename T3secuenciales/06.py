import os, math
os.system("cls")

r = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cllindro: "))


at= 2 * math.pi * r * (r+h)
volumen = math.pi * r**2 *h

print(f"Área total:{at:.2f}")
print(f"Volumen:  {volumen:.2f}")

