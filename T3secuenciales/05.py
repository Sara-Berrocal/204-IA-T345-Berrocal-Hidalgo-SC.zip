import os
os.system("cls")
gigabytes = int(input("Gigabytes: "))

megabytes = gigabytes * 1024.0
kilobytes = megabytes * 1024.0
bytes = kilobytes * 1024.0

print(f"megabytes:{megabytes:.2f}MB")
print(f"kilobytes:{kilobytes:.2f}KB")
print(f"bytes:{bytes:.2f} bytes")
