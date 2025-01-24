from ui.element import UIElement
from typing import List

class FightStats(UIElement):

    STAT_CONTAINER = [
        ".---------------------.",
        "|                     |",
        "|                     |",
        "°---------------------°",
    ]

    def __init__(self, pos_x:int, pos_y:int, children:List[UIElement]):
        super().__init__(pos_x, pos_y, self.STAT_CONTAINER, children=children)
