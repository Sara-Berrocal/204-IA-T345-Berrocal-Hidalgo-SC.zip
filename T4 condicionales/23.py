import os
os.system("cls")

notmate =float(input("Nota de Matematica: "))
notfisica = float(input("Nota de fìsica: "))

propmate   = 3 if notmate > 17 else notmate
propfisica = 2 if notfisica > 15 else 0.5
tpropina   = propmate + propfisica

promedio = (notmate + notfisica) / 2
reloj    = "Si" if promedio > 16 else "No"

print(f"Total de propina: S/. {tpropina:.2f}")
print(f"Obsequio reloj: {reloj}")

    