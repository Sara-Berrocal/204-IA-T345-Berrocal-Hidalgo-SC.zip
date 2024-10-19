import os
os.system("cls")
    
montvendido = float(input("Ingrese el monto total vendido: S/. "))
sueldot     = montvendido * 0.10 + (max(0, (montvendido - 5000) // 500)*25)
    
print(f"Sueldo total del vendedor: S/. {sueldot:.2f}")
