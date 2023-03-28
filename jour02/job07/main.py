import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        valeurs = list(range(2, 11)) + ['Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Coeur', 'Carreau', 'Trefle', 'Pique']
        self.paquet = [Carte(v, c) for v in valeurs for c in couleurs]
        random.shuffle(self.paquet)

    def piocher(self):
        return self.paquet.pop()

    def valeur_main(self, main):
        valeur = 0
        as_present = False
        for carte in main:
            if carte.valeur == 'As':
                as_present = True
                valeur += 11
            elif carte.valeur in ['Valet', 'Dame', 'Roi']:
                valeur += 10
            else:
                valeur += carte.valeur

        if as_present and valeur > 21:
            valeur -= 10

        return valeur

    def jouer_partie(self):
        main_joueur = [self.piocher(), self.piocher()]
        main_croupier = [self.piocher(), self.piocher()]

        print("Main du joueur:", main_joueur)
        print("Main du croupier:", main_croupier[0], "et une carte cachée")

        while True:
            choix = input("Souhaitez-vous piocher (P) ou passer (S) ? ").lower()
            if choix == 'p':
                main_joueur.append(self.piocher())
                print("Main du joueur:", main_joueur)
                if self.valeur_main(main_joueur) > 21:
                    print("Vous avez dépassé 21, vous avez perdu.")
                    return
            elif choix == 's':
                break
            else:
                print("Choix invalide, veuillez choisir P ou S.")

        while self.valeur_main(main_croupier) < 17:
            main_croupier.append(self.piocher())

        print("Main du croupier:", main_croupier)

        if self.valeur_main(main_croupier) > 21:
            print("Le croupier a dépassé 21, vous avez gagné !")
        elif self.valeur_main(main_joueur) > self.valeur_main(main_croupier):
            print("Vous avez gagné !")
        else:
            print("Le croupier a gagné.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer_partie()