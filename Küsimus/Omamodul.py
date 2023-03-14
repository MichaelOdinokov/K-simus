import random

kus_vas={}
with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
    for line in f:
        kusimus, vastus=line.strip().split(":")
        kus_vas[kusimus]=vastus

def kusimus_vastused_1(n):
    print(f"Tere, {n}! Alustame küsitlust.")
    punktid=0
    kusimus=random.shuffel
    for kusimus, vastus in kus_vas.items():
        kasutaja_vastus=input(kusimus)
        if kasutaja_vastus.lower()==vastus.lower():
            print("Õige vastus!")
            punktid+=1
        else:
            print("Vale vastus!")
    if punktid > 3:
        print(f"Tubli töö, {n}! Teie skoor oli {punktid}/5.")
        with open("oiged.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")
    else:
        print(f"Pole paha, {n}. Teie skoor oli {punktid}/5.")
        with open("valed.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/5\n")