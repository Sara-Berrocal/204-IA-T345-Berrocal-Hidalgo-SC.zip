import os 
os.system("cls")

producodigo = {101:17, 102:25, 103:30, 104:27}
codigo_producto = int(input("Ingrese el codigo del precio unitario (101, 102, 103, 104): "))
unidades = int(input("Ingrese la cantidad de unidades: "))

preciounitario = producodigo[codigo_producto]
impocompra = preciounitario * unidades

if 1 <= unidades <= 10:
    desporcentaje = 0.05
elif 11 <= unidades <= 20:
    desporcentaje= 0.08
elif 21 <= unidades <= 30:
    desporcentaje = 0.10
else:
    desporcentaje = 0.13

descuento = impocompra * desporcentaje
tpagar    = impocompra - descuento

print(f"Importe de la compra: {impocompra:.2f}")
print(f"Descuento: {descuento:.2f}")
print(f"Total a pagar: {tpagar:.2f}")