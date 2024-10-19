import os
os.system("cls")
    
not1=float(input("Ingrese la primera nota: "))
not2=float(input("Ingrese la segunda nota: "))
not3=float(input("Ingrese la tercera nota: "))

if not3 >= 10:
   not3 += 2
   
promediof = (not1 +not2 + not3) / 3

print(f"El promedio final del alumno es: {promediof:.2f}")
