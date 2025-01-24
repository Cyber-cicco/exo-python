from typing import List, overload
import time
import random

class Formule1:

    def __init__(self, moteur:int, position:int, pilote:str, temperature_pneumatique:float=110, vitesse:float=200.0) -> None:
        self.__moteur = moteur
        self.__temperature_pneumatique = temperature_pneumatique
        self.__vitesse = vitesse
        self.__pilote = pilote
        self.__position = position

    @property
    def vitesse(self) -> float:
        return self.__vitesse

    @property
    def pilote(self) -> str:
        return self.__pilote

    @property
    def moteur(self) -> int:
        return self.__moteur

    @property
    def position(self) -> int:
        return self.__position

    @property
    def temperature_pneumatique(self) -> float:
        return self.__temperature_pneumatique

    @property
    def temperature_moteur(self) -> float:
        return (self.temperature_pneumatique * 0.9) * (self.vitesse * 0.11)

    @position.setter
    def position(self, position:int) -> None:
        if abs(self.__position - position) == 1:
            self.__position = position
        else:
            raise Exception("La position ne peut changer que de 1 rang")

    @temperature_pneumatique.setter
    def temperature_pneumatique(self, temperature_pneumatique:int) -> None:
        self.__temperature_pneumatique = temperature_pneumatique

    @vitesse.setter
    def vitesse(self, vitesse:float):
        self.__vitesse = vitesse

    def moteur_is_dead(self) -> bool:
        return self.temperature_pneumatique > 360
    
    def accelerer(self, amount:int) -> None:
        if amount > 0:
            self.__vitesse += amount
        else:
            raise Exception("Method only accepts positive values")
    
    def decelerer(self, amount:float) -> None:
        if amount > 0:
            self.__vitesse -= amount
        else:
            raise Exception("Method only accepts positive values")

    def drs(self) -> None:
        self.accelerer(self.vitesse * 0.15)

    def depassement(self, depasse) -> None:
        if depasse.position == self.position - 1:
            prev_pos = self.position
            self.position = depasse.position
            depasse.position = prev_pos
            print(f"{self.pilote} vient de dépasser {depasse.pilote} ! Que de rebondissements !")
        else:
            raise Exception("Un dépassement ne peut se faire qu'avec une personne juste devant soi")

    def __eq__(self, o) -> bool:
        return self.pilote == o.pilote

    def __str__(self) -> str:
        return f"{self.pilote}, {self.position}"

class Mercedes(Formule1):

    def __init__(self, moteur:int, position:int, pilote:str, temperature_pneumatique:float=110, vitesse:float=200.0):
        super().__init__(moteur, position, pilote, temperature_pneumatique,vitesse)

    def depassement(self, depasse):
        super().depassement(depasse)
        self.temperature_pneumatique -= self.temperature_pneumatique * 0.12


class Ferrari(Formule1):
    def __init__(self, moteur: int, position: int, pilote: str, temperature_pneumatique: float = 110, vitesse: float = 200.0):
        super().__init__(moteur, position, pilote, temperature_pneumatique, vitesse)

    @property
    def position(self) -> int:
        return super().position

    @position.setter
    def position(self, position: int) -> None:
        # Utilize the parent class's setter to handle validation
        super(Ferrari, Ferrari).position.__set__(self, position)
        # Alternatively: Formule1.position.fset(self, position)
        self.vitesse -= self.vitesse * random.randint(5, 12) / 100  # Adjusted to percentage

class Redbull(Formule1):

    def __init__(self, moteur:int, position:int, pilote:str, temperature_pneumatique:float=110, vitesse:float=200.0):
        super().__init__(moteur, position, pilote, temperature_pneumatique,vitesse)

    def depassement(self, depasse):
        super().depassement(depasse)
        if type(depasse) == Mercedes:
            self.temperature_pneumatique -= self.temperature_pneumatique * 0.08
            depasse.temperature_pneumatique += depasse.temperature_pneumatique * 0.12
        elif type(depasse) == Ferrari:
            self.temperature_pneumatique -= self.temperature_pneumatique * 0.08
            depasse.temperature_pneumatique += depasse.temperature_pneumatique * 0.14


class Formule1EnCourse:

    def __init__(self, formule1:Formule1):
        self.formule1 = formule1
        self.avancement = 0
        self.dead = False

    def __str__(self) -> str:
        return f"{self.formule1} : {self.avancement}"


class Course:

    def __init__(self, voitures: List[Formule1]) -> None:
        self.voitures = voitures
        self.voitures.sort(key=lambda e: e.position, reverse=True)
        self.avancement_voiture = []
        for voiture in self.voitures:
            self.avancement_voiture.append(Formule1EnCourse(voiture))

    def __creer_depassements(self) -> None:

        for voiture_av in self.avancement_voiture:
            if not voiture_av.formule1.moteur_is_dead():
                voiture_av.avancement += (voiture_av.formule1.vitesse / 60)


        self.avancement_voiture.sort(key=lambda e: e.avancement, reverse=True)

        break_loop = False
        while not break_loop:
            break_loop = True
            self.voitures.sort(key=lambda e: e.position)
            for index, voiture in enumerate(self.voitures):
                ## Si pas égale, c'est que la voitures qui se trouvait dans voitures a dépassé la voiture suivante
                if self.voitures[index] != self.avancement_voiture[index].formule1 and index != len(self.voitures) - 1:
                    print(f"{self.voitures[index+1]} dépasse {self.voitures[index]}")
                    self.voitures[index+1].depassement(self.voitures[index])
                    break_loop = False
                    break

                
        self.voitures.sort(key=lambda e: e.position)

        ## On vérifie la cohérence des données
        for index, voiture in enumerate(self.avancement_voiture):
            print(f"La voiture de {voiture.formule1.pilote} a avancé de {voiture.avancement}km")
            assert self.voitures[index] == self.avancement_voiture[index].formule1


    def __verifier_moteurs(self) -> None:
        for voiture_in_course in self.avancement_voiture:
            if voiture_in_course.formule1.moteur_is_dead() and not voiture_in_course.dead:
                print(f"La formule 1 de {voiture.pilote} vient de tomber en panne !")
                voiture_in_course.dead = True


    def lancer_course(self) -> None:
        for i in range (1, 30):
            self.__randomise_vitesse()
            self.__creer_depassements()
            self.__verifier_moteurs()
            time.sleep(1)
        print("La course est terminée ! Voici les résultats : ")

        for i, voiture in enumerate(self.voitures):
            print(f"Position n°{i + 1} : {voiture}")

    def __randomise_vitesse(self) -> None:
        for voiture in self.voitures:
            if not voiture.moteur_is_dead():
                rand_vitesse = random.randint(-20, 20)
                if rand_vitesse > 0:
                    voiture.accelerer(rand_vitesse)
                    print(f"{voiture.pilote} accélère !")
                elif rand_vitesse < 0:
                    voiture.decelerer(abs(rand_vitesse))
                    print(f"{voiture.pilote} ralentis !")

if __name__ == "__main__":
    course = Course([
        Ferrari(500, 1, "Vincent Vincent"),
        Redbull(500, 2, "Vincent Timètre"),
        Mercedes(500, 3, "Vincent Pité"),
    ])
    course.lancer_course()
