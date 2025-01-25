class Event:
    def __init__(self, id: str, parent=None) -> None:
        self.id = id
        self.parent = parent

    def execute(self) -> bool:
        return True

    def capture_input(self, input:str) -> bool:
        return input == "q"

