from enum import Enum
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from pokemon import Pokemon

import random


class AttackType(Enum):
    FEU = 0
    PLANTE = 1
    EAU = 2
    NORMAL = 3


class AttackTarget(Enum):
    ALLY = 0
    ENNEMY = 1


class AfflictionFunc:

    def __init__(
            self,
            on_inflict: Callable[["Pokemon", list[str]], list[str]],
            on_turn: Callable[["Pokemon", list[str]], list[str]],
            on_recover: Callable[["Pokemon", list[str]], list[str]]
    ) -> None:
        self.__on_inflict = on_inflict
        self.__on_turn = on_turn
        self.__on_recover = on_recover

    def inflict(self, pokemon: "Pokemon", diags: list[str]) -> list[str]:
        return self.__on_inflict(pokemon, diags)

    def turn_effect(self, pokemon: "Pokemon", diags: list[str]) -> list[str]:
        return self.__on_turn(pokemon, diags)

    def recover(self, pokemon: "Pokemon", diags: list[str]) -> list[str]:
        return self.__on_recover(pokemon, diags)


class Affliction:

    def __init__(self,
                 name: str,
                 effect: AfflictionFunc,
                 chances_working: int,
                 min_turns: int,
                 max_turns: int,
                 recovery_chance: int
                 ) -> None:
        self.name = name
        self.__effect = effect
        self.min_turns = min_turns
        self.max_turns = max_turns
        self.chances_working = chances_working
        self.recovery_chance = recovery_chance

    def inflict(self,
                pokemon: "Pokemon",
                combat_turn: int,
                diags: list[str]
                ) -> list[str]:
        rand = random.randint(0, 100)
        if rand < self.chances_working - pokemon.spdf:
            pokemon.add_affliction(self, combat_turn)
            return self.__effect.inflict(pokemon, diags)
        return diags

    # Fonction lancée à chaque tour pour l'affliction. Retourne des messages
    def afflict(self, pokemon, diags: list[str]) -> list[str]:
        return self.__effect.turn_effect(pokemon, diags)

    # Fonction lancée à la fin d'une affliction. Retourne des messages
    def recover(self, pokemon: "Pokemon", diags: list[str]) -> list[str]:
        return self.__effect.recover(pokemon, diags)


class PokemonAffliction(Affliction):

    def __init__(self, aff: Affliction, combat_turn: int):
        super().__init__(aff.name, aff.__effect, aff.chances_working,
                         aff.min_turns, aff.max_turns, aff.recovery_chance)
        self.combat_turn = combat_turn


class Attack:

    def __init__(self,
                 nom: str,
                 atk_type: AttackType,
                 base_pwr: int,
                 pwr_mult: int,
                 crit_chance: int = 10,
                 target: AttackTarget = AttackTarget.ENNEMY,
                 afflictions: list[Affliction] = []
                 ) -> None:
        self.nom = nom
        self.atk_type = atk_type
        self.base_pwr = base_pwr
        self.pwr_mult = pwr_mult
        self.crit_chance = crit_chance
        self.target = target
        self.afflictions = afflictions
