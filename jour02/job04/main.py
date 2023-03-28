# Classe de base Forme pour représenter des formes géométriques
class Forme:
    # Calcule l'aire de la forme (0 par défaut pour une forme générique)
    def aire(self):
        return 0

# Classe Rectangle héritant de Forme
class Rectangle(Forme):
    # Constructeur prenant la largeur et la hauteur du rectangle
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Calcule l'aire du rectangle (largeur * hauteur)
    def aire(self):
        return self.largeur * self.hauteur

# Crée un rectangle de largeur 5 et hauteur 10
mon_rectangle = Rectangle(5, 10)

# Affiche l'aire du rectangle
print(mon_rectangle.aire())
