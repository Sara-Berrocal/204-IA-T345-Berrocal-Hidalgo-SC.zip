import os 
os.system("cls")

tarifhorar = float(input("Ingrese la tarifa horaria en dólares: "))
horatrabaj = float(input("Ingrese el número total de horas trabajadas: "))

sueldbasi = tarifhorar * horatrabaj
bonificacion = sueldbasi * 0.20
sueldbrut = sueldbasi + bonificacion
desc = sueldbrut * 0.10
sueldnet = sueldbrut - desc

print(f"Sueldo básico: ${sueldbasi:.2f}")
print(f"Sueldo bruto: ${sueldbrut:.2f}" )
print(f"Sueldo neto: ${sueldnet:.2f}" )
