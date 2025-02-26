###Polymorphisme:
## Exemple de redéfinition :#
class Personne:
    def __init__(self, nom, cin, dateNaiss):
        self.nom = nom
        self.cin = cin
        self.dateNaiss = dateNaiss

    def afficher(self):
        print("Personne", self.nom)

class Etudiant(Personne):
    def __init__(self, nom, cin, dateNaiss, note1, note2):
        super().__init__(nom, cin, dateNaiss)
        self.note1 = note1
        self.note2 = note2

    def moyenne(self):
        return (self.note1 + self.note2) / 2

    def afficher(self):# Redéfinit la méthode `afficher` de la classe parente pour afficher le nom de l'étudiant avec le préfixe "Etudiant".#
        # Redéfinition de la méthode `afficher`#
        print("Etudiant", self.nom)

# Création des instances
p1 = Personne("Imad", "A876549", "05/12/2000")
e1 = Etudiant("Sara", "A876559", "05/11/2000", 15, 18)

# Appel des méthodes `afficher`
p1.afficher()
e1.afficher()

# Affichage de la moyenne pour l'étudiant
print(f"Moyenne de {e1.nom}: {e1.moyenne()}")
print("###########")
## Un exemple de Surcharge de méthode à l'aide d'arguments variables.#
class Personne:
#le surcharger une méthode en utilisant des arguments variables pour calculer la moyenne de différentes combinaisons de notes.#
    def __init__(self,nom,cin,dateNaiss):
        self.nom = nom
        self.cin = cin
        self.dateNaiss = dateNaiss
    def age(self):
        print(self.age)
    def afficher(self):
        print("Personne",self.nom)
class Etudiant(Personne):
    def __init__(self, nom, cin, dateNaiss, note1, note2):
        super().__init__(nom, cin, dateNaiss)
        self.note1 = note1
        self.note2 = note2

    def Moyene(self, *args):
        if len(args) == 0:  #Calcule la moyenne des attributs de l'objet #
            return (self.note1 + self.note2) / 2
        elif len(args) == 2:
            return (args[0] + args[1]) / 2
        else:   #Autres cas: Lève une exception `ValueError` si le nombre d'arguments n'est pas 0 ou 2 .#
            raise ValueError("La méthode accepte soit 0 soit 2 paramètres")

class Etudiant2(Personne):
    def __init__(self, nom, cin, dateNaiss, note1, note2, note3, note4):
        super().__init__(nom, cin, dateNaiss)
        self.note1 = note1
        self.note2 = note2
        self.note3 = note3
        self.note4 = note4

    def Moyene(self, *args):
        try:
            if len(args) == 0:#Calcule la moyenne de quatre attributs de l'objet .#
                return (self.note1 + self.note2 + self.note3 + self.note4) / 4
            elif len(args) == 2:#Calcule la moyenne des deux arguments fournis.#
                return (args[0] + args[1]) / 2
            elif len(args) == 4:# Calcule la moyenne des quatre arguments fournis.#
                return sum(args) / 4
        except ValueError as e:  #Autres cas: Lève une exception `ValueError` si le nombre d'arguments n'est pas 0, 2 ou 4.#
           print(e)

# Tests
print("les moyennes de Sara *:")
print("moyenne 1: 2 arg")
e1 = Etudiant(f"Sara", "A876559", "05/11/2000",15, 18)
print(e1.Moyene())
print("moyenne 1: 2 arg")
print(e1.Moyene(12, 16))
print("les moyennes de ALI §:")
print("moyenne 1: 4 arg")
e2 = Etudiant2("Ali", "B123456", "01/01/2000", 14, 16, 18, 20)
print(e2.Moyene())
print("moyenne 2: 2 arg")
print(e2.Moyene(10, 12))
print("moyenne 3: 4 arg")
print(e2.Moyene(10, 12, 14, 16))


