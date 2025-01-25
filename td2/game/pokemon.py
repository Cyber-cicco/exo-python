from attack import Attack, AttackType, Affliction, PokemonAffliction
import random
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from combat import Combat


class Pokemon:
    WEAKNESS_MULT = 2.0
    RESIST_MULT = 0.5

    def __init__(self,
                 nom: str,
                 hp: int,
                 atk: int,
                 df: int,
                 spdf: int,
                 attacks: dict[str, Attack],
                 ia: Callable[["Combat", "Pokemon", "Pokemon"], list[str]]
                 ) -> None:
        self.__nom = nom
        self.__hp = hp
        self.__hp_max = hp
        self.__atk = atk
        self.__df = df
        self.__spdf = spdf
        self.affinities_dict = {}
        self.__afflictions = {}
        self.able_to_act = True
        self.__attacks = attacks
        self.ia = ia

    def add_affliction(self, affliction: Affliction, combat_turn: int) -> None:
        self.__afflictions[affliction.name] = PokemonAffliction(
            affliction, combat_turn)

    def run_afflictions(self, combat_turn: int) -> None:
        for aff in self.__afflictions.values():
            aff.afflict(self)
            rand = random.randint(0, 100)
            if ((rand < aff.recovery_chance + self.spdf and
                combat_turn - aff.combat_turn > aff.min_turns) or
                    combat_turn - aff.combat_turn >= aff.max_turns):
                self.recover_from_affliction(aff.name)

    def recover_all_afflictions(self):
        for aff in self.__afflictions.values():
            self.recover_from_affliction(aff.name)

    def recover_from_affliction(self, name: str) -> None:
        self.__afflictions[name].recover(self)

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def attacks(self) -> dict[str, Attack]:
        return self.__attacks

    @property
    def atk(self) -> int:
        return self.__atk

    @property
    def df(self) -> int:
        return self.__df

    @property
    def spdf(self) -> int:
        return self.__spdf

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, amount: int):
        if amount < 0:
            amount = 0
        self.__hp = amount

    @property
    def hp_max(self) -> int:
        return self.__hp_max

    def is_dead(self) -> bool:
        return self.hp == 0

    def take_damage(self,
                    attacker: "Pokemon",
                    attack: Attack,
                    combat_turn: int,
                    diags: list[str]
                    ) -> list[str]:
        # Gestion des coups efficaces
        multiplier = 1
        if self.affinities_dict.get(attack.atk_type) is not None:
            multiplier = self.affinities_dict[attack.atk_type]
            if multiplier > 1:
                diags.append("C'est super efficace !")
            elif multiplier < 1:
                diags.append("C'est peu efficace")

        # Gestion des coups critiques
        rand = random.randint(1, 100)
        if rand < attack.crit_chance:
            multiplier *= 1.7
            diags.append("Coup critique !")

        # Gestion des dégâts supplémentaires en fonction de la force
        max_add_power = int((attack.pwr_mult / 100) * attacker.atk)
        add_power = random.randint(int(max_add_power / 3), max_add_power)
        dmg = int((attack.base_pwr + add_power) * multiplier - self.__df)

        if dmg < 0:
            diags.append(f"{self.nom} n'a pas subit de dégâts !")
            return diags
        res = self.hp - dmg
        self.hp = res
        return diags

    def attaquer(self,
                 target: "Pokemon",
                 attack: Attack,
                 combat_turn: int,
                 diags: list[str]
                 ) -> list[str]:
        return target.take_damage(self, attack, combat_turn, diags)

    def __str__(self) -> str:
        return f"{self.nom} est un pokemon normal. Caractéristiques : \n HP: {self.hp}/{self.hp_max}\n Atk : {self.atk}"


class TypePlante(Pokemon):
    def __init__(self,
                 nom: str,
                 hp: int,
                 atk: int,
                 df: int,
                 spdf: int,
                 attacks: dict[str, Attack],
                 ia: Callable[["Combat", Pokemon, Pokemon], list[str]]
                 ) -> None:
        super().__init__(nom, hp, atk, df, spdf, attacks, ia)
        self.affinities_dict[AttackType.FEU] = Pokemon.WEAKNESS_MULT
        self.affinities_dict[AttackType.PLANTE] = Pokemon.RESIST_MULT
        self.affinities_dict[AttackType.EAU] = Pokemon.RESIST_MULT


class TypeFeu(Pokemon):
    def __init__(self,
                 nom: str,
                 hp: int,
                 atk: int,
                 df: int,
                 spdf: int,
                 attacks: dict[str, Attack],
                 ia: Callable[["Combat", Pokemon, Pokemon], list[str]]
                 ) -> None:
        super().__init__(nom, hp, atk, df, spdf, attacks, ia)
        self.affinities_dict[AttackType.FEU] = Pokemon.RESIST_MULT
        self.affinities_dict[AttackType.PLANTE] = Pokemon.RESIST_MULT
        self.affinities_dict[AttackType.EAU] = Pokemon.WEAKNESS_MULT


class TypeEau(Pokemon):
    def __init__(self,
                 nom: str,
                 hp: int,
                 atk: int,
                 df: int,
                 spdf: int,
                 attacks: dict[str, Attack],
                 ia: Callable[["Combat", Pokemon, Pokemon], list[str]]
                 ) -> None:
        super().__init__(nom, hp, atk, df, spdf, attacks, ia)
        self.affinities_dict[AttackType.FEU] = Pokemon.RESIST_MULT
        self.affinities_dict[AttackType.EAU] = Pokemon.RESIST_MULT
        self.affinities_dict[AttackType.PLANTE] = Pokemon.WEAKNESS_MULT
