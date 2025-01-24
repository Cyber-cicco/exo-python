from event import Event
from ui.menu import Menu, MenuOption
from ui.character import CharacterType, Character
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
        self.menu = Menu(
            pos_x=0,
            pos_y=30,
        )
        self.ally = Character(0, 25, CharacterType.FACING_RIGHT)
        self.ennemy = Character(20, 23, CharacterType.FACING_LEFT)
        attaquer = MenuOption(2, 1, ["attaquer"], Combat.attaquer, True)
        parler = MenuOption(2, 2, ["parler"], Combat.parler)
        fuir = MenuOption(2, 3, ["fuir"], Combat.fuir)
        self.cursor_pos = 0
        self.options = [attaquer,parler, fuir]
        self.menu.position_on_self(attaquer)
        self.menu.position_on_self(parler)
        self.menu.position_on_self(fuir)

    def execute(self) -> None:
        self.ennemy.render()
        self.ally.render()
        self.menu.render()

    def attaquer() -> None:
        self.ennemy.take_damage(self.ally)
        self.combat_turn = CombatTurn.ENNEMY
        time.sleep(1)

    def parler() -> None:
        print("parler")
        time.sleep(1)

    def fuir() -> None:
        print("fuir")
        time.sleep(1)

    def capture_input(self, input:str) -> None:
        if self.combat_turn == CombatTurn.ALLY:
            if input == "j" or input == "[A":
                self.options[self.cursor_pos].set_cursor(False)
                self.cursor_pos = (self.cursor_pos + 1) % len(self.options)
                self.options[self.cursor_pos].set_cursor(True)
                self.__refresh_menu()
            if input == "k":
                self.options[self.cursor_pos].set_cursor(False)
                self.cursor_pos = (self.cursor_pos - 1) % len(self.options)
                self.options[self.cursor_pos].set_cursor(True)
                self.__refresh_menu()
            if input == "\n" or input == "\r":
                self.options[self.cursor_pos].execute_option()

    def __refresh_menu(self) -> None:
        self.menu.refresh()
        for option in self.options:
            self.menu.position_on_self(option)
