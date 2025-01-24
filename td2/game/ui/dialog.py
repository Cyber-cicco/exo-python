from ui.popup import PopUp
from ui.element import UIElement
from gamestate import GameState
from typing import List

class DialogRight(PopUp):

    TOP = [
        "-----------------------------"
    ]
    BOT = [
        "\\------------------- -------/",
        "                    V        ",
    ]
    def __init__(self, contents:List[str], rerenders:List[UIElement], pos_x:int, pos_y:int):
        super().__init__(contents[0], rerenders, pos_x, pos_y)
        self.contents = contents

    def render(self):
        for content in self.contents:
            self.ascii = self.get_ascii([content])
            for el in self.rerenders:
                el.refresh()
            joint_list = list("".join(line) for line in self.ascii)
            for index, joint_text in enumerate(joint_list):
                print(f"\033[{self.pos_y + index};{self.pos_x}H{joint_text}", end="", flush=True)
            char = ""
            while char != "\n" and char != "\r":
                char = GameState.get_char()
            for index, joint_text in enumerate(joint_list):
                print(f"\033[{self.pos_y + index};{self.pos_x}H{len(joint_text) * ' '}", end="", flush=True)

