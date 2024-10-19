#Contar cuántas veces aparece un dígito en un número
import os 
os.system("cls")

def cont_digito(n, digit):
    if n == 0:
        return 0
    return(1 if n % 10 == digit else 0) + cont_digito(n // 10, digit)

print(cont_digito (1222334, 3))
