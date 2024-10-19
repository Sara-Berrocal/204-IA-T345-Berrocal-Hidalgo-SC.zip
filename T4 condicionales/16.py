import os
os.system("cls")

ingremensual = float(input("Ingreso mensual es: "))
costcasa = float(input("Ingrese el costo de la casa: "))

if ingremensual < 1250:
    cuotinicial = costcasa * 0.15
    cuotmensual = (0.85 * costcasa) / 120
else:
    cuotinicial = costcasa * 0.30
    cuotmensual = (0.70 * costcasa) / 75

# cuotinicial = (0.15 if ingremensual < 1250 else 0.30) * costcasa

# cuotmensual = (0.85 if ingremensual < 1250 else 0.70) * costcasa / (120 if ingremensual < 1250 else 75)

print(f"Cuota inicial = {cuotinicial:.2f}")
print(f"Cuota mensual = {cuotmensual:.2f}")                