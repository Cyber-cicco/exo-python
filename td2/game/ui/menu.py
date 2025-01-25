from ui.element import UIElement
from ui.dynamic_box import DynamicBox
from typing import Callable

class MenuOption(UIElement):
    def __init__(self, pos_x: int, pos_y: int, ascii: list[str], execute_option:Callable[[], None], has_cursor: bool = False) -> None:
        super().__init__(pos_x, pos_y, ascii)
        self.has_cursor = has_cursor
        self.execute_option = execute_option
        if self.has_cursor:
            # Prepend '>' to the first line (list of characters)
            self.ascii[0] = ['>'] + self.ascii[0]

    def set_cursor(self, has: bool) -> None:
        if self.has_cursor and not has:
            # Remove the '>' from the first line
            self.ascii[0] = self.ascii[0][1:]  # Slice from index 1 onward
            self.ascii[0].append(" ")
        elif not self.has_cursor and has:
            # Add '>' to the beginning of the first line
            self.ascii[0] = ['>'] + self.ascii[0]
        self.has_cursor = has


class Menu(DynamicBox):

    def __init__(self, pos_x:int, pos_y:int, options:list[MenuOption]):
        ascii = []
        for option in options:
            ascii.append(''.join(option.ascii[0]))
        super().__init__(ascii, pos_x, pos_y, options)
        


