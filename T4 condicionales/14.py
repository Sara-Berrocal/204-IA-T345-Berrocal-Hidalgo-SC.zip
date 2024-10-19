import os
os.system("cls")

numetarjeta = int(input("Ingrese el numero de la tarjeta: "))
montcompra  = float(input("Ingrese el monto de la compra: "))
descuento   = 0.05
if (numetarjeta // 2) * 2 == numetarjeta:
          
    if numetarjeta >= 100:
        descuento = 0.15
     

montdescuento = montcompra * descuento

print("Nùmero de Tarjeta:", numetarjeta)
print("Monto de Compra:", montcompra)
print("Monto de descuento:", montdescuento)

