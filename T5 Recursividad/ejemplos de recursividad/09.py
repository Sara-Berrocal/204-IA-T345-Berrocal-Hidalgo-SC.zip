#Comprobación de palidromo
import os 
os.system("cls")
def palidromo(cadena):
    cadena = cadena.replace(" ", "").lower()

    def verifipalindromo(cadena, inicio, fin):
        if inicio >= fin:
            return True
        
        if cadena[inicio] != cadena[fin]:
            return False
        return verifipalindromo(cadena, inicio + 1, fin - 1)

    return verifipalindromo(cadena, 0, len(cadena)- 1)
    
cadena = "radar"
resultado = palidromo(cadena)
print(f"La cadena {cadena} es palindromo: {resultado}")