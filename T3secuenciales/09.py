import os 
os.system("cls")

num = int(input("Ingrese un número entero positivo de 4 cifras: "))

c1 = num // 1000
c2 = (num % 1000) // 100
c3 = ((num % 1000) % 100) // 10
c4 = num % 10

print(f"Suma = {( c1+c2+c3+c4)}")

