from ui.element import UIElement

class HpBar(UIElement):

    def __init__(self, props:dict={}, pos_x:int=2, pos_y:int=2) -> None:
        super().__init__(pos_x, pos_y, [self.__get_line(props["hp"], props["max_hp"])], props=props)

    def refresh(self, props:dict={}):
        self.props = {**self.props, **props}
        self.ascii = [self.__get_line(self.props["hp"], self.props["max_hp"])]

    def __get_line(self, hp:int, max_hp:int) -> str:
        val = int(float(hp) / float(max_hp)) * 10
        line = f"{hp}/{max_hp} |"
        i = 0
        while i < 10:
            if i < val:
                line = line + "o"
            else:
                line = line + "-"
            i += 1

        return line + "|"

