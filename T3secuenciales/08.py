import os, math
os.system("cls")

r = float(input("Ingrese el radio del cilindro:"))
h = float(input("Ingrese la altura del cilindro:"))
 
abase = math.pi * r**2
alateral = 2 * math.pi * r * h
atotal = 2 * abase + alateral

print(f"Área base:{abase :.2f}")
print(f"Área lateral:{alateral :.2f}")
print(f"Área total: {atotal :.2f}")
