import os 
os.system("cls")

Juandolar = float(input("Ingrese la cantidad aportada de Juan en dólares: "))
Rosadolar = float(input("Ingrese la cantidad aportada de Rosa en dólares: "))

Danisoles = float(input("Ingrese la cantidad aportada de Daniel en soles: "))

Danidolar = Danisoles / 3.00
capitotal = Juandolar + Rosadolar + Danidolar

Juanporcent = (Juandolar / capitotal) * 100
Rosaporcent= (Rosadolar / capitotal) * 100
Daniporcent = (Danidolar / capitotal) * 100

print(f"Capital total en dólares: ${capitotal:.2f}")
print(f"Juan aportó {Juanporcent:.2f}% del capitotal")
print(f"Rosa aportó {Rosaporcent:.2f}% del capitotal")
print(f"Daniel aportó {Daniporcent:.2f}% del capitotal")

