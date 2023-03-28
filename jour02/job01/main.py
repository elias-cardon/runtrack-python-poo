# Classe Personne qui représente une personne générique avec un attribut 'age' et quelques méthodes
class Personne:
    # Constructeur de la classe Personne avec l'attribut 'age' initialisé à 14 par défaut
    def __init__(self, age=14):
        self.age = age

    # Méthode pour afficher l'âge de la personne en console
    def afficherAge(self):
        print("L'âge de la personne est de", self.age, "ans")

    # Méthode pour afficher 'Hello' en console
    def bonjour(self):
        print("Hello")

    # Méthode pour modifier l'âge de la personne
    def modifierAge(self, new_age):
        self.age = new_age

# Classe Eleve héritant de la classe Personne, représente un élève
class Eleve(Personne):
    # Méthode pour simuler le fait qu'un élève va en cours
    def allerEnCours(self):
        print("Je vais en cours")

    # Méthode pour afficher l'âge de l'élève avec le format "J'ai XX ans"
    def affichageAge(self):
        print("J'ai", self.age, "ans")

# Classe Professeur héritant de la classe Personne, représente un professeur
class Professeur(Personne):
    # Constructeur de la classe Professeur avec l'attribut privé matiere_enseignee et l'attribut age initialisé à 14 par défaut
    def __init__(self, matiere_enseignee, age=14):
        super().__init__(age)  # Appel du constructeur de la classe parente (Personne)
        self.__matiere_enseignee = matiere_enseignee

    # Méthode pour simuler le début d'un cours enseigné par le professeur
    def enseigner(self):
        print("Le cours va commencer")

# Instancier une classe "Personne" et une classe "Eleve"
personne1 = Personne()
eleve1 = Eleve()

# Instancier une classe "Professeur" avec la matière enseignée "Mathématiques"
professeur1 = Professeur("Mathématiques")

# Afficher l'âge par défaut de l'élève en console
eleve1.affichageAge()

# Simuler le fait que l'élève va en cours
eleve1.allerEnCours()

# Simuler le début d'un cours enseigné par le professeur
professeur1.enseigner()
