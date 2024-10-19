import os
os.system("cls")

unidades = int(input("Ingrese la cantidad de unidades compradas: "))
precio = 20

compra = unidades * precio

if compra <= 500: descuento = 0.12 * compra
elif compra <= 700: descuento =  0.14 * compra
else: descuento = 0.16 * compra

if unidades <= 50 : caramelos = 5
elif unidades <= 100 : caramelos = 10 
else: caramelos = 15

print(f"Compra: S/. {compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {(compra-descuento):.2f}")
print(f"Caramelos:{caramelos:.2f}")

 