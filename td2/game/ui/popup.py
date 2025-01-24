from ui.element import UIElement

class PopUp(UIElement):

    def __init__(self, pos_x:int, pos_y:int, ascii:List[str]):
        super().__init__(pos_x, pos_y, ascii)
