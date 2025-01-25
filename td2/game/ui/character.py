from ui.element import UIElement
from enum import Enum


class CharacterType(Enum):
    FACING_RIGHT = 0
    FACING_LEFT = 1


class Character(UIElement):

    CHARACTERS = {
        CharacterType.FACING_RIGHT: [
            " :^) ",
            "  |  ",
            "-----",
            "  |  ",
            " / \\ ",
        ],
        CharacterType.FACING_LEFT: [
            " (^: ",
            "  |  ",
            "-----",
            "  |  ",
            " / \\ ",
        ]
    }

    def __init__(self, pos_x: int, pos_y: int, char_type: CharacterType):
        super().__init__(pos_x, pos_y, Character.CHARACTERS[char_type])
        self.char_type = char_type

    def refresh(self, props: dict = {}):
        self.ascii = [list(line)
                      for line in Character.CHARACTERS[self.char_type]]
