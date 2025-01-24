from event import Event
from ui.menu import Menu, MenuOption
from pokemon import Pokemon

class Combat(Event):
    def __init__(self, id: str, ally:Pokemon, ennemy:Pokemon) -> None:
        super().__init__(id)
        self.ally = ally
        self.ennemy = ennemy
        self.menu = Menu(
            pos_x=0,
            pos_y=30,
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
