import os 
os.system("cls")

categoria = input("Ingrese la categoria del trabajador (A, B, C, D): ").upper()
hrtrabajadas = float(input("Ingrese el numero de horas trabajadas: "))

sueldobruto = 0 
descuento   = 0

if categoria == 'A':
    tarifa = 21.00

elif categoria == 'B':
    tarifa = 19.50

elif categoria == 'C':
    tarifa = 17.00

elif categoria == 'D':
    tarifa = 15.50
else:
    tarifa = 0

if tarifa > 0:

    sueldobruto = tarifa * hrtrabajadas

    if sueldobruto > 2500:
        descuento = sueldobruto * 0.20
    else:
        descuento = sueldobruto * 0.15

    sueldoneto = sueldobruto - descuento

    print(f"Sueldo Bruto: S/. {sueldobruto:.2f}")
    print(f"Descuento: S/. {descuento:.2f}")
    print(f"Sueldo Neto: S/. {sueldoneto:.2f}")
else:
    print("Categoria no válida")
    
    