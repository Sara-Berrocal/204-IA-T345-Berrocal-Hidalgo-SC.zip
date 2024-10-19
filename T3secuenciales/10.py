import os
os.system("cls")

num = int(input("Ingrese un número natural de 4 cifras: "))
numeroreves = (num % 10) * 1000 + ((num // 10) % 10) * 100 + ((num // 100) % 10) * 10 + (num // 1000)

print(f"El numero al reves es: {numeroreves}")


