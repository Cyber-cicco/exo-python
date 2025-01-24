from typing import List
import time

class UIElement:
    def __init__(self, pos_x: int, pos_y: int, ascii: List[str]) -> None:
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.ascii = [list(line) for line in ascii]

    def position_on_self(self, ui) -> None:
        if ui.pos_x + len(ui.ascii[0]) > len(self.ascii[0]):
            raise Exception("UI element is wider than the container.")
        if ui.pos_y + len(ui.ascii) > len(self.ascii):
            raise Exception("UI element is taller than the container.")

        for i, ascii_line in enumerate(ui.ascii):
            start = ui.pos_x
            end = start + len(ascii_line)
            print(self.ascii[i + ui.pos_y])
            print(ascii_line)
            self.ascii[i + ui.pos_y][start:end] = ''.join(ascii_line)

    def render(self) -> None:
        joint_text = "\n".join("".join(line) for line in self.ascii)
        print(f"\033[{self.pos_y};{self.pos_x}H{joint_text}", end="", flush=True)

    def refresh(self) -> None:
        pass

