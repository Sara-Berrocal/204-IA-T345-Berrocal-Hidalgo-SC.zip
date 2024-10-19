import os
os.system("cls")

precdocena = float(input("Precio por docena: S/. "))
cantdocenas = int(input("Cantidad de docenas: "))

montcompra =  precdocena * cantdocenas
descuento  =  montcompra * (0.15 if cantdocenas >= 6 else 0.10)
tpagar     =  montcompra - descuento
obselapice = (cantdocenas // 3) * 2 if cantdocenas >= 30 else 0

print(f"Monto de la compra: S/. {montcompra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {tpagar:.2f}")
print(f"Obsequio lapiceros: S/. {obselapice:.2f}")
    
