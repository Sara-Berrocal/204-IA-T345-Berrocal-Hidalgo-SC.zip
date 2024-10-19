import os
os.system("cls")

suelbasic = 500
comiporce = 0.09
descuporce = 0.11
    
montovend = float(input("Ingrese el monto total vendido: "))
comision  = montovend * comiporce
suelbrut   = suelbasic + comision
descuento = suelbrut * descuporce

suelnet = suelbrut - descuento

print(f"Comisión: S/. {comision:.2f}")
print(f"Sueldo bruto: S/. {suelbrut:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {suelnet:.2f}")

