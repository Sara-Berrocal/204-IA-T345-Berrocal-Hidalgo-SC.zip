import os 
os.system("cls")
propinmen = 20
propinadi = 5

examapro = int(input("Ingrese el número de exámenes aprobados (de 0 a 3): "))
propinaditot = propinadi * examapro
propitot     = propinmen + propinaditot

print(f"La propina total es: S/. {propitot}")
 