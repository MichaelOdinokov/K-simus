kus_vas={"Mis месяцы относятся к лету?":"juuni, juuli, august", "Какое растение символизирует лето?":"подсолнух", "Как называется праздник начала лета?":"летнее солнцестояние", "Как называется игра, которая играют на улице летом?":"лазертаг", "Какой фрукт считается символом лета?":"арбуз", "Какой цвет ассоциируется с летом?":"желтый", "Какой город в России считается летней столицей?":"Санкт-Петербург"}

def valik(n:int):# n=nimi
    """
    """
    if n==1:
        nimi

def nimi(n:int,i):#i=inimesed
    """
    """   
    if i<=5:
        if i==1:
            kusimus_vastused

def kusimus_vastused(n):
    """
    """
    
    print(f"Tere, {n}! Alustame küsitlust.")
    punktid=0    
    for kusimus, vastus in kus_vas.items():
        kasutaja_vastus = input(kusimus)
        if kasutaja_vastus.lower() == vastus.lower():
            print("Õige vastus!")
            punktid += 1
        else:
            print("Vale vastus!")    
    if punktid > 3:
        print(f"Tubli töö, {n}! Teie skoor oli {punktid}/7.")
        with open("oiged.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/7\n")
    else:
        print(f"Pole paha, {n}. Teie skoor oli {punktid}/7.")
        with open("valed.txt", "a", encoding="utf-8") as f:
            f.write(f"{n}: {punktid}/7\n")