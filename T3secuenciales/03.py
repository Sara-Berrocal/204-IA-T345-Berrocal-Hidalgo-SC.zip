import os 
os.system("cls")

km = float(input("kilometros: "))
pies = float(input("pies: "))
millas = float(input("millas: "))


metros = km * 1000 + (pies / 3.2808) + (millas * 1609)
yardas = metros * 1.0936

print(f"total recorrido: {metros:.2f} metros o {yardas:.2f} yardas.")
