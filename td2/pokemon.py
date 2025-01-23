import os
from typing import List

class Pokemon:

    WEAKNESS_MULT = 2.0
    RESIST_MULT = 0.5

    def __init__(self, nom:str, hp:int, atk:int) -> None:
        self.__nom = nom
        self.__hp = hp
        self.__hp_max = hp
        self.__atk = atk
        self.afinities_dict = {}

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def atk(self) -> int:
        return self.__atk

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def hp_max(self) -> int:
        return self.__hp_max

    def is_dead(self) -> bool:
        return self.hp == 0

    def take_damage(self, atk:int, pokemon:Pokemon) -> None:
        mutlitplier = 1
        if self.afinities_dict.get(type(pokemon)) is not None :
            mutlitplier = self.afinities_dict[type(pokemon)]
        res == self.hp - atk * mutlitplier
        if res < 0:
            self.__hp = 0
            return
        self.__hp = res

    def attaquer(self, pokemon:Pokemon) -> None:
        pokemon.take_damage(self.atk)

    def __str__(self) -> str:
        return f"{self.nom} est un pokemon normal. Caractéristiques : \n HP: {self.hp}/{self.hp_max}\n Atk : {self.atk}"

class TypePlante(Pokemon):

    def __init__(self, nom:str, hp:int, atk:int) -> None:
        super().__init__(nom, hp, atk)
        self.afinities_dict[TypeFeu] = Pokemon.WEAKNESS_MULT 
        self.afinities_dict[TypePlante] = Pokemon.RESIST_MULT 
        self.afinities_dict[TypeEau] = Pokemon.RESIST_MULT 

class TypeFeu(Pokemon):

    def __init__(self, nom:str, hp:int, atk:int) -> None:
        super().__init__(nom, hp, atk)
        self.afinities_dict[TypeFeu] = Pokemon.RESIST_MULT 
        self.afinities_dict[TypePlante] = Pokemon.RESIST_MULT 
        self.afinities_dict[TypeEau] = Pokemon.WEAKNESS_MULT 

class TypeEau(Pokemon):

    def __init__(self, nom:str, hp:int, atk:int) -> None:
        super().__init__(nom, hp, atk)
        self.afinities_dict[TypeFeu] = Pokemon.RESIST_MULT 
        self.afinities_dict[TypeEau] = Pokemon.RESIST_MULT 
        self.afinities_dict[TypePlante] = Pokemon.WEAKNESS_MULT 

class GameState:
    
    def __init__(self, events:List[Event]) -> None:
        self.events_dict = {}
        if os.name == 'nt':
            raise Exception("Wtf are you doing on windows stop please")
        elif os.name == 'posix':
            self.clear = lambda: os.system('clear')
        for e in events:
            self.events_dict[e.id] = e
        
    def main_loop(self):
        self.clear()
        self.events_dict["main"].execute(self)

class Event:
    
    def __init__(self, id:str, game_state:GameState, parent:Event=None) -> None:
        self.id = id
        self.parent

    def execute(self) -> None:
        pass

    def render(self) -> None:
        pass

class Combat(Event):

    def __init__(self, id:str) -> None:
        super().__init__(id)
        self.menu = UIElement(
            pos_x=0,
            pos_y=30,
            ascii=[
                "/---------------------------\\",
                "|                           |",
                "|                           |",
                "\\---------------------------/",
            ])
        attaquer = UIElement(2, 2, ["attaquer"])
        fuir = UIElement(2, 2, ["fuir"])
        self.menu.position_on_self(pos_x, pos_y, ui)


class UIElement:

    def __init__(self, pos_x:int, pos_y:int, ascii:List[str]) -> None:
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.ascii = ascii

    def position_on_self(self, ui:UIElement) -> None:
        if pos_x + len(ui.ascii[0]) > len(self.ascii[0]):
            raise Exception("impossible state in UI : ui larger than container")
        if pos_y + len(ui.ascii) > len(self.ascii) :
            raise Exception("impossible state in UI : ui larger than container")

        i = 0
        for ascii_line in ui.ascii:
            self.ascii[i + ui.pos_y][pos_x:len(ascii_line)] = ascii_line
            i += 1


