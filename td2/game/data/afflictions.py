from pokemon import Pokemon
from attack import Affliction, AfflictionFunc

def poison_on_inflict(pokemon:Pokemon, diags:list[str]) -> list[str]:
    diags.append(f"{pokemon.nom} vient de se faire empoisonner !")
    return diags

def poison_on_turn(pokemon:Pokemon, diags:list[str]) -> list[str]:
    dmg = int(pokemon.hp_max / 10)
    pokemon.hp -= dmg
    diags.append(f"Le poison coule dans les veines de {pokemon.nom} ! Il subit {dmg} points de dégâts.")
    return diags


def poison_recover(pokemon:Pokemon, diags:list[str]) -> list[str]:
    diags.append(f"{pokemon.nom} a guéri du poison.")
    return diags

def sommeil_on_inflict(pokemon:Pokemon, diags:list[str]) -> list[str]:
    diags.append(f"{pokemon.nom} s'endort... ")
    return diags

def sommeil_on_turn(pokemon:Pokemon, diags:list[str]) -> list[str]:
    pokemon.able_to_act = False
    diags.append(f"{pokemon.nom} dort paisiblement.")
    return diags

def sommeil_recover(pokemon:Pokemon, diags:list[str]) -> list[str]:
    diags.append(f"{pokemon.nom} vient de se réveiller.")
    return diags
    
AFFLICTIONS = {
    "poison_1": Affliction(
        name="poison_1",
        effect=AfflictionFunc(
            poison_on_inflict,
            poison_on_turn,
            poison_recover,
        ),
        chances_working=30, 
        min_turns=1, 
        max_turns=3, 
        recovery_chance=50
    ),
    "poison_2": Affliction(
        name="poison_2",
        effect=AfflictionFunc(
            poison_on_inflict,
            poison_on_turn,
            poison_recover,
        ),
        chances_working=40, 
        min_turns=1, 
        max_turns=5, 
        recovery_chance=30
    ),
    "poison_3": Affliction(
        name="poison_3",
        effect=AfflictionFunc(
            poison_on_inflict,
            poison_on_turn,
            poison_recover,
        ),
        chances_working=60, 
        min_turns=3, 
        max_turns=6, 
        recovery_chance=20
    ),
    "sommeil_1": Affliction(
        name="sommeil_1",
        effect=AfflictionFunc(
            sommeil_on_inflict,
            sommeil_on_turn,
            sommeil_recover,
        ),
        chances_working=30, 
        min_turns=1, 
        max_turns=3, 
        recovery_chance=50
    ),
    "sommeil_2": Affliction(
        name="sommeil_2",
        effect=AfflictionFunc(
            sommeil_on_inflict,
            sommeil_on_turn,
            sommeil_recover,
        ),
        chances_working=40, 
        min_turns=1, 
        max_turns=5, 
        recovery_chance=30
    ),
    "sommeil_3": Affliction(
        name="sommeil_3",
        effect=AfflictionFunc(
            sommeil_on_inflict,
            sommeil_on_turn,
            sommeil_recover,
        ),
        chances_working=60, 
        min_turns=3, 
        max_turns=6, 
        recovery_chance=20
    ),
}
