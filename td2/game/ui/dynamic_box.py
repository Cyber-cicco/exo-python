from ui.element import UIElement
from typing import List

class DynamicBox(UIElement):

    TOP = ["/---------------------------\\"]
    BOT = ["\\---------------------------/"]

    def __init__(self,content:List[str], pos_x:int, pos_y:int, children: List[UIElement]=[]):
        ascii = self.get_ascii(content)
        super().__init__(pos_x, pos_y, ascii, children=children)

    def get_ascii(self, content:str) -> List[str]:
        ascii = []
        for line in self.TOP:
            ascii.append(line)
        top_len = len(self.TOP[0])
        for line in content:
            while len(line) > top_len  - 2 :
                new_line = "|" + line[:top_len - 2] + "|"
                line = line[top_len - 3:]
                ascii.append(new_line)
            padding_left = top_len - len(line) - 2
            line = "|" + line + " " * padding_left + "|"
            ascii.append(line)
        for line in self.BOT:
            ascii.append(line)
        return ascii
