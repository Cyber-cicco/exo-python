calcs = {
    "*" : lambda num_1, num_2 : num_1 * num_2,
    "+" : lambda num_1, num_2 : num_1 + num_2,
    "-" : lambda num_1, num_2 : num_1 - num_2,
    "/" : lambda num_1, num_2 : num_1 / num_2,
    "**" : lambda num_1, num_2 : num_1 ** num_2,
    "%" : lambda num_1, num_2 : num_1 % num_2,
}

def main_loop():
    result:int
    num_1 = number_enter("Entrez un premier nombre : ")
    num_2 = number_enter("Entrez deuxième nombre : ")
    operand = symbol_enter("Veuillez entrer l'opérande : ", ("*", "+", "-", "/", "**", "%"))
    print(f"le résultat est {calcs[operand](num_1, num_2)}")
    proceed = symbol_enter("souhaitez vous continuer ? [y/n] : ", ("y", "Y", "n", "N"))
    if proceed == "y" or proceed == "Y":
        main_loop()

def number_enter(prompt:str) -> float:
    try:
        nbr = float(input(prompt))
        return nbr
    except ValueError:
        return number_enter("Erreur de syntaxe. Veuillez saisir un nombre de nouveau : ")

def symbol_enter(prompt:str, symboles:tuple) -> str:
    sym = input(prompt)
    if sym not in symboles:
        return symbol_enter("Erreur de syntaxe. L'opérande doit être l'un des symboles suivants : *, +, -, /, **, % : ", symboles)
    return sym

main_loop()
