import os
os.system("cls")

cuadernos = int(input("Ingrese el numero de cuadernos: "))
lucas = pilot = faber = 0

if cuadernos >= 36:
    pilot = (cuadernos // 4)*2
    faber = (cuadernos // 6)
    lucas = (cuadernos // 12)

elif cuadernos >= 24:
    faber = (cuadernos // 4)*2
elif cuadernos >= 12:
    lucas = (cuadernos //4)

print(f"Lapiceros:\nLucas: {lucas}\nFaber: {faber}\Pilot: {pilot}")
