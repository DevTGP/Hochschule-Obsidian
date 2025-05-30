#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:37:58 2025

@author: schmitz
"""



##  Probeklausur

# %% Aufgabe 1
###############################################################################


def vokale(w):
    pass            # diese Zeile durch Ihre Lösung ersetzen!


# Testfälle
print(vokale('Auto'))                     # Sollergebis: 3
print(vokale('Fachbereich Informatik'))   # Sollergebis: 8
print(vokale(''))                         # Sollergebis: 0
print(vokale('AaEeIiOoUu '))              # Sollergebis: 10
print(vokale('1234&%$'))                  # Sollergebis: 0

# Ihre weiteren Testfälle:
    



# %% Aufgabe 2
###############################################################################

def fib_liste(n):
    pass            # diese Zeile durch Ihre Lösung ersetzen!


print(fib_liste(0))     # Sollergebis: [0]
print(fib_liste(1))     # Sollergebis: [0, 1]
print(fib_liste(2))     # Sollergebis: [0, 1, 1]
print(fib_liste(3))     # Sollergebis: [0, 1, 1, 2]
print(fib_liste(9))     # Sollergebis: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]




def fib_gerade(k):
    pass            # diese Zeile durch Ihre Lösung ersetzen!


print(fib_gerade(1))     # Sollergebis: [0]
print(fib_gerade(2))     # Sollergebis: [0, 2]
print(fib_gerade(3))     # Sollergebis: [0, 2, 8]
print(fib_gerade(4))     # Sollergebis: [0, 2, 8, 34]
print(fib_gerade(5))     # Sollergebis: [0, 2, 8, 34, 144]



# %% Aufgabe 3
###############################################################################

def entferne_zeichen(w, c):
    pass            # diese Zeile durch Ihre Lösung ersetzen!


print(entferne_zeichen('Hallo', 'l'))       # Sollergebis: 'Hao'
print(entferne_zeichen('Python', 'y'))      # Sollergebis: 'Pthon'
print(entferne_zeichen('Python', 'x'))      # Sollergebis: 'Python'
print(entferne_zeichen('', 'l'))            # Sollergebis: ''
print(entferne_zeichen('aaabbbcb', 'b'))    # Sollergebis: 'aaac'
print(entferne_zeichen('Hallo Welt', ' '))  # Sollergebis: 'HalloWelt'
print(entferne_zeichen('Python', 'p'))      # Sollergebis: 'Python'




# %% Aufgabe 4
###############################################################################

def pi_approx10():
    pass            # diese Zeile durch Ihre Lösung ersetzen!


print(pi_approx10())       # Sollergebis: 3.0395075895610533

# Differenz zu math.pi?    # Sollergebis: 0.10208506402873985



def pi_approx(k):
    pass            # diese Zeile durch Ihre Lösung ersetzen!


print(pi_approx(1))       # Sollergebnis: 2.449489742783178
print(pi_approx(2))       # Sollergebnis: 2.7386127875258306
print(pi_approx(5))       # Sollergebnis: 2.9633877010385707
print(pi_approx(10))      # Sollergebnis: 3.04936163598207
print(pi_approx(11))      # Sollergebnis: 3.0574815067075627






# %% Aufgabe 5
###############################################################################

Saison = [('H', 3, 2),      # Heimspiel gewonnen 
          ('A', 0, 1),      # Auswärtsspiel gewonnen
          ('H', 1, 1),      # Heimspiel unentschieden
          ('H', 1, 2),      # Heimspiel verloren
          ('A', 7, 0),      # Auswärtsspiel verloren
          ('H', 3, 1),      # usw.
          ('A', 2, 2),
          ('A', 1, 1)]


def tordiff(S):
    pass            # diese Zeile durch Ihre Lösung ersetzen!

def ergebnis(S):
    pass            # diese Zeile durch Ihre Lösung ersetzen!

def heimstark(S):
    pass            # diese Zeile durch Ihre Lösung ersetzen!

def torhist(S):
    pass            # diese Zeile durch Ihre Lösung ersetzen!


print(tordiff(Saison))          # Sollergebis: -4  (12 Tore geschossen, 16 Tore kassiert)
print(ergebnis(Saison))         # Sollergebis: (3, 2, 3)
print(heimstark(Saison))        # Sollergebis: True
print(torhist(Saison))          # Sollergebis: {1: 1, 2: 2, 3: 1, 4: 2, 5: 1, 7: 1}




