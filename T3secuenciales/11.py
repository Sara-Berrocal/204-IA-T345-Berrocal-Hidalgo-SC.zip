import os
os.system("cls")

num1 = 123
num2 = 456

c1_1 = num1 // 100
c2_1 = (num1 // 10) % 10
c3_1 = num1 % 10

c1_2 = num2 // 100
c2_2 = (num2 // 10) % 10
c3_2 = num2 % 10

nume1 = c3_2 * 100 + c2_1 * 10 + c1_2
nume2 = c3_1 * 100 + c2_2 * 10 + c1_1

print(f"Los numeros seran: {nume1} y {nume2}")
