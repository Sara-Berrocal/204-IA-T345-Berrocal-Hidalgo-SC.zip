import os 
os.system("cls")

donacion = float(input("Ingrese el monto de la donacion: $"))
salud, comedor = (donacion * 0.30, donacion * 0.50) if donacion >= 10000 else (donacion * 0.25, donacion * 0.60)
bolsa = donacion - (salud + comedor)

print(f"Centro de salud: $ {salud}")
print(f"Comedor de niños: $ {comedor}")
print(f"Inversion de la bolsa: $ {bolsa}")
