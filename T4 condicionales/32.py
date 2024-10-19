import os 
os.system("cls")

categoria = input("Ingrese la categoria (A, B, C, D): ")
hr_trabajadas = float(input("Ingrese las horas trabajadas: "))

if categoria == "A":
    pago_hr = 21.00
elif categoria == "B":
    pago_hr = 19.50
elif categoria == "C":
    pago_hr = 17.00
elif categoria == "D":
    pago_hr = 15.50
else:
    print("Categoria no valida.")

suelbruto = hr_trabajadas * pago_hr

if suelbruto > 2500:
    descuento = suelbruto * 0.20
else:
    descuento = suelbruto * 0.15

suelneto = suelbruto - descuento

print("Sueldo bruto: S/.", suelbruto)
print("Descuento: S/.", descuento)
print("Sueldo neto: S/.", suelneto)





