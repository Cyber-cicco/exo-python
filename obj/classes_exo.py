class Voiture :
    modele:str

    def __init__(self, model:str) -> None:
        self.model = model

    def __str__(self) -> str:
        return "La voiture roule"

def caca() -> None:
    pass

vroum = Voiture("Peugeot")
print(vroum)
