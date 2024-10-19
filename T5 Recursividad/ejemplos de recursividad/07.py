# Conteo de ceros en un número
import os 
os.system("cls")
def contar_ceros(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    return( n % 10 == 0) + contar_ceros( n // 10)

print( contar_ceros(2005001040000)) 