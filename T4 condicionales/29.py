import os
os.system("cls")

hrtrabajada = float(input("Ingrese las horas trabajadas: "))
tarihoraria = float(input("Ingrese el pago por hora: S/. "))
    
suelbruto = hrtrabajada * tarihoraria if hrtrabajada <= 48 else 48 * tarihoraria + (hrtrabajada - 48) * tarihoraria * 1.2
descuento = suelbruto * 0.11 if suelbruto > 1500 else 0 

print(f"Horas trabajadas: {hrtrabajada}\nPago por hora: S/. {tarihoraria:.2f}\nSueldo bruto: S/. {suelbruto:.2f}\nDescuento: S/. {descuento:.2f}\nTotal a pagar: S/. {suelbruto - descuento:.2f}")
