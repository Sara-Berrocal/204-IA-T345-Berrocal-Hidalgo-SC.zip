import os
os.system("cls")

montotal = float(input("Ingrese el monto total de la compra: S/. "))

porcenprestamo = 0.30 if montotal > 5000 else 0.20
monprestamo    = montotal * porcenprestamo
interes        = monprestamo * 0.10
tpagarbanco    = monprestamo + interes
dineroprop     = montotal - monprestamo

print(f"Monto a pagar con dinero propio de la empresa: S/. {dineroprop:.2f}")
print(f"Montoa pagar al banco con interes : S/. {tpagarbanco:.2f}")

