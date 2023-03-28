import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur}{self.couleur}"

class Jeu:
    def __init__(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['♠', '♣', '♥', '♦']
        self.paquet = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
        random.shuffle(self.paquet)

    def piocher(self):
        return self.paquet.pop()

def valeur_main(cartes):
    valeur = 0
    as_compte = 0

    for carte in cartes:
        if carte.valeur in ['J', 'Q', 'K']:
            valeur += 10
        elif carte.valeur == 'A':
            as_compte += 1
            valeur += 11
        else:
            valeur += int(carte.valeur)

    while valeur > 21 and as_compte:
        valeur -= 10
        as_compte -= 1

    return valeur

def jouer_tour(jeu, main):
    main.append(jeu.piocher())
    return valeur_main(main)

def blackjack():
    jeu = Jeu()
    joueur_main = []
    croupier_main = []

    for _ in range(2):
        jouer_tour(jeu, joueur_main)
        jouer_tour(jeu, croupier_main)

    print("Main du joueur:", ', '.join(str(carte) for carte in joueur_main))
    print("Carte visible du croupier:", croupier_main[0])

    while input("Voulez-vous piocher une carte? (o/n): ").lower() == 'o':
        jouer_tour(jeu, joueur_main)
        print("Main du joueur:", ', '.join(str(carte) for carte in joueur_main))
        if valeur_main(joueur_main) > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
            return

    while valeur_main(croupier_main) < 17:
        jouer_tour(jeu, croupier_main)

    print("Main du croupier:", ', '.join(str(carte) for carte in croupier_main))

    if valeur_main(croupier_main) > 21:
        print("Le croupier a dépassé 21. Vous avez gagné!")
    elif valeur_main(joueur_main) > valeur_main(croupier_main):
        print("Vous avez gagné!")
    elif valeur_main(joueur_main) < valeur_main(croupier_main):
        print("Vous avez perdu.")
    else:
        print("Égalité.")

if __name__ == "__main__":
    blackjack()
