#Generar los cuadrados de los números desde 1 hasta m
import os
os.system("cls")

def squares(m):
    if m == 0:
        return[]
    return squares(m - 1) + [m * m]
print(squares(6))   #salida [1, 4, 9, 16, 25. 36]