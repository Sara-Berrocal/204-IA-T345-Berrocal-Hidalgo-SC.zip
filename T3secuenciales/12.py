import os, math
os.system("cls")

a = 1
b = -6
c = 2

discriminante = b**2 - 4*a*c

x1 = (-b + math.sqrt(discriminante)) / (2 * a)
x2 = (-b - math.sqrt(discriminante)) / (2 * a)

print(f"Las soluciones son: x1= {x1} y x2= {x2}")

