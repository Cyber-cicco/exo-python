class CompteBancaire:

    def __init__(self, titulaire:str, solde:float=0) -> None:
        self.solde = solde
        self.titulaire = titulaire

    def depot(self, argent:float) -> bool:
        self.solde += argent
        return True

    def retrait(self, argent:float) -> bool:
        self.solde -= argent
        return True

    def afficher_solde(self) -> None:
        print(f"solde du compte de {self.titulaire} : {self.solde}")


class CompteEpargne(CompteBancaire):

    def __init__(self, titlulaire:str, solde:float=0, taux_interet:float=1) -> None:
        super().__init__(titlulaire, solde)
        self.taux_interet = taux_interet


    def ajouter_interet(self) -> None:
        self.solde += (self.solde / 100) * self.taux_interet

class CompteCourant(CompteBancaire):

    def __init__(self, titlulaire:str, solde:float=0, decouvert_max:float=150) -> None:
        super().__init__(titlulaire, solde)
        self.decouvert_max = decouvert_max


    def retrait(self, argent:float) -> bool:
        result = self.solde - argent
        if result < -self.decouvert_max :
            print("l'opération n'a pas pu aboutir")
            return False
        self.solde -= argent
        return True

compte_courant = CompteCourant("vincent")
compte_courant.depot(200)
compte_courant.afficher_solde()
compte_courant.retrait(350)
compte_courant.afficher_solde()
compte_courant.retrait(350)
compte_courant.afficher_solde()

compte_epargne = CompteEpargne("vincentin")
compte_epargne.depot(300)
compte_epargne.afficher_solde()
compte_epargne.ajouter_interet()
compte_epargne.afficher_solde()

