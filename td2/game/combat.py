import time
from event import Event
from ui.element import UIElement
from ui.menu import Menu, MenuOption
from ui.footer import Footer
from ui.character import CharacterType, Character
from ui.popup import PopUp
from ui.dialog import DialogRight
from ui.fightstats import FightStats
from ui.hp_bar import HpBar
from pokemon import Pokemon
from enum import Enum
from gamestate import GameState

from typing import Union
import random

class CombatTurn(Enum):
    ALLY = 0
    ENNEMY = 1
    FLEE = 2

class Combat(Event):
    

    def __init__(self, id: str, ally:Pokemon, ennemy:Pokemon, parent:Union[Event, None]=None) -> None:
        super().__init__(id)

        # Assignation basique
        self.ally = ally
        self.ennemy = ennemy
        self.parent = parent
        self.combat_turn = CombatTurn.ALLY
        self.cursor_pos = 0
        self.turn_count = 1

        self.ui:dict[str, UIElement] = {}
        self.ui["footer"] = Footer()
        self.ui["ally"] = Character(0, 25, CharacterType.FACING_RIGHT)
        self.ui["ennemy"] = Character(20, 23, CharacterType.FACING_LEFT)

        ally_hp = HpBar(self.ally_props) 
        ally_name = UIElement(1, 1, [self.ally.nom])
        self.ui["ally_menu"] = FightStats(0, 15, [ally_name, ally_hp])

        ennemy_hp = HpBar(self.ennemy_props) 
        ennemy_name = UIElement(1, 1, [self.ennemy.nom])
        self.ui["ennemy_menu"] = FightStats(25, 15, [ennemy_name, ennemy_hp])

        self.main_menu_options:list[MenuOption] = [
            MenuOption(1, 1, ["attaquer"], lambda: self.show_attack_menu(), True),
            MenuOption(1, 2, ["parler"], lambda: self.parler()),
            MenuOption(1, 3, ["objet"], lambda: self.objets()),
            MenuOption(1, 4, ["fuir"], lambda: self.fuir()),
        ]

        self.ui["menu"] = Menu(
            pos_x=0,
            pos_y=30,
            options=self.main_menu_options,
        )

        self.attack_options:list[MenuOption] = []
        for i, nom in enumerate(self.ally.attacks.keys()):
            self.attack_options.append(
                MenuOption(1, i+1, [nom], lambda x=nom: self.attaquer(x))
            )
        self.ui["menu_attack"] = Menu(
            pos_x=0,
            pos_y=30,
            options=self.attack_options,
        )
        self.options = self.main_menu_options

        self.current_menu = "menu"

    @property
    def ally_props(self) -> dict:
        return {"hp": self.ally.hp, "max_hp": self.ally.hp_max}

    @property
    def ennemy_props(self) -> dict:
        return {"hp": self.ennemy.hp, "max_hp": self.ennemy.hp_max}


    def execute(self) -> bool:
        self.ui["ennemy"].render()
        self.ui["ally"].render()
        self.ui["ennemy_menu"].render(self.ennemy_props)
        self.ui["ally_menu"].render(self.ally_props)
        self.ui["footer"].render()
        self.ui[self.current_menu].render()

        if self.ally.hp == 0:
            PopUp("Vous avez échoué...", list(self.ui.values()), pop_up_time=1.5).render()
            return True

        if self.ennemy.hp == 0:
            PopUp("Vous avez triomphé !", list(self.ui.values()), pop_up_time=1.5).render()
            return True

        if self.combat_turn == CombatTurn.ALLY:

            input = GameState.get_char()
            return self.capture_input(input)

        elif self.combat_turn == CombatTurn.ENNEMY:

            PopUp(f"Au tour de l'ennemi d'attaquer !", list(self.ui.values()), pop_up_time=1.5).render()
            diags = self.ennemy.ia(self, self.ennemy, self.ally)
            for diag in diags:
                PopUp(diag, list(self.ui.values())).render()
            self.ui["ally_menu"].refresh(self.ally_props)
            self.combat_turn = CombatTurn.ALLY
            self.__refresh_turn()
            return False

        elif self.combat_turn.FLEE: 
            return True

        return False

    def __refresh_turn(self):
        self.current_menu = "menu"
        self.options = self.main_menu_options
        self.turn_count += 1

    def show_attack_menu(self) -> None:
        self.ui["menu"].hide()
        self.cursor_pos = 0
        self.current_menu = "menu_attack"
        self.options = self.attack_options
        self.__refresh_cursor()


    def attaquer(self, attack_name:str) -> None:
        attack = self.ally.attacks[attack_name]
        PopUp(f"{self.ally.nom} utilise {attack_name} !", list(self.ui.values()), pop_up_time=1.5).render()
        diags = []
        diags = self.ally.attaquer(self.ennemy, attack, self.turn_count, diags)
        for diag in diags:
            PopUp(diag, list(self.ui.values())).render()
        self.ui["ennemy_menu"].refresh(self.ennemy_props)
        self.combat_turn = CombatTurn.ENNEMY
        self.cursor_pos = 0


    def parler(self) -> None:
        DialogRight(["Bonjour", "J'aime le boulgour"], list(self.ui.values()), 2, 19).render()

    def objets(self):
        PopUp("Vous n'avez pas d'objet ! ", list(self.ui.values()), pop_up_time=1.5).render()

    def fuir(self) -> None:
        PopUp(f"{self.ally.nom} s'enfuit comme un gros lâche !", list(self.ui.values()), pop_up_time=3).render()
        rand = random.randint(0, 100)
        print(rand)
        if rand <= 50:
            PopUp(f"Mais sa lacheté ne paie pas : l'ennemi bloque le passage !", list(self.ui.values()), pop_up_time=2).render()
            self.combat_turn = CombatTurn.ENNEMY
        else : 
            self.combat_turn = CombatTurn.FLEE

    def __refresh_cursor(self):
        for i, option in enumerate(self.options):
            if self.cursor_pos == i:
                option.set_cursor(True)
            else:
                option.set_cursor(False)


    def capture_input(self, input:str) -> bool:
        if input == "j" or input == "[A":
            self.cursor_pos = (self.cursor_pos + 1) % len(self.options)
            self.__refresh_cursor()
            self.__refresh_menu()
            return False
        elif input == "k":
            self.cursor_pos = (self.cursor_pos - 1) % len(self.options)
            self.__refresh_cursor()
            self.__refresh_menu()
            return False
        elif input == "\n" or input == "\r":
            self.options[self.cursor_pos].execute_option()
            return False
        return input == "q"


    def __refresh_menu(self) -> None:
        self.ui[self.current_menu].refresh()
