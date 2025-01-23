from typing import List

class Ville:

    def __init__(self, nom:str, nb_habitants:int) -> None:
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def __str__(self) -> str:
        return f"Nom: {self.nom}, Nombre d'habitants : {self.nb_habitants}"

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def nb_habitants(self) -> int:
        return self.__nb_habitants

    @nom.setter
    def nom(self, nom: str) -> None:
        if len(nom) > 3 and len(nom) < 120:
            self.__nom = nom

    @nb_habitants.setter
    def nb_habitants(self, nb_habitants: int) -> None:
        if nb_habitants > 1 and nb_habitants < 1000000000:
            self.__nb_habitants = nb_habitants
        else:
            self.__nb_habitants = self.__nb_habitants

class Capitale(Ville):

    def __init__(self, nom:str, nb_habitants:int, monuments: List[str]) -> None:
        super().__init__(nom, nb_habitants)
        self.__monuments = monuments

    def __str__(self) -> str:
        return f"{super().__str__()}.\n Monuments : {', '.join(self.monuments)}"

    @property
    def monuments(self) -> List[str]:
        return self.__monuments

    @monuments.setter
    def monuments(self, monuments: List[str]) -> None:
        self.__monuments = monuments


if __name__ == "__main__":
    captital = Capitale("paris", 1000000, ["Tour effeil", "Arc de triomphe"])
    print(captital)
    captital.nb_habitants = 89
    print(captital)
    captital.nb_habitants = -6
    print(captital)
