seznam_ukolu = []

def pridat_ukol():
    prazdny_text= True
    while prazdny_text:
        nazev = input("zadej název úkolu: ")
        if nazev != "":
            break
        print("název úkolu musí být vyplněný!")
        
    prazdny_text= True
    while prazdny_text:
        popis = input("zadej popis úkolu: ")
        if popis != "":
            break
        print("popis úkolu musí být vyplněný!")  
    
    seznam_ukolu.append({"nazev":nazev, "popis": popis})
    print(f"Úkol {nazev} byl přidán do seznamu úkolů.")
    
    
    
def zobraz_ukoly():
    if len(seznam_ukolu) == 0:
        print("seznam úkolů je prázdný")
        return
    print("seznam úkolů: ")
    
    #for i in seznam_ukolu:
    #    print(f"{i['nazev']} - {i['popis']}")
    for i, t in enumerate(seznam_ukolu, start=1):
        print(f"{i}.{t['nazev']} - {t['popis']} ")

def odstranit_ukol():
    if len(seznam_ukolu) == 0:
        print("seznam úkolů je prázdný není co odstranit")
        return
    zobraz_ukoly()
    try:
        cislo_ukolu = int(input("Zadej číslo úkolu který chceš odstranit"))
        if 1 <= cislo_ukolu <= len(seznam_ukolu):
            odstraneny_ukol = seznam_ukolu.pop(cislo_ukolu - 1)
            print(f"Úkol '{odstraneny_ukol['popis']}' byl odstraněn")
        else:
            print("zadané číslo úkolu není v seznamu")
    except ValueError:
            print("musíš zadat celé číslo")


def hlavni_menu():
    volba = ""
    while volba != 4:
        print("Správce úkolů")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost (1-4):")
        
        match volba:
            case "1":
                print("zvolil jsi 1.")
                pridat_ukol()
                
            case "2":
                print("zvolil jsi 2.")
                zobraz_ukoly()

            case "3":
                print("zvolil jsi 3.")
                odstranit_ukol()
            case "4":
                print("zvolil jsi 4. Konec programu")
                break
                
            case _:
                print("zadali jste neplatnou volbu. Zkuste to prosím znovu")

#spuštění programu
hlavni_menu()

