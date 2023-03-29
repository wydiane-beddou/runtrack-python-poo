class Personne:
    def __init__(self, age):
        self.age = age
        
    def afficherAge (self):
        print(self.age)
        
    def bonjour(self):
        return "Hello"
    
    class Eleve:
        def __init__(self, age):
            self.age = age
        
        def allerEnCours(self):
            return "Je vais en cours"
        
        def afficherAge(self):
            print(f"J'ai {self.age} ans")



P = Personne (14)
E = Personne.Eleve(6)

E.afficherAge()
P.afficherAge()
print(P.bonjour())

eleve_instance = Personne.Eleve("")
print(eleve_instance.allerEnCours())

class Professeur:
    def __init__(self, matiereEnseignée):
        self._matiereEnseignée = matiereEnseignée
        
    def enseigner(self):
        return f"Le cours va commencer."
        
Prof = Professeur("Mathématique")
print(Prof.enseigner())
        
