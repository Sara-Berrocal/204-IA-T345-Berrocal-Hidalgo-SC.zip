import os 
os.system("cls")

unidades = int(input("Ingrese la canitdad de unidades adquiridas: "))

if unidades <= 25:
    preciounit = 27
elif unidades <= 50:
    preciounit =25
else:
    preciounit = 23

impocompr = unidades * preciounit

if unidades > 50:
    descuento = impocompr * 0.15
else:
    descuento = impocompr *0.05
tpagar = impocompr - descuento

print(f"Importe de la compra: S/. {impocompr:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {tpagar:.2f}")
