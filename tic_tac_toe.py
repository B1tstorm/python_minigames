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
intro = ['xxxxxxxxxxxxxxxxxxxxxxxxx',
        'x  Tic  |       |       x',
        'x-------|-------|-------x',
        'x       |  Tac  |       x',
        'x-------|-------|-------x',
        'x       |       |  Toe  x',
        'xxxxxxxxxxxxxxxxxxxxxxxxx']
for letter in intro:
    time.sleep(0.2)
    print(letter)
time.sleep(1.2)

# Variablen
spieler_eins = ''
spieler_zwei = '$'
spielen = True
# Spielfelder
sf = {'Q': ' ', 'W': ' ', 'E': ' ', 'A': ' ', 'S': ' ', 'D': ' ', 'Y': ' ', 'X': ' ', 'C': ' '}

def render_anleitung():
    anleitung = ['FELDER:',
            'xxxxxxxxxxxxxxxxxxxxxxxxx',
            'x   Q   |   W   |   E   x',
            'x-------|-------|-------x',
            'x   A   |   S   |   D   x',
            'x-------|-------|-------x',
            'x   Y   |   X   |   C   x',
            'xxxxxxxxxxxxxxxxxxxxxxxxx\n']
    for letter in anleitung:
            print(letter)

# Spielerauswahl
"""
spieler_eins = input("Spieler 1 waehle O oder X = ")
if spieler_eins == 'X':
    spieler_zwei = 'O'
else:
    spieler_zwei = 'X'
"""

def render_spielfeld():
    spielfeld = ['SPIELFELD:',
        'xxxxxxxxxxxxxxxxxxxxxxxxx',
        'x   ' + sf['Q'] + '   |   ' + sf['W'] + '   |   ' + sf['E'] + '   x',
        'x-------|-------|-------x',
        'x   ' + sf['A'] + '   |   ' + sf['S'] + '   |   ' + sf['D'] + '   x',
        'x-------|-------|-------x',
        'x   ' + sf['Y'] + '   |   ' + sf['X'] + '   |   ' + sf['C'] + '   x',
        'xxxxxxxxxxxxxxxxxxxxxxxxx']
    for letter in spielfeld:
        print(letter)

def check_feld(feld, spieler):
    frei = True
    while frei:
        if sf[feld] != ' ':
            print("Schon vergeben, waehle eine anderes Feld")
            feld = input("Feld ? = ")
        else:
            sf[feld] = spieler
            frei = False

def spiel():
    clear()
    render_anleitung()
    render_spielfeld()
    feld = input("Spieler 1! Welches Feld ? = ")
    check_feld(feld, spieler_eins)
    render_spielfeld()

    clear()
    render_anleitung()
    render_spielfeld()
    feld = input("Spieler 2! Welches Feld ? = ")
    check_feld(feld, spieler_zwei)
    render_spielfeld()

# TODO: - Ueberpruefen ob 3 Felder in Reihe das gleiche Symbol haben
def gewonnen():
    pass
# TODO: - Ueberpruefen ob alle Felder gefuellt sind
def ende():
    pass

while spielen:
    spiel()
