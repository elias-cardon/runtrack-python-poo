# Classe Vehicule avec marque, modele, annee et prix comme attributs
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    # Méthode pour afficher les informations du véhicule
    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}")

    # Méthode pour démarrer le véhicule
    def demarrer(self):
        print("Attention, je roule")


# Classe Voiture héritant de la classe Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4  # Attribut spécifique à la classe Voiture pour le nombre de portes

    # Méthode pour afficher les informations de la voiture, en incluant le nombre de portes
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    # Méthode pour démarrer la voiture avec un message personnalisé
    def demarrer(self):
        print("Attention, la voiture démarre")


# Classe Moto héritant de la classe Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2  # Attribut spécifique à la classe Moto pour le nombre de roues

    # Méthode pour afficher les informations de la moto, en incluant le nombre de roues
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    # Méthode pour démarrer la moto avec un message personnalisé
    def demarrer(self):
        print("Attention, la moto démarre")


# Instanciation d'une Voiture avec marque, modèle, année et prix
ma_voiture = Voiture("Peugeot", "208", 2021, 25000)
# Affichage des informations de la voiture
ma_voiture.informationsVehicule()
# Démarrage de la voiture
ma_voiture.demarrer()

print()

# Instanciation d'une Moto avec marque, modèle, année et prix
ma_moto = Moto("Yamaha", "MT-07", 2020, 15000)
# Affichage des informations de la moto
ma_moto.informationsVehicule()
# Démarrage de la moto
ma_moto.demarrer()
