class Personne:
    def __init__(self, age):
        self.age = age
        
    def afficherAge (self):
        print(self.age)
        
    def bonjour(self):
        print ("Hello")
    
    class Eleve:
        def __init__(self, age):
            self.age = age
        
        def allerEnCours(self):
            return "Je vais en cours"
        
        def afficherAge(self):
            print(f"J'ai {self.age} ans")



P = Personne (14)
E = Personne.Eleve(6)

print(P.bonjour())
print(E.allerEnCours())

E.age = 15
E.afficherAge()


class Professeur:
    def __init__(self, matiereEnseignée):
        self._matiereEnseignée = matiereEnseignée
        
    def enseigner(self):
        return f"Le cours va commencer."
        
