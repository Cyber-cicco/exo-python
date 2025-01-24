from event import Event
from ui.menu import Menu, MenuOption
from ui.character import CharacterType, Character
from ui.popup import PopUp
from pokemon import Pokemon
from enum import Enum
from gamestate import GameState
import time

class CombatTurn(Enum):
    ALLY = 0
    ENNEMY = 1

class Combat(Event):
    def __init__(self, id: str, ally:Pokemon, ennemy:Pokemon, parent:Event=None) -> None:
        super().__init__(id)
        self.ally = ally
        self.ennemy = ennemy
        self.parent = parent
        self.combat_turn = CombatTurn.ALLY
        menu = Menu(
            pos_x=0,
            pos_y=30,
        )
        self.ui = {}
        self.ui["ally"] = Character(0, 25, CharacterType.FACING_RIGHT)
        self.ui["ennemy"] = Character(20, 23, CharacterType.FACING_LEFT)
        attaquer = MenuOption(2, 1, ["attaquer"], lambda: self.attaquer(), True)
        parler = MenuOption(2, 2, ["parler"], lambda: self.parler())
        fuir = MenuOption(2, 3, ["fuir"], lambda: self.fuir())
        self.cursor_pos = 0
        self.options = [attaquer,parler, fuir]
        menu.position_on_self(attaquer)
        menu.position_on_self(parler)
        menu.position_on_self(fuir)
        self.ui["menu"] = menu

    def execute(self) -> bool:
        self.ui["ennemy"].render()
        self.ui["ally"].render()
        self.ui["menu"].render()
        if self.combat_turn == CombatTurn.ALLY:
            input = GameState.get_char()
            return self.capture_input(input)
        elif self.combat_turn == CombatTurn.ENNEMY:
            return False

    def attaquer(self) -> None:
        dmg = self.ennemy.take_damage(self.ally)
        popup = PopUp(f"{self.ennemy.nom} a subit {dmg} points de dégats.", list(self.ui.values()))
        popup.render()
        self.combat_turn = CombatTurn.ALLY

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
