from functools import reduce

class Voiture:

    def __init__(self, marque:str, modele:str, prix:float) -> None:
        self.marque = marque
        self.modele = modele
        self.prix = prix
    
    def __str__(self):
        return f" Marque: {self.marque}, Modèle: {self.modele}, Prix: {self.prix}€"

class Garage:

    @classmethod
    def calculerTotalVoitures(cls, voitures: list[Voiture]) -> float:
        return reduce(lambda prix, voiture: prix + voiture.prix, voitures, 0)

    @staticmethod
    def calculerTotalVoituresStatic(voitures: list[Voiture]) -> float:
        return reduce(lambda prix, voiture: prix + voiture.prix, voitures, 0)

    def __init__(self, voitures:list[Voiture]) -> None:
         self.voitures = voitures

    def ajouter_voiture(voiture:Voiture) -> None:
        self.voitures.append(voiture)

    def __str__(self):
        acc = ""
        for voiture in self.voitures:
            acc += voiture.__str__() + "\n"
        return acc


garage = Garage([
    Voiture("peaugot", "S20", 30000),
    Voiture("citronin", "S21", 30000),
    Voiture("aaaaa", "S22", 30000),
    Voiture("prout", "S20", 30000),
])

total = Garage.calculerTotalVoitures(garage.voitures)
print(garage)
print(f"le total du prix des voitures dans le garage est de {total}")


