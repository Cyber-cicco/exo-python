class Voiture :

    def __init__(self, marque:str, nb_km:float=10000, ct_is_ok:bool=True, assurances:dict={}, niveau_essence:float=1.0) -> None:
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

def caca() -> None:
    pass

vroum = Voiture("Peugeot")
print(f"Ma voiture : {vroum}")
vroum.rouler(250, 0.3)
print(f"Ma voiture après avoir roulé : {vroum}")
