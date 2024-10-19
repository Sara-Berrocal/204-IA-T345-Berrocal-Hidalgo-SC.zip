import os 
os.system("cls")

sexo = input("Ingrese el sexo (M/F): ")
edad = int(input("Ingrese la edad: "))


if sexo == "F":
    categoria = "FA" if edad < 23 else "FB"
elif sexo == "M":
    categoria = "MA" if edad < 25 else "MB"
else:
    categoria = "Sexo no vàlido"

print(f"Categoria: {categoria}")

    