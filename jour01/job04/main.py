class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return "Je m'appelle {} {}.".format(self.nom, self.prenom)


# Créer plusieurs objets Personne avec des valeurs de construction différentes
personne1 = Personne("Dupont", "Pierre")
personne2 = Personne("Martin", "Sophie")
personne3 = Personne("Lefebvre", "Jacques")

# Appeler la méthode SePresenter pour afficher les noms et prénoms de chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
