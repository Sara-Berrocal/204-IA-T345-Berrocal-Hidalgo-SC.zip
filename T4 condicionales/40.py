import os
os.system("cls")

pesomateria = {
    "Matematica": {"PC1": 0.10, "PC2": 0.20, "PC3": 0.10, "EP": 0.30, "EF":0.30},
    "Fisica"    : {"PC1":0.20, "PC2": 0.20, "PC3": 0.20, "EP": 0.20, "EF": 0.20},
    "Quimica"   : {"PC1": 0.10,"PC2": 0.30, "PC3": 0.10, "EP": 0.25, "EF": 0.25} 
}

curso = input("Ingrese el curso: ") 
pc1   = float(input("Ingrese la nota de PC!: "))
pc2   = float(input("Ingrese la nota de PC2: "))
pc3   = float(input("Ingrese la nota de PC3: ")) 
ep    = float(input("Ingrese la nota examen parcial: "))
ef    = float(input("Ingrese la nota del examen final: "))

promedio = (pc1 * pesomateria[curso]["PC1"] + pc2 * pesomateria[curso]["PC2"] + pc3 * pesomateria[curso]["PC3"] + ep * pesomateria[curso]["EP"] + ef * pesomateria[curso]["EF"]) 

if promedio >= 13:
    estado = "Aprobado"
else:
    estado = "Desaprobado"

print(f"El promedio final es: {promedio:.2f}")
print(f"Estado: {estado}")
