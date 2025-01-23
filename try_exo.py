annee_liste = ["2019", "2020", "2021", "2022", "2023", "2024"]
annee_dict = {
    "2019": 3927,
    "2020": 4920,
    "2021": 7402,
    "2032": 3902,
    "2023": 3840,
    "2025": 9367
}

for annee in annee_liste:
    try:
        number_of_poops = annee_dict[annee]
        print(number_of_poops)
    except:
        print("key did noit exist on dict")
