import os
os.system("cls")
    
pies= float(input("Ingrese la cantidad de pies: "))
pulgadas= float(input("Ingrese la cantidad de pulgadas: "))

metros = (pies * 0.3048) + (pulgadas * 0.0254)

print(f"La estatura en metros es:{metros} m")


