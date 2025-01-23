class Etudiant:

    def __init__(self, nom:str, note_info:float, note_maths:float) -> None:
        self.nom = nom
        self.note_info = note_info
        self.note_maths = note_maths

    def __str__(self) -> str:
        return f"Etudiant {self.nom}, moyenne générale : {self.moyenne_generale}"

    @property
    def moyenne_generale(self) -> float:
        return (self.note_info + self.note_maths) / 2

if __name__ == "__main__":
    etudiants = [
        Etudiant("Vincent_1", 12, 9),
        Etudiant("Vincent_2", 13, 6),
        Etudiant("Vincent_3", 18, 13),
        Etudiant("Vincent_4", 14, 8),
        Etudiant("Vincent_5", 15, 20),
        Etudiant("Vincent_6", 15, 20),
    ]

    print()
    print("Étudiants")
    for etudiant in etudiants:
        print(etudiant)

    classement = list(etudiants)
    classement.sort(key=lambda e: e.moyenne_generale)


    print()
    print("Classement des étudiants")
    for etudiant in classement:
        print(etudiant)

    d = {}

    prev = None
    result = []
    for etudiant in classement:
        if prev != None and prev.moyenne_generale == etudiant.moyenne_generale:
            result.append(prev)
            result.append(etudiant)
        prev = etudiant

    print()
    print("Étudiants ayant la même moyenne")
    for etudiant in result:
        print(etudiant)
            

