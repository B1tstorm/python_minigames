import random
import time
from os import system, name

# Konsolenausgabe loeschen
def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

clear()

# Intro
intro = ['***************************',
        '*                         *',
        '*  Schere, Stein, Papier  *',
        '*                         *',
        '***************************']
for letter in intro:
    time.sleep(0.4)
    print(letter)
time.sleep(1.2)

# Punkte
class Punkte():
    punkte = 0

# Variablen
figuren = {1: "Schere", 2: "Stein", 3: "Papier"}
spieler_punkte = Punkte.punkte
gegner_punkte = Punkte.punkte
spielen = True

while spielen:
    clear()
    print("Du {1}:{0} Gegner".format(gegner_punkte, spieler_punkte))
    # Auswahl des Spielers
    spieler_wahl = int(input("Waehle [1]Schere, [2]Stein, [3]Papier = "))
    #spieler_wahl = random.randint(1, 3) # Computer spieler

    # Gegner waehlt
    gegner_wahl = random.randint(1, 3)

    # Ladezeit
    loading = ["Spiel beginnt", ".", ".", ".", "\n\n"]
    for i in loading:
        print(i, end='')
        time.sleep(0.4)

    # Gewinner ermittlung
    print("{} vs. {}".format(figuren[spieler_wahl], figuren[gegner_wahl]))
    time.sleep(1)
    if spieler_wahl == gegner_wahl:
        print("Unentschieden")
    else:
        if spieler_wahl == 1:
            if gegner_wahl == 2:
                gegner_punkte += 1
                print("Der Gegner bekommt einen Punkt")
            elif gegner_wahl == 3:
                spieler_punkte += 1
                print("Punkt fuer dich")
        elif spieler_wahl == 2:
            if gegner_wahl == 3:
                gegner_punkte += 1
                print("Punkt fuer den Gegner")
            elif gegner_wahl == 1:
                spieler_punkte += 1
                print("Du bekommst einen Punkt")
        elif spieler_wahl == 3:
                if gegner_wahl == 1:
                    gegner_punkte += 1
                    print("Den Punkt bekommt der Gegner")
                elif gegner_wahl == 2:
                    spieler_punkte += 1
                    print("Der Punkt geht an dich")
    time.sleep(2)
    
    # Punktestand der Spieler ermitteln
    if spieler_punkte == 3:
        print("\nDu {1}:{0} Gegner".format(gegner_punkte, spieler_punkte))
        print("Du hast gewonnen!\n")
        restart = input("Erneut spielen ? [y] = ")
        if restart != 'y':
            spielen = False
        else:
            spieler_punkte = 0
            gegner_punkte = 0
            continue
    elif gegner_punkte == 3:
        print("\nDu {1}:{0} Gegner".format(gegner_punkte, spieler_punkte))
        print("Verlierer!\n")
        restart = input("Erneut spielen ? [y] = ")
        if restart != 'y':
            spielen = False
        else:
            spieler_punkte = 0
            gegner_punkte = 0
            continue
        