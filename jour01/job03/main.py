class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def afficher_attributs(self):
        print("Le nombre1 est", self.nombre1)
        print("Le nombre2 est", self.nombre2)

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", resultat)

# Créer un objet Operation avec les valeurs 2 et 3 pour nombre1 et nombre2
operation = Operation(12, 3)

# Afficher les attributs de l'objet operation
operation.afficher_attributs()

# Appeler la méthode addition pour calculer la somme de nombre1 et nombre2
operation.addition()