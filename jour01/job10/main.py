class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("Le réservoir est trop bas pour démarrer.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir > 5


# Créer une instance de la classe Voiture
ma_voiture = Voiture("Toyota", "Corolla", 2015, 50000)

# Afficher les attributs de la voiture
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("Réservoir :", ma_voiture.get_reservoir())
print("En marche :", ma_voiture.get_en_marche())

# Démarrer la voiture
ma_voiture.demarrer()

# Afficher l'état de la voiture après l'avoir démarrée
print("En marche :", ma_voiture.get_en_marche())

# Ajouter de l'essence à la voiture
ma_voiture.set_reservoir(10)

# Démarrer la voiture à nouveau
ma_voiture.demarrer()

# Afficher l'état de la voiture après avoir ajouté de l'essence et l'avoir démarrée
print("Réservoir :", ma_voiture.get_reservoir())
print("En marche :", ma_voiture.get_en_marche())

# Arrêter la voiture
ma_voiture.arreter()

# Afficher l'état final de la voiture
print("En marche :", ma_voiture.get_en_marche())
