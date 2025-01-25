from gamestate import GameState
from combat import Combat
from data.pokemons import POKEMONS

if __name__ == "__main__":
    game = GameState(
        [
            Combat(
                "main",
                POKEMONS["Salamèche"],
                POKEMONS["Bulbizarre"],
            )
        ]
    )
    game.main_loop()
