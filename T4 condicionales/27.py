import os
os.system("cls")

montvendido = float(input("Ingrese el monto total vendido: S/. "))
suelbruto   = 600 + (montvendido * 0.15)
descuento   = suelbruto * (0.10 if suelbruto > 1000 else 0.05)
suelneto    = suelbruto - descuento
polos       = 3 if montvendido > 1000 else 1

print(f"Sueldo bruto: S/. {suelbruto:.2f}\nDescuento: S/. {descuento:.2f}\nSueldo neto: {suelneto:.2f}\nNumero de polos: {polos}")
    