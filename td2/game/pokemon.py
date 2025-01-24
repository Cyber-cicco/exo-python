class Pokemon:
    WEAKNESS_MULT = 2.0
    RESIST_MULT = 0.5

    def __init__(self, nom: str, hp: int, atk: int) -> None:
        self.__nom = nom
        self.__hp = hp
        self.__hp_max = hp
        self.__atk = atk
        self.afinities_dict = {}

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def atk(self) -> int:
        return self.__atk

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def hp_max(self) -> int:
        return self.__hp_max

    def is_dead(self) -> bool:
        return self.hp == 0

    def take_damage(self, pokemon) -> int:
        multiplier = 1
        if self.afinities_dict.get(type(pokemon)) is not None:
            multiplier = self.afinities_dict[type(pokemon)]
        dmg = int(pokemon.atk * multiplier)
        res = self.hp - dmg  # Fixed assignment
        if res < 0:
            self.__hp = 0
        else:
            self.__hp = res
        return int(dmg)

    def attaquer(self, pokemon) -> None:
        pokemon.take_damage(self.atk, self)  # Pass 'self' as the attacker

    def __str__(self) -> str:
        return f"{self.nom} est un pokemon normal. Caractéristiques : \n HP: {self.hp}/{self.hp_max}\n Atk : {self.atk}"

class TypePlante(Pokemon):
    def __init__(self, nom: str, hp: int, atk: int) -> None:
        super().__init__(nom, hp, atk)
        self.afinities_dict[TypeFeu] = Pokemon.WEAKNESS_MULT
        self.afinities_dict[TypePlante] = Pokemon.RESIST_MULT
        self.afinities_dict[TypeEau] = Pokemon.RESIST_MULT

class TypeFeu(Pokemon):
    def __init__(self, nom: str, hp: int, atk: int) -> None:
        super().__init__(nom, hp, atk)
        self.afinities_dict[TypeFeu] = Pokemon.RESIST_MULT
        self.afinities_dict[TypePlante] = Pokemon.RESIST_MULT
        self.afinities_dict[TypeEau] = Pokemon.WEAKNESS_MULT

class TypeEau(Pokemon):
    def __init__(self, nom: str, hp: int, atk: int) -> None:
        super().__init__(nom, hp, atk)
        self.afinities_dict[TypeFeu] = Pokemon.RESIST_MULT
        self.afinities_dict[TypeEau] = Pokemon.RESIST_MULT
        self.afinities_dict[TypePlante] = Pokemon.WEAKNESS_MULT
