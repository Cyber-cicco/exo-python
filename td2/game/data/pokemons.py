from pokemon import Pokemon, TypePlante, TypeFeu, TypeEau
from attack import AttackType
from combat import Combat

import random
import data.attacks as att

# Merci ☭ DeepSeek ☭
# Context : 
# * data.attacks
# * data.pokemons
# * pokemon
# Instructions :

#I want you to complete the dracofeu IA with the following guidance:
#
# * if he is against a TypePlate, he is more likely to use fire attacks
# * if he is against a TypeFeu or TypeEau, he is more likely to use normal attacks
# * If he is low HP, he is more likely to use high variance attacks (with more crit chance and more power based on his attack power)
# * If the ennemy is low HP, he is more likely to use low variance attacks
#
#I want you to implement it in a way so that there is a mult-dimensional space matrice,
#and each one of theses characteristics position him on a point of this matrice,
#influencing the likeliness of each attack to be thrown
#
# Demandera une abstraction à l'avenir
def dracofeu_ia(combat:Combat, source:Pokemon, target:Pokemon) -> list[str]:
    diags: list[str] = []
    attacks = list(source.attacks.items())  # List of (attack_name, Attack)
    weights = []

    for _, attack in attacks:
        weight = 1.0

        # Adjust for opponent type
        if isinstance(target, TypePlante):
            if attack.atk_type == AttackType.FEU:
                weight *= 2.0  # Favor Fire attacks against Grass
        elif isinstance(target, (TypeFeu, TypeEau)):
            if attack.atk_type == AttackType.NORMAL:
                weight *= 2.0  # Favor Normal attacks against Fire/Water

        # Adjust if Dracofeu is low HP (<=30%)
        draco_hp_ratio = source.hp / source.hp_max
        if draco_hp_ratio <= 0.3:
            variance = attack.crit_chance + (attack.pwr_mult / 10)
            weight *= 1.0 + (variance / 100)  # Boost high variance attacks

        # Adjust if enemy is low HP (<=30%)
        enemy_hp_ratio = target.hp / target.hp_max
        if enemy_hp_ratio <= 0.3:
            variance = attack.crit_chance + (attack.pwr_mult / 10)
            weight *= 1.0 - (variance / 200)  # Penalize high variance attacks

        weights.append(weight)

    # Normalize weights to probabilities
    total_weight = sum(weights)
    if total_weight == 0:
        probabilities = [1.0 / len(attacks) for _ in attacks]
    else:
        probabilities = [w / total_weight for w in weights]

    # Select attack based on probabilities
    chosen_index = random.choices(range(len(attacks)), weights=probabilities, k=1)[0]
    chosen_attack_name = attacks[chosen_index][0]
    diags.append(f"{source.nom} utilise {chosen_attack_name}!")
    source.attaquer(target, source.attacks[chosen_attack_name], combat.turn_count, diags)
    return diags

# Merci ☭ DeepSeek ☭
# Context : 
# * data.attacks
# * data.pokemons
# * data.afflictions
# * combat
# * pokemon
#
# Instructions :
#I want you to complete the dracofeu IA with the following guidance:
#
#I want you to complete the bulbizarre IA with the following guidance:
#
# * if he is against a TypePlante, or TypeFeu, he is more likely to use normal attacks
# * if he is against a TypeEau, he is more likely to use plate attacks
# * If it is the beginning of the battle, he is more likely to use powerful poison attacks
# * If the ennemy is low HP, he is less likely to use poison attacks
#
# Demandera une abstraction à l'avenir
def bulbizarre_ia(combat: Combat, source: Pokemon, target: Pokemon) -> list[str]:
    diags = []
    attacks = list(source.attacks.items())
    weights = []

    for _, attack in attacks:
        weight = 1.0

        # Type-based adjustments
        if isinstance(target, (TypePlante, TypeFeu)):
            if attack.atk_type == AttackType.NORMAL:
                weight *= 2.0  # Boost Normal against Grass/Fire
        elif isinstance(target, TypeEau):
            if attack.atk_type == AttackType.PLANTE:
                weight *= 2.0  # Boost Plant against Water

        # Early battle poison boost
        if combat.turn_count <= 2:
            if attack.afflictions and any('poison' in aff.name for aff in attack.afflictions):
                weight *= 2.5  # Favor poison attacks in first 3 turns

        # Enemy low HP poison penalty
        enemy_hp_ratio = target.hp / target.hp_max
        if enemy_hp_ratio <= 0.3:
            if attack.afflictions and any('poison' in aff.name for aff in attack.afflictions):
                weight *= 0.3  # Reduce poison when enemy is low

        weights.append(weight)

    # Normalize probabilities
    total_weight = sum(weights)
    if total_weight == 0:
        probabilities = [1.0/len(attacks)] * len(attacks)
    else:
        probabilities = [w/total_weight for w in weights]

    # Select attack
    chosen_index = random.choices(range(len(attacks)), weights=probabilities, k=1)[0]
    chosen_name = attacks[chosen_index][0]
    chosen_attack = attacks[chosen_index][1]
    
    diags.append(f"{source.nom} utilise {chosen_name}!")
    source.attaquer(target, chosen_attack, combat.turn_count, diags)
    return diags

POKEMONS = {
    "Salamèche" : TypeFeu(
        nom="Salamèche",
        hp=45,
        atk=18,
        df=3,
        spdf=5,
        attacks={
            "flammiche" : att.ATTACKS["flammiche"],
            "terre brulée" : att.ATTACKS["terre brulée"],
            "coup de queue" : att.ATTACKS["coup de queue"],
            "rafaldecou" : att.ATTACKS["rafaldecou"],
        },
        ia=dracofeu_ia,
    ),
    "Bulbizarre" : TypePlante(
        nom="Bulbizarre",
        hp=50,
        atk=15,
        df=4,
        spdf=10,
        attacks={
            "épines empoisonnées" : att.ATTACKS["épines empoisonnées"],
            "coup de tête" : att.ATTACKS["coup de tête"],
            "déracinement" : att.ATTACKS["déracinement"],
        },
        ia=bulbizarre_ia,
    ),
}
