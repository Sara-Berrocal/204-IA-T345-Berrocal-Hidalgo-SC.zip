import os
os.system("cls")

n = int(input("Ingresa un número de tres cifras: "))

if 100 <= n <= 999:
    a, b, c = map(int, str(n))
    if a + 1 == b == c-1:
        print("Consecutivo ascendente.")
    elif a - 1 == b == c + 1:
        print("Consecutivo descendente.")
    else:
        print("No son números consecutivos.")
else:
    print("No es un número de tres cifras.")