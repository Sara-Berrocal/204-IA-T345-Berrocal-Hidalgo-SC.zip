#Suma de números pares hasta m
import os
os.system("cls")

def suma_pares(m):
    if m < 2:
        return 0
    return(m if m % 2 == 0 else m - 1) + suma_pares(m - 2)
print(suma_pares(16)) # 72 (2+4+6+8+10+12+14+16)
