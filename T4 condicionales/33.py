import math

def calculos_matematicos():
    num = 25
    raiz = math.sqrt(num)
    print(f"La raiz cuadrada de {num} es {raiz}")

    print(f"El valor de pi es aproximadamente {math.pi}")

    angulo_grados = 45
    angulo_radianes = math.radians(angulo_grados)
    seno = math.sin(angulo_radianes)
    print(f"El seno de {angulo_grados} grados es {seno}")

    logaritmo = math.log(100)
    print(f"El logaritmo natural de 100 es {logaritmo}")

    num_factorial = 5
    factorial = math.factorial(num_factorial)
    print(f"El factorial de {num_factorial} es {factorial}")


def main():
    calculos_matematicos()


if __name__ == "__main__":
    main()
