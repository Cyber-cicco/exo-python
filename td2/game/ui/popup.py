from ui.element import UIElement
from ui.dynamic_box import DynamicBox
import time


class PopUp(DynamicBox):

    def __init__(self, content: str, rerenders: list[UIElement], pos_x: int = 10, pos_y: int = 13, pop_up_time: float = 2):
        self.rerenders = rerenders
        self.pop_up_time = pop_up_time
        super().__init__([content], pos_x, pos_y)

    def render(self, props: dict = {}, force_render: bool = False):
        for el in self.rerenders:
            el.refresh()
        joint_list = list("".join(line) for line in self.ascii)
        for index, joint_text in enumerate(joint_list):
            print(
                f"\033[{self.pos_y + index};{self.pos_x}H{joint_text}", end="", flush=True)
        time.sleep(self.pop_up_time)
        self.hide()
