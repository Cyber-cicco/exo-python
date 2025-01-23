class CompteBancaire:

    def __init__(self,numero_compte:str, nom:str, solde:float=0) -> None:
        self.numero_compte = numero_compte
        self.solde = solde
        self.nom = nom

    # Retourne un booléen pour savoir si l'opération a aboutie
    def versement(self, argent:float) -> bool:
        self.solde += argent
        return True

    # Retourne un booléen pour savoir si l'opération a aboutie
    def retrait(self, argent:float) -> bool:
        self.solde -= argent
        return True

    def comission(self) -> None:
        self.solde -= self.solde * 0.05

    def afficher(self) -> None:
        print(f"Numéro de compte : {self.numero_compte}\n Titulaire : {self.nom} \n Solde : {self.solde}")


