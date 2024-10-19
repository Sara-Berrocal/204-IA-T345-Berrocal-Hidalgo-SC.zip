import os 
os.system("cls")
uniA = int(input("Unidades del Producto A: "))
uniB = int(input("Unidades del Producto B: "))

impobruto = uniA * 25 + uniB * 30
descuentot = (0.15 * (uniA * 25) if uniA > 50 else 0) + (0.10 * (uniB * 30) if uniB > 60 else 0)

Tpagar = impobruto - descuentot

print(f"Importe bruto: S/. {impobruto:.2f}")
print(f"Descuento: S/. {descuentot:.2f}")
print(f"Total a pagar : S/. {Tpagar:.2f}")
