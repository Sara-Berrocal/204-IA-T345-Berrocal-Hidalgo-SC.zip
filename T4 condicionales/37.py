import os 
os.system("cls")

pamela = int(input("Ingrese los votos para Pamela: "))
carol = int(input("Ingrese los votos para Carol: "))
fanny = int(input("Ingrese los votos para Fanny: "))

tvotos = pamela + carol + fanny
mitadmasuno = (tvotos // 2) + 1

if pamela >= carol and pamela >= fanny:
    puesto1 = "Pamela"
    votos1  = pamela
    if carol >= fanny:
        puesto2 = "Carol"
        votos2  = carol
        puesto3 = "Fanny"
        votos3  = fanny
    else:
        puesto2 = "Fanny"
        votos2  = fanny
        puesto3 = "Carol"
        votos3  = carol

elif carol >= pamela and carol >= fanny:
    puesto1 = "Carol"
    votos1 = carol
    if pamela >= fanny:
        puesto2 = "Pamela"
        votos2  = pamela
        puesto3 = "Fanny"
        votos3  = fanny
    else:
        puesto2 = "Fanny"
        votos2  = fanny
        puesto3 = "Pamela"
        votos3  = pamela
else:
    puesto1 = "Fanny"
    votos1  = fanny
    if pamela >= carol:
        puesto2 = "Pamela"
        votos2  = pamela
        puesto3 = "Carol"
        votos3 = carol
    else:
        puesto2 = "Carol"
        votos2  = carol
        puesto3 = "Pamela"
        votos3  = pamela

if pamela == carol == fanny:
    print("Empate entre las tres candidatas")
elif votos2 == votos3:
    print("Empate por el segundo puesto.")
elif votos1 >= mitadmasuno:
    print(f"{puesto1} ganó la elección.")
else:
    print(f"Segunda vuelgta entre {puesto1} y {puesto2}.")
    
