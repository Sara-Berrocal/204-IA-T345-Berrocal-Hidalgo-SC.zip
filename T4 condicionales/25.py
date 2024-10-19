import os
os.system("cls")

suelbruto = float(input("Ingrese el sueldo bruto: S/. "))
hijos     = int(input("Ingrese la cantidad de hijos: "))

bonif = (suelbruto * 0.125 + hijos * 40) if hijos > 1 else suelbruto * 0.10
suelneto = suelbruto + bonif

print(f"Bonificacion: S/. {bonif:.2f} ")
print(f"Sueldo neto: S/. {suelneto:.2f}") 


