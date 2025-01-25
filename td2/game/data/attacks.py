from attack import Attack, AttackType
import data.afflictions as aff


ATTACKS = {
    "flammiche" : Attack(
        nom="flammiche",
        atk_type=AttackType.FEU,
        base_pwr=14,
        pwr_mult=55
    ),
    "terre brulée" : Attack(
        nom="terre brulée",
        atk_type=AttackType.FEU,
        base_pwr=9,
        pwr_mult=55,
        crit_chance=40,
    ),
    "coup de tête" : Attack(
        nom="coup de tête",
        atk_type=AttackType.NORMAL,
        base_pwr=14,
        pwr_mult=55
    ),
    "coup de queue": Attack(
        nom="coup de queue",
        atk_type=AttackType.NORMAL,
        base_pwr=13,
        pwr_mult=65
    ),
    "bulle d'O": Attack(
        nom="bulle d'O",
        atk_type=AttackType.EAU,
        base_pwr=14,
        pwr_mult=55
    ),
    "déracinement": Attack(
        nom="déracinement",
        atk_type=AttackType.PLANTE,
        base_pwr=13,
        pwr_mult=65
    ),
    "rafaldecou": Attack(
        nom="rafaldecou",
        atk_type=AttackType.NORMAL,
        base_pwr=6,
        pwr_mult=200,
        crit_chance=30
    ),
    "épines empoisonnées": Attack(
        nom="épines empoisonnées",
        atk_type=AttackType.PLANTE,
        base_pwr=10,
        pwr_mult=45,
        afflictions=[aff.AFFLICTIONS["poison_1"]]
    ),
    "arsenic": Attack(
        nom="arsenic",
        atk_type=AttackType.NORMAL,
        base_pwr=0,
        pwr_mult=0,
        afflictions=[aff.AFFLICTIONS["poison_3"]]
    ),
    "verre suspect": Attack(
        nom="verre suspect",
        atk_type=AttackType.EAU,
        base_pwr=0,
        pwr_mult=0,
        afflictions=[aff.AFFLICTIONS["sommeil_3"]]
    ),
}
