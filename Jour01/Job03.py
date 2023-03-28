class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def somme(self):
        return self.nombre1 + self.nombre2
    
    def addition(self, nombre1, nombre2):
        resultat = nombre1 + nombre2
        print(f"Le résultat de l'addition de {nombre1} et {nombre2} est {resultat}.")
        
op = Operation(0,0)
op.addition(12,3)