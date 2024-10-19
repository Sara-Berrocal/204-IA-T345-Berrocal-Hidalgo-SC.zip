import os
os.system("cls")

cuota   = float(input("Ingrese el monto de la cuota: $"))
diapago = int(input("Ingrese el dia del pago (1-31): "))

if 1 <= diapago <= 10:
    tpagar = cuota - max(5, cuota * 0.02)
elif 11 <= diapago <= 20:
    tpagar = cuota
elif 21 <= diapago <= 31:
    tpagar = cuota + max(10, cuota * 0.03)
else:
    print("Dia invalido.")
print(f"Cuota mensual: $ {cuota:.2f}\nTotal a pagar: $ {tpagar:.2f}")

