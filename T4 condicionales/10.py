import os 
os.system("cls")
 
notas = [float(input("Ingrese una nota: ")) for _ in range(5)]

notamax = max(notas)
notamin = min(notas)
print(f"Notas eliminadas : {notamax}, {notamin}")

notas.remove(max(notas)) 
notas.remove(min(notas))

promedio = sum(notas) / len(notas)

print(f"Promedio aprobatorio: {promedio:.2f}")
