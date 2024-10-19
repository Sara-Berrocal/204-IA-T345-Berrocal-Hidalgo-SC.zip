import os, math
os.system("cls")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
d = int(input("Ingrese el cuarto numero: "))
e = int(input("Ingrese el quinto numero: "))

numemay1 = max(a, b, c, d, e)
numemay2 = max( min(a, b), min(c, d), min (e, numemay1))
numemay3 = min(max(a, b), max(c, d), max(e, numemay2))

promedio = (numemay1 + numemay2 + numemay3) / 3
print(f"El promedio de los 3 numeros mayores es: {promedio}")