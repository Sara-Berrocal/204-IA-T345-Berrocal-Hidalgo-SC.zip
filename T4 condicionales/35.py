import os
os.system("cls")

codigo = int(input("Ingrese el codigo el empleado (3cifras): "))

if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0:
    tipo = "Administrativo"
elif codigo % 3 == 0 and codigo % 5 == 0:
    tipo = "Directivo"
elif codigo % 2 == 0:
    tipo = "Vendedor"
else: 
    tipo = "Seguridad"
    
print(f"El tipo de empleado es: {tipo}")
