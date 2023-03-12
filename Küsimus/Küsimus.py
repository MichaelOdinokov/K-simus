from Omamodul import*
kus=[] 
vastu=[] 
oiged=[]
while True:
    kogus=int(input("Mitu inimesi osaleb?"))
    if kogus<=3:
        if kogus==1:
            n=kusimus_vastused_1(input("Sissetage sinu nimi:"))
        elif kogus==2:
            for i in range(2):
                n=kusimus_vastused_2(input("Sissetage sinu nimi:"))
        elif kogus==3:
            n=kusimus_vastused_3(input("Sissetage sinu nimi:"))

    
