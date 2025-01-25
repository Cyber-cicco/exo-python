from ui.element import UIElement

class Footer(UIElement):

    FOOTER = [
                "/-----------------------------------------\\",
                "| h: curseur vers le haut                 |",
                "| j: curseur vers le bas                  |",
                "| Enter: choisir une option               |",
                "| q: quitter                              |",
                "\\-----------------------------------------/",
            ]

    def __init__(self, pos_x:int=0, pos_y:int=37):
        super().__init__(pos_x, pos_y, self.FOOTER)
        
    def refresh(self, props:dict={}):
        self.ascii = [list(line) for line in self.FOOTER]
