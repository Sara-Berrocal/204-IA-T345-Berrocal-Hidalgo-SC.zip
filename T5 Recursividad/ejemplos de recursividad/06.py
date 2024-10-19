#Calcular el valor absoluto de un número
import os 
os.system("cls")

def valor_absoluto(n):
    if n < 0:
        return -n
    return n
print(valor_absoluto(-6))
print(valor_absoluto(6))
