import math

# Définition de la classe abstraite Forme qui représente une forme géométrique
class Forme:
    # Méthode pour calculer l'aire de la forme (implémentation par défaut renvoyant 0)
    def aire(self):
        return 0

# Définition de la classe Rectangle héritant de Forme pour représenter un rectangle
class Rectangle(Forme):
    # Constructeur de la classe Rectangle avec la largeur et la hauteur comme arguments
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharger la méthode aire pour calculer l'aire du rectangle en multipliant la largeur et la hauteur
    def aire(self):
        return self.largeur * self.hauteur

# Définition de la classe Cercle héritant de Forme pour représenter un cercle
class Cercle(Forme):
    # Constructeur de la classe Cercle avec le rayon comme argument
    def __init__(self, radius):
        self.radius = radius

    # Surcharger la méthode aire pour calculer l'aire du cercle en utilisant la formule pi * r^2
    def aire(self):
        return math.pi * self.radius * self.radius

# Créer une instance de Rectangle avec une largeur de 5 et une hauteur de 10
mon_rectangle = Rectangle(5, 10)

# Créer une instance de Cercle avec un rayon de 3
mon_cercle = Cercle(3)

# Calculer et afficher l'aire du rectangle en appelant la méthode aire de l'instance mon_rectangle
print("Aire du rectangle:", mon_rectangle.aire())

# Calculer et afficher l'aire du cercle en appelant la méthode aire de l'instance mon_cercle
print("Aire du cercle:", mon_cercle.aire())