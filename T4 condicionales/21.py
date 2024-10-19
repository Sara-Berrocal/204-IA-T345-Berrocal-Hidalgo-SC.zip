import os 
os.system("cls")
numero = int(input("Ingrese el nùmero asignado (cuatro cifras): "))

if 1000 <= numero <10000:
    estcivil = {1: "Soltero", 2: "Casado", 3: "Divorciado", 4: "Viudo"}.get(numero // 1000, "Estado civil no vàlido")
    edad     = (numero // 10) % 100
    sexo     = {1:"Masculino", 2: "Femenino"}.get(numero % 10, "Sexo no vàlido")

    print(f"Estado civil: {estcivil}")
else:
    print("El numero ingresado debe tener cuatro cifras.")
