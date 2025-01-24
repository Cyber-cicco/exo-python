from event import Event
from typing import List
import os
import tty
import sys
import termios
import time

class GameState:
    def __init__(self, events: List[Event]) -> None:
        self.events_dict = {}
        self.__quit = False
        if os.name == "nt":
            raise Exception("Windows is not supported.")
        elif os.name == "posix":
            self.clear = lambda: os.system("clear")
        for e in events:
            self.events_dict[e.id] = e

    def main_loop(self):
        while not self.__quit:
            self.clear()
            main_event = self.events_dict["main"]
            main_event.execute()
            char = GameState.get_char()
            if char == "q":
                self.__quit = True
            main_event.capture_input(char)


    def get_char() -> str:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)  # Read a single character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char
