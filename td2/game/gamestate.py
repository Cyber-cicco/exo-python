from event import Event
from typing import Iterable
import os
import tty
import sys
import termios


class GameState:

    def __init__(self, events: Iterable[Event]) -> None:
        self.events_dict = {}
        self.__quit = False
        if os.name == "nt":
            raise Exception(
                "Wtf are you doing on windows wtf bro pls stop frfr at least use WSL idk bro"
            )
        elif os.name == "posix":
            self.clear = lambda: os.system("clear")
        for e in events:
            self.events_dict[e.id] = e

    def main_loop(self):
        self.clear()
        while not self.__quit:
            main_event = self.events_dict["main"]
            self.__quit = main_event.execute()

    def get_char() -> str:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)  # Read a single character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char
