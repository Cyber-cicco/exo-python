from ui.element import UIElement
from typing import List

class Menu(UIElement):

    MENU = [
                "/---------------------------\\",
                "|                           |",
                "|                           |",
                "\\---------------------------/",
            ]

    def __init__(self, pos_x:int, pos_y:int):
        super().__init__(pos_x, pos_y, Menu.MENU)
        
    def refresh(self):
        self.ascii = [list(line) for line in Menu.MENU]



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
