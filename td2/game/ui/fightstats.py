from ui.element import UIElement

class FightStats(UIElement):

    STAT_CONTAINER = [
        ".---------------------.",
        "|                     |",
        "|                     |",
        "°---------------------°",
    ]

    def __init__(self, pos_x:int, pos_y:int, children:list[UIElement]):
        super().__init__(pos_x, pos_y, self.STAT_CONTAINER, children=children)
