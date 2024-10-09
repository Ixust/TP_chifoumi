import random

def choix_ordi():
    liste_ordi = ['p','f','c']
    choice_o = random.choice(liste_ordi)
    if choice_o == 'p':
        print("L'ordinateur a choisi la pierre")
    elif choice_o == 'f':
        print("L'ordinateur a choisi la feuille")
    else:
        print("L'ordinateur a choisi le ciseau")
    return choice_o

def verdict(ch, ch_o):
    if ch == 'p':
        if ch_o == 'p':
            return 0
        elif ch_o == 'f':
            return -1
        else:
            return 1
    elif ch == 'f':
        if ch_o == 'p':
            return 1
        elif ch_o == 'f':
            return 0
        else:
            return -1
    elif ch == 'c':
        if ch_o == 'p':
            return -1
        elif ch_o == 'f':
            return 1
        else:
            return 0
    else:
        return 2

def partie():
    choice = '0'
    rage = 0
    while choice.lower() != 'p' and choice.lower() != 'f' and choice.lower() != 'c':
        choice = str(input("Choisi un signe (p, f ou c)\n"))
        good = 1
        f_m = 'la'
        if choice.lower() == 'p':
            my_choice = "pierre"
        elif choice.lower() == 'f':
            my_choice = "feuille"
        elif choice.lower() == 'c':
            my_choice = "ciseau"
            f_m = 'le'
        else:
            good = 0
        if good == 1:
            print(f"Tu as choisie {f_m} {my_choice}")
        else:
            rage = rage + 1
            if rage == 5:
                print("Stop doing that!")        
            if rage == 10:
                print("Stooop!!")
            if rage == 15:
                print("...")
            if rage == 20:
                print("Keep Yourself Safe")
    return choice.lower()

def jeu_pfc():
    score = 0
    score_o = 0
    point = 2
    while True:
        if point != 0:
            print(f"Score: {score} - {score_o}")
        point = 2
        while point == 2:
            point = verdict(partie(), choix_ordi())
        if point == 0:
            print("Égalité")
        elif point == 1:
            print("Victoire!")
            score = score + 1
        else:
            print("Défaite...")
            score_o = score_o + 1
jeu_pfc()