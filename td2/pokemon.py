import os
from typing import List
import tty
import sys
import termios
import time


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

    def take_damage(self, atk: int, pokemon) -> None:
        multiplier = 1
        if self.afinities_dict.get(type(pokemon)) is not None:
            multiplier = self.afinities_dict[type(pokemon)]
        res = self.hp - atk * multiplier  # Fixed assignment
        if res < 0:
            self.__hp = 0
        else:
            self.__hp = res

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

class Event:
    def __init__(self, id: str, parent=None) -> None:
        self.id = id
        self.parent = parent

    def execute(self) -> None:
        pass

    def capture_input(self, input:str) -> None:
        pass

class Combat(Event):
    def __init__(self, id: str, ally:Pokemon, ennemy:Pokemon) -> None:
        super().__init__(id)
        self.ally = ally
        self.ennemy = ennemy
        self.menu = UIElement(
            pos_x=0,
            pos_y=30,
            ascii=[
                "/---------------------------\\",
                "|                           |",
                "|                           |",
                "\\---------------------------/",
            ],
        )
        attaquer = MenuOption(2, 1, ["attaquer"], True)
        fuir = MenuOption(2, 2, ["fuir"])
        self.cursor_pos = 0
        self.options = [attaquer, fuir]
        self.menu.position_on_self(attaquer)
        self.menu.position_on_self(fuir)

    def execute(self):
        self.menu.render()

    def capture_input(self, input:str) -> None:
        if input == "j":
            self.options[self.cursor_pos].set_cursor(False)
            self.cursor_pos = (self.cursor_pos + 1) % len(self.options)
            self.options[self.cursor_pos].set_cursor(True)
            self.__refresh_menu()
        if input == "k":
            self.options[self.cursor_pos].set_cursor(False)
            self.cursor_pos = (self.cursor_pos - 1) % len(self.options)
            self.options[self.cursor_pos].set_cursor(True)
            self.__refresh_menu()

    def __refresh_menu(self) -> None:
        self.menu.refresh()
        for option in self.options:
            self.menu.position_on_self(option)



class UIElement:
    def __init__(self, pos_x: int, pos_y: int, ascii: List[str]) -> None:
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.ascii = [list(line) for line in ascii]
        self.__initial_state = list(self.ascii)

    def position_on_self(self, ui) -> None:
        if ui.pos_x + len(ui.ascii[0]) > len(self.ascii[0]):
            raise Exception("UI element is wider than the container.")
        if ui.pos_y + len(ui.ascii) > len(self.ascii):
            raise Exception("UI element is taller than the container.")

        for i, ascii_line in enumerate(ui.ascii):
            start = ui.pos_x
            end = start + len(ascii_line)
            self.ascii[i + ui.pos_y][start:end] = ascii_line

    def render(self) -> None:
        joint_text = "\n".join("".join(line) for line in self.ascii)
        print(f"\033[{self.pos_y};{self.pos_x}H{joint_text}", end="", flush=True)

    def refresh(self) -> None:
        self.ascii = self.initial_state

        
    @property
    def initial_state(self) -> List[str]:
        return self.__initial_state


class MenuOption(UIElement):
    def __init__(self, pos_x: int, pos_y: int, ascii: List[str], has_cursor: bool = False) -> None:
        super().__init__(pos_x, pos_y, ascii)
        self.has_cursor = has_cursor
        if self.has_cursor:
            # Prepend '>' to the first line (list of characters)
            self.ascii[0] = ['>'] + self.ascii[0]

    def set_cursor(self, has: bool) -> None:
        if self.has_cursor and not has:
            # Remove the '>' from the first line
            self.ascii[0] = self.ascii[0][1:]  # Slice from index 1 onward
        elif not self.has_cursor and has:
            # Add '>' to the beginning of the first line
            self.ascii[0] = ['>'] + self.ascii[0]
        self.has_cursor = has
        

class GameState:
    def __init__(self, events: List[Event]) -> None:
        self.events_dict = {}
        self.__quit = False
        if os.name == "nt":
            raise Exception("Windows is not supported.")
        elif os.name == "posix":
            self.clear = lambda: os.system("clear")
        for e in events:
            self.events_dict[e.id] = e

    def main_loop(self):
        while not self.__quit:
            self.clear()
            main_event = self.events_dict["main"]
            main_event.execute()
            char = GameState.get_char()
            if char == "q":
                self.__quit = True
            main_event.capture_input(char)


    def get_char() -> str:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)  # Read a single character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char

if __name__ == "__main__":
    game = GameState([Combat("main", TypeFeu("Dracofeu", 45, 17), TypePlante("Bulbizarre", 50, 15))])
    game.main_loop()
