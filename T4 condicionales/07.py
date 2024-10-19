import os 
os.system("cls")

n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
n3 = int(input("Ingrese el tercer número entero "))

if n1 <= n2 <= n3:
    intermedio = n2
elif n1 <= n3 <= n2:
    intermedio = n3
elif n2 <= n1 <= n3:
    intermedio = n1
elif n2 <= n3 <= n1:
    intermedio = n3
elif n3 <= n1 <= n2:
    intermedio = n1
else:
    intermedio = n2


print(f"El número intermedio es: {intermedio}")

 