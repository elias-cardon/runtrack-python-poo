# Classe Rectangle représentant un rectangle avec des attributs privés longueur et largeur
class Rectangle:
    # Constructeur de la classe Rectangle avec les attributs privés longueur et largeur
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Méthode pour calculer et retourner le périmètre du rectangle
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer et retourner la surface du rectangle
    def surface(self):
        return self.__longueur * self.__largeur

    # Méthode pour obtenir la longueur du rectangle
    def get_longueur(self):
        return self.__longueur

    # Méthode pour obtenir la largeur du rectangle
    def get_largeur(self):
        return self.__largeur

    # Méthode pour modifier la longueur du rectangle
    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Méthode pour modifier la largeur du rectangle
    def set_largeur(self, largeur):
        self.__largeur = largeur

# Classe Parallelepipede héritant de la classe Rectangle et représentant un parallélépipède
class Parallelepipede(Rectangle):
    # Constructeur de la classe Parallelepipede avec l'attribut privé hauteur en plus des attributs hérités de Rectangle
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Méthode pour calculer et retourner le volume du parallélépipède
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur

    # Méthode pour obtenir la hauteur du parallélépipède
    def get_hauteur(self):
        return self.__hauteur

    # Méthode pour modifier la hauteur du parallélépipède
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

# Instanciation de la classe Rectangle avec une longueur de 4 et une largeur de 6
rect = Rectangle(4, 6)

# Test des méthodes de la classe Rectangle pour calculer le périmètre et la surface
print("Périmètre du rectangle :", rect.perimetre())  # 20
print("Surface du rectangle :", rect.surface())  # 24

# Modification des attributs du rectangle
rect.set_longueur(5)
rect.set_largeur(7)

# Test des méthodes de la classe Rectangle après modification pour calculer le périmètre et la surface
print("Périmètre du rectangle modifié :", rect.perimetre())  # 24
print("Surface du rectangle modifié :", rect.surface())  # 35

# Instanciation de la classe Parallélépipède avec une longueur de 4, une largeur de 6 et une hauteur de 8
para = Parallelepipede(4, 6, 8)

# Test de la méthode de la classe Parallélépipède pour calculer le volume
print("Volume du parallélépipède :", para.volume())  # 192
