import os 
os.system("cls")

b = float(input("Ingrese la base del rectangulo:"))
h = float(input("Ingrese la altura del rectangulo:"))


a= b * h
p = 2 * (b + h)

print(f"Área :{a:.2f}")
print(f"Perimetro :{p:.2f}")

