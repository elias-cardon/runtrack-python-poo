class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instancier un objet Animal et afficher son âge
animal = Animal()
animal.nommer("Fido")

# Afficher le nom de l'animal
print("Nom de l'animal :", animal.prenom)

print("Âge de l'animal avant vieillissement :", animal.age)

# Faire vieillir l'animal et afficher son âge
animal.vieillir()
print("Âge de l'animal après vieillissement :", animal.age)

