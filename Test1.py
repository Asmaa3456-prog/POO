class Etudiante:
    def __init__(self,nom,prenom,age,note) :
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.note = note
    def ajouterNote(self,points):
        print(self.note+points)
    def afficher(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Âge: {self.age},note est:{self.note}")
etudiante= Etudiante("elfathi","asmaa",18,13)
print(etudiante.afficher())
etudiante.ajouterNote(2)