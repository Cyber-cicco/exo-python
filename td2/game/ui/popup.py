from ui.element import UIElement
from typing import List
import time

class PopUp(UIElement):


    TOP = "/---------------------------\\"
    BOT = "\\---------------------------/"



    def __init__(self,content:str, rerenders: List[UIElement], pos_x:int=10, pos_y:int=10, pop_up_time=2):
        self.rerenders = rerenders
        self.pop_up_time = pop_up_time
        ascii = [self.TOP]
        while len(content) > len(self.TOP) - 2 :
            new_line = "|" + content[:len(PopUp.TOP) - 2] + "|"
            content = content[len(self.TOP) - 3:]
            ascii.append(new_line)
        padding_left = len(self.TOP) - len(content) - 2
        content = "|" + content + " " * padding_left + "|"
        ascii.append(content)
        ascii.append(self.BOT)
        super().__init__(pos_x, pos_y, ascii)

    def render(self):
        for el in self.rerenders:
            el.refresh()
        joint_list = list("".join(line) for line in self.ascii)
        for index, joint_text in enumerate(joint_list):
            print(f"\033[{self.pos_y + index};{self.pos_x}H{joint_text}", end="", flush=True)
        time.sleep(self.pop_up_time)
        for index, joint_text in enumerate(joint_list):
            print(f"\033[{self.pos_y + index};{self.pos_x}H{len(joint_text) * ' '}", end="", flush=True)


