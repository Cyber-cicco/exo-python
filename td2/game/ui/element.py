from typing import Iterable


class UIElement:

    def __init__(self,
                 pos_x: int,
                 pos_y: int,
                 ascii: list[str],
                 children: Iterable["UIElement"] = [],
                 props: dict = {}
                 ) -> None:
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.ascii = [list(line) for line in ascii]
        self.children = children
        self.props = props
        self.__should_render = True

    def position_on_self(self, ui) -> None:
        if ui.pos_x + len(ui.ascii[0]) > len(self.ascii[0]):
            raise Exception("UI element is wider than the container.")
        if ui.pos_y + len(ui.ascii) > len(self.ascii):
            raise Exception("UI element is taller than the container.")

        for i, ascii_line in enumerate(ui.ascii):
            start = ui.pos_x
            end = start + len(ascii_line)
            self.ascii[i + ui.pos_y][start:end] = ascii_line
        self.__should_render = True

    def render(self, props: dict = {}, force_render: bool = False) -> None:
        if self.__should_render or force_render:
            for child in self.children:
                self.position_on_self(child)
            joint_list = list("".join(line) for line in self.ascii)
            for index, joint_text in enumerate(joint_list):
                print(
                    f"\033[{self.pos_y + index};{self.pos_x}H{joint_text}", end="", flush=True)
            self.__should_render = False

    def refresh(self, props: dict = {}) -> None:
        self.props = {**self.props, **props}
        for child in self.children:
            child.refresh(self.props)
            self.position_on_self(child)
        self.__should_render = True

    def hide(self):
        joint_list = list("".join(line) for line in self.ascii)
        for index, joint_text in enumerate(joint_list):
            print(
                f"\033[{self.pos_y + index};{self.pos_x}H{len(joint_text) * ' '}", end="", flush=True)
