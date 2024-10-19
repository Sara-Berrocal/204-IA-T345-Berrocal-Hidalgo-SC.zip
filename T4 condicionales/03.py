import os 
os.system("cls")

angulo = float(input("Ingrese el valor del ángulo en grados:"))

if angulo == 0:
    clasif = "Nulo"
elif 0 < angulo < 90:
    clasif = "Agudo"
elif angulo == 90:
    clasif = "Recto"
elif 90 < angulo < 180:
    clasif = "Obtuso"
elif angulo == 180:
    clasif = "llano"
elif 180 < angulo < 360:
    clasif = "Cóncavo"
elif angulo == 360:
    clasif = "Completo"
else:
    clasif = "No válido"

print(f"El ángulo de {angulo}° es {clasif}")


 