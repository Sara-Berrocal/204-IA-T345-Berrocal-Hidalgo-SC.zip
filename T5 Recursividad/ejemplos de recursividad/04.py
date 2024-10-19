#Imprimir números desde el 1 hasta m en orden ascendente
import os 
os.system("cls")

def nume_ascendente(m):
    if m == 0:
        return
    print(m)
    nume_ascendente(m -1)
nume_ascendente(5)