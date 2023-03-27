class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_num_etudiant(self):
        return self.__num_etudiant

    def set_num_etudiant(self, num_etudiant):
        self.__num_etudiant = num_etudiant

    def get_credits(self):
        return self.__credits

    def set_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, Numéro étudiant: {self.__num_etudiant}, Niveau: {self.__level}")

# Instancier un objet représentant l’étudiant John Doe qui possède le numéro d’étudiant 145
john_doe = Student("Doe", "John", 145)

# Ajoutez-lui des crédits à trois reprises
john_doe.set_credits(20)
john_doe.set_credits(50)
john_doe.set_credits(30)

# Imprimer son total de crédits en console
print(john_doe.get_credits()) # affiche 100

# Imprimer les informations de l'étudiant en console
john_doe.studentInfo() # affiche "Nom: Doe, Prénom: John, Numéro étudiant: 145, Niveau: Très bien"
