from gamestate import GameState
from combat import Combat
from pokemon import TypePlante, TypeFeu, TypeEau

if __name__ == "__main__":
    game = GameState([Combat("main", TypeFeu("Dracofeu", 45, 17), TypePlante("Bulbizarre", 50, 15))])
    game.main_loop()
