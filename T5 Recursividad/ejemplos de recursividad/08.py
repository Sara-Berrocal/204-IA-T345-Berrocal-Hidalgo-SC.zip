#Descomposición en factores primos 
import os 
os.system("cls")

def factores_primos(n, divisor=2):
    
    if n == 1:
        return[]
    if n % divisor == 0:
        return [divisor] + factores_primos(n // divisor, divisor)
    else:
        return factores_primos(n, divisor + 1)
numero = 56
resultado = factores_primos(numero)
print(f"Los factores primos de {numero} son: {resultado}")
