#Calcular el tamaño de un número
import os 
os.system("cls")

def contar_digitos(n):
    if n == 0:
        return 0
    return 1 + contar_digitos(n // 10)
print(contar_digitos(123456))
