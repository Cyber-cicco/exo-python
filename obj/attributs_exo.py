class Voiture :

    def __init__(self, marque:str, nb_km:float=10000, ct_is_ok:bool=True, assurances:dict={"2024":"MMA", "2025" : "Amélie", "2023": "CIC"}, niveau_essence:float=1.0) -> None:
        self.marque = marque
        self.nb_km = nb_km
        self.ct_is_ok = ct_is_ok
        self.assurances = assurances
        self.niveau_essence = niveau_essence

    def __str__(self) -> str:
        return f" Marque : {self.marque}\n Kilométrage : {self.nb_km}\n Niveau d'essence : {self.niveau_essence} \n"

    def rouler(self, km:float, consommation_essence:float):
        self.niveau_essence -= consommation_essence
        self.nb_km += km

    def get_assurance(self):
        return sorted(self.assurances.items())[-1][1]

vroum = Voiture("Peugeot")
print(f"Ma voiture : {vroum}")
vroum.rouler(250, 0.3)
print(f"Ma voiture après avoir roulé : {vroum}")
print(f"Elle s'est crashée ! Heureusement, il y a {vroum.get_assurance()}")
