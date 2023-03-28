class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom
        
        
    def vieillir(self): 
        self.age += 1
    
    def nommer(self):
        self.prenom = "Luna"

animal = Animal(0, "")
print("L'age de l'animal", animal.age, "ans")
animal.vieillir()
print("L'age de l'animal", animal.age, "ans")
animal.nommer()
print("L'animal se nomme", animal.prenom)