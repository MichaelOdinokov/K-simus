from random import*

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

def kusimus_vastused(n:int):
        n=input("Sissetage sinu nimi:")
        print(f"Привет, {n}! Начнем наш опрос.")
        k=input("Mis месяцы относятся к лету?")#juuni, juuli, august
        k=input("Какое растение символизирует лето?") #подсолнух
        k=input("Как называется праздник начала лета?") #летнее солнцестояние
        k=input("Как называется игра, которая играют на улице летом?") #лазертаг
        k=input("Какой фрукт считается символом лета?") #арбуз
        k=input("Какой цвет ассоциируется с летом?") #желтый
        k=input("Какой город в России считается летней столицей?") #Санкт-Петербург 
        f=open("kusimused_vastused.txt", "r", encoding="utf-8")
        print(f.read())

            
"""          
def test_word_knowledge(rus:list, est: list)->str:
    kokku=int(input("Mitu küsimust?"))
    for i in range(kokku):
        järjend=choice=([rus, est])
        sõna=choice(järjend)
        print(f"{sõna}")
        tõlke=input()
        if sõna in rus:
            i=rus.index(sõna)
            tõlke_kontroll=est[i]
        elif sõna in est:
            i=est.index(sõna)
            tõlke_kontroll=rus[i]
        if tõlke==tõlke_kontroll:
            p+=1
            print("Õige")
        else:
            print("Vale")
        p=5
    if (p/kokku)*100>90:
        hinne=5
    elif (p/kokku)*100>75:
        hinne=4
    elif (p/kokku)*100>60:
        hinne=3
    else:
        hinne="Väga halb"
    return hinne
                
"""
                


