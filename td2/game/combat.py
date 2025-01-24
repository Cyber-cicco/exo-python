from event import Event
from ui.element import UIElement
from ui.menu import Menu, MenuOption
from ui.footer import Footer
from ui.character import CharacterType, Character
from ui.popup import PopUp
from ui.fightstats import FightStats
from ui.hp_bar import HpBar
from pokemon import Pokemon
from enum import Enum
from gamestate import GameState
import time

class CombatTurn(Enum):
    ALLY = 0
    ENNEMY = 1
    END = 2

class Combat(Event):
    

    def __init__(self, id: str, ally:Pokemon, ennemy:Pokemon, parent:Event=None) -> None:
        super().__init__(id)

        # Assignation basique
        self.ally = ally
        self.ennemy = ennemy
        self.parent = parent
        self.combat_turn = CombatTurn.ALLY

        menu = Menu(
            pos_x=0,
            pos_y=30,
        )
        self.ui = {}
        self.ui["footer"] = Footer()
        self.ui["ally"] = Character(0, 25, CharacterType.FACING_RIGHT)
        self.ui["ennemy"] = Character(20, 23, CharacterType.FACING_LEFT)

        ennemy_hp = HpBar(self.ennemy_props) 
        ally_hp = HpBar(self.ally_props) 

        ally_name = UIElement(1, 1, [self.ally.nom])
        ennemy_name = UIElement(1, 1, [self.ennemy.nom])

        self.ui["ally_menu"] = FightStats(0, 15, [ally_name, ally_hp])
        self.ui["ennemy_menu"] = FightStats(25, 15, [ennemy_name, ennemy_hp])

        attaquer = MenuOption(2, 1, ["attaquer"], lambda: self.attaquer(), True)
        parler = MenuOption(2, 2, ["parler"], lambda: self.parler())
        fuir = MenuOption(2, 3, ["fuir"], lambda: self.fuir())
        self.cursor_pos = 0
        self.options = [attaquer,parler, fuir]
        menu.position_on_self(attaquer)
        menu.position_on_self(parler)
        menu.position_on_self(fuir)
        self.ui["menu"] = menu

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
        self.ui["menu"].render()
        self.ui["footer"].render(True)

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

            PopUp(f"Autour de l'ennemi d'attaquer !", list(self.ui.values()), pop_up_time=1.5).render()
            PopUp(f"{self.ennemy.nom} utilise attaque !", list(self.ui.values()), pop_up_time=1.5).render()
            dmg = self.ally.take_damage(self.ennemy)
            PopUp(f"{self.ally.nom} a subit {dmg} points de dégats.", list(self.ui.values())).render()
            self.ui["ally_menu"].refresh(self.ally_props)
            self.combat_turn = CombatTurn.ALLY
            return False


    def attaquer(self) -> None:
        dmg = self.ennemy.take_damage(self.ally)
        PopUp(f"{self.ally.nom} utilise attaque !", list(self.ui.values()), pop_up_time=1.5).render()
        PopUp(f"{self.ennemy.nom} a subit {dmg} points de dégats.", list(self.ui.values())).render()
        self.ui["ennemy_menu"].refresh(self.ennemy_props)
        self.combat_turn = CombatTurn.ENNEMY


    def parler(self) -> None:
        print("parler")
        time.sleep(1)


    def fuir(self) -> None:
        print("fuir")
        time.sleep(1)


    def capture_input(self, input:str) -> bool:
        if input == "j" or input == "[A":
            self.options[self.cursor_pos].set_cursor(False)
            self.cursor_pos = (self.cursor_pos + 1) % len(self.options)
            self.options[self.cursor_pos].set_cursor(True)
            self.__refresh_menu()
            return False
        elif input == "k":
            self.options[self.cursor_pos].set_cursor(False)
            self.cursor_pos = (self.cursor_pos - 1) % len(self.options)
            self.options[self.cursor_pos].set_cursor(True)
            self.__refresh_menu()
            return False
        elif input == "\n" or input == "\r":
            self.options[self.cursor_pos].execute_option()
            return False
        return input == "q"


    # Pk les options sont dans le combat et pas le menu ?
    def __refresh_menu(self) -> None:
        self.ui["menu"].refresh()
        for option in self.options:
            self.ui["menu"].position_on_self(option)
