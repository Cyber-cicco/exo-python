from typing import Callable

class Article:

    def __init__(self, reference:str, nom:str, prix:float, qte:int):
        self.reference = reference
        self.nom = nom
        self.prix = prix
        self.qte = qte

    def __str__(self) -> str:
        return f"Reference : {self.reference}, Nom : {self.nom}, Prix : {self.prix}, Quantité: {self.qte}"

class Store:

    def __init__(self, articles:list) -> None:
        self.reference_dict = {}
        for article in articles:
            self.reference_dict[article.reference] = article

    def get_article_by_reference(self, reference:str) -> [Article, None]:
        try:
            article = self.reference_dict[reference]
            return article
        except KeyError:
            return None

    def add_article(self, article:Article):
        if self.reference_dict.get(article.reference) is None:
            self.reference_dict[article.reference] = article
        else : 
            print("L'article existe déjà")

    def delete_article(self, reference:str):
        if self.reference_dict.get(reference) is not None:
            del self.reference_dict[reference]

    def modify_article(self, article:Article) -> None:
        if self.reference_dict.get(article.reference) is not None:
            self.reference_dict[article.reference] = article
        else:
            print("Reference did not match any article in the store")

    def find_by_nom(self, nom:str) -> list:
        result = []
        for article in self.reference_dict.values():
            if article.nom == nom:
                result.append(article)
        return result

    def find_in_price_range(self, lower:float, upper:float) -> None:
        result = []
        for article in self.reference_dict.values():
            if article.prix >= lower and article.prix <= upper:
                result.append(article)
        return result

    def show_articles(self) -> None:
        for article in self.reference_dict.values():
            print(article)

class Menu:

    def __init__(self, options:list) -> None:
        self.option_dict = {}
        for option in options:
            self.option_dict[option.number] = option

    def execute(self, number:int) -> None:
        try:
            should_continue = self.option_dict[number].callable()
            if should_continue:
                self.showMenu()

        except KeyError:
            print(f"Unknown option {number}. Please specifiy a valid entry ")
            self.showMenu()

    def showMenu(self) -> None:
        print("Bienvenue dans l'application de gestion des stocks !")
        for option in self.option_dict.values():
            option.show_in_menu()
        try:
            choice = int(input("Veuillez choisir une option parmis celles proposées : "))
            self.execute(choice)

        except ValueError:
            print("Veuillez entrer un chiffre valide")
            self.showMenu()


class Option:

    def __init__(self, number:int, description:str, callable:Callable[[],bool]):
        self.number = number
        self.callable = callable
        self.description = description

    def show_in_menu(self):
        print(f"{self.number} : {self.description}")


if __name__ == "__main__":
    store = Store([
        Article("1", "Camembert", 3.4, 15),
        Article("2", "Coulommier", 3.4, 15),
        Article("3", "Bire", 3.4, 15),
        Article("4", "Saint pautlin", 3.4, 15),
        Article("5", "azhelkrjazekr", 3.4, 15),
        Article("6", "Yest", 3.4, 15),
        Article("7", "Fraisses", 3.4, 15),
        Article("8", "Framboises", 3.4, 15),
        Article("9", "Perceuses", 3.4, 15),
        Article("10", "Perceuse à camembert", 3.4, 15),
        Article("11", "Ouiiiiiiiii", 3.4, 15),
    ])

    def find_by_reference() -> bool:
        reference = input("Veuillez entrer la référence : ")
        article = store.get_article_by_reference(reference)
        if article != None:
            print(article)
        else:
            print("L'article n'a pas été trouvé")
        return True

    option_1 = Option(1, "Rechercher un article par référence", find_by_reference)

    def get_reference() -> str :
        reference = input("Veuillez saisir la référence de l'article : ")
        if len(reference) < 2 or len(reference) > 30:
            print("La référence doit être un chaine de caractère de longueur 2 minium et 30 maximum")
            return get_reference()
        return reference

    def get_nom() -> str :
        nom = input("Veuillez saisir le nom de l'article : ")
        if len(nom) < 2 or len(nom) > 20:
            print("le nom doit être un chaine de caractère de longueur 2 minium et 20 maximum")
            return get_nom()
        return nom

    def get_prix(prompt:str="Veuillez saisir prix de l'article : ") -> float :
        try:
            prix = float(input(prompt))
            return prix
        except:
            print("Le prix doit être un nombre valide")
            return get_prix()

    def get_quantite() -> int :
        try:
            qte = int(input("Veuillez saisir la quantité : "))
            return qte
        except:
            print("Le prix doit être un nombre valide")
            return get_quantite()


    def build_article() -> Article:
        reference = get_reference()
        nom = get_nom()
        prix = get_prix()
        quantite = get_quantite()
        return Article(reference, nom, prix, quantite)

    def add_article() -> bool:
        print("Saisie du nouvel article")
        article = build_article()
        store.add_article(article)
        return True

    option_2 = Option(2, "Ajouter un nouvel article", add_article)

    def remove_article() -> bool:
        reference = input("Saisissez la référence de l'article que vous souhaitez supprimer : ")
        store.delete_article(reference)
        return True

    option_3 = Option(3, "Supprimer un article", remove_article)

    def modify_article() -> bool:
        print("Modification d'un article")
        article = build_article()
        store.modify_article(article)
        return True

    option_4 = Option(4, "Modifier un article", modify_article)

    def rechercher_par_nom() -> bool:
        nom = input("Saisissez le nom de l'article ou des articles : ")
        articles = store.find_by_nom(nom)
        for article in articles:
            print(article)
        return True

    option_5 = Option(5, "Rechercher un article par nom", rechercher_par_nom)

    def rechercher_par_reference() -> bool:
        reference = input("Saisissez la référence de l'article : ")
        articles = store.get_article_by_reference(reference)
        print(article)
        return True

    option_6 = Option(6, "Rechercher un article par référence", rechercher_par_reference)

    def rechercher_par_intervalle() -> bool:
        prix_bas = get_prix("Veuillez saisir la borne basse de prix : ")
        prix_haut = get_prix("Veuillez saisir la haute basse de prix : ")
        articles = store.find_in_price_range(prix_bas, prix_haut)
        print(article)
        return True

    option_7 = Option(7, "Faire une recherche par intervalle de prix", rechercher_par_intervalle)

    def show_articles() -> bool:
        store.show_articles()
        return True

    option_8 = Option(8, "Afficher tous les articles", show_articles)

    option_9 = Option(9, "Quitter", lambda: False)

    menu = Menu([
        option_1,
        option_2,
        option_3,
        option_4,
        option_5,
        option_6,
        option_7,
        option_8,
        option_9,
    ])

    menu.showMenu()

