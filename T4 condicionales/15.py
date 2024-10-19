import os 
os.system("cls")

suelbasico = 250
montvendido = float(input("Ingrese el monto total vendido: "))

if montvendido < 5000:
    comision = 0.05
elif montvendido < 10000:
    comision = 0.08
elif montvendido > 20000:
    comision = 0.10
else: 
    comision = 0.15

comiganada = montvendido * comision
suelbruto = suelbasico + comiganada

if suelbruto > 3500:
    descuento = 0.15
else:
    descuento = 0.08

descaplicado = suelbruto * descuento
suelneto = suelbruto - descaplicado

print("Sueldo bruto: ", suelbruto)
print("Comision aplicada: ", comiganada)
print("Descuento aplicado: ", descaplicado)
print("Sueldo neto: ", suelneto)