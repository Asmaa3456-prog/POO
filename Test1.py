# basics of oop :
# creation of classes, function#
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
etudiante= Etudiante("fth","asmaa",18,13)
print(etudiante.afficher())
etudiante.ajouterNote(2)
#########
class Prof:
    def __init__(self,nom,prenom,age) :
        # encapsulation "nom" public-->private(.__)#
        self.__nom = nom
        self.prenom = prenom
        self.age = age
        # how to create getter and setter methode#
    def getNom(self):
        return self.__nom
    def setNom(self,nom):
        self.__nom=nom
per=Prof("fthprv","asmaa",18)
per.setNom("fthpub")
print(per.getNom())
#make ur code more precis:
# heritage:(heritage simple)#
class animals():# this class-mom collect the same shared attributes  #
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def affiche(self):#simple way to affiche ur code with the function#
        print(f"cat-color:",self.color)
class cat(animals):# must tagging the class-mom in the class-child#
    def __init__(self,color,name,eyes1):
        animals.__init__(self,color,name)#must tagging the constructor of the class-mom#
        self.eyes=eyes1
    def affiche(self):
        super().affiche()#super():he take the attrubutes from the class-mom#
class dog(animals):# must tagging the class-mom in the class-child#
    def __init__(self, color,name,eyes2):
        animals.__init__(self,color,name)#must tagging the constructor of the class-mom#
        self.eyes=eyes2
anim1=cat("orange","kittie","green")
anim1.affiche()
anim2=dog("white","moon","brown")
print(f"cat-color:{anim1.color},her name:{anim1.name},her eyes-color:{anim1.eyes}")
print(f"dog-color:{anim2.color},his name:{anim2.name},his eyes-color:{anim2.eyes}")



