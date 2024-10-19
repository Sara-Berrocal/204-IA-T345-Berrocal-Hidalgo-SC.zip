import os 
os.system("cls")

donacion= float(input("Ingrese el monto de la donación anual: "))

print(f"Monto para el centro de salud: ${0.25 * donacion:.2f}")
print(f"Monto para el comedor infantil: ${0.35 * donacion:.2f}")
print(f"Monto para la escuela infantil: ${0.25 * donacion:.2f}")
print(f"Monto para el asilo de ancianos: ${0.15 * donacion:.2f}")

