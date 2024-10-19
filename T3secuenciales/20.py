import os
os.system("cls")

cantidad = float(input("Ingrese la cantidad de dinero en soles: "))

billete200 = int( cantidad //200)
cantidad %= 200

billete100 = int( cantidad //100)
cantidad %= 100

billete50 = int( cantidad //50)
cantidad %= 50

billete20 = int( cantidad //20)
cantidad %= 20

billete10 = int( cantidad //10)
cantidad %= 10

moneda5 = int(cantidad // 5)
cantidad %= 5


moneda2 = int(cantidad // 2)
cantidad %= 2

moneda1 = int(cantidad // 1)

print(f"Billetes de 200: {billete200}")
print(f"Billetes de 100: {billete100}")
print(f"Billetes de 50: {billete50}")
print(f"Billetes de 20: {billete20}")
print(f"Billetes de 10: {billete10}")
print(f"Moneda de 5: {moneda5}")
print(f"Moneda de 2: {moneda2}")
print(f"Moneda de 1: {moneda1}")