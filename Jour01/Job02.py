class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Le nombre1 est {self.nombre1}." f" Le nombre2 est {self.nombre2}."
    
Op = Operation(12,3)
print(Op)