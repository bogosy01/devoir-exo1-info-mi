def table_verite_entree():
    # Demande à l'utilisateur la fonction logique
    fonction_logique = input("Entrez la fonction logique (par exemple, '(a and b) or not c'): ")

    # Demande à l'utilisateur les noms des variables (séparés par des virgules)
    noms_variables_str = input("Entrez les noms des variables (séparés par des virgules, par exemple, 'a,b,c'): ")
    noms_variables = [nom.strip() for nom in noms_variables_str.split(',')]

    n = len(noms_variables)

    # Initialise les listes pour stocker les mintermes et les maxtermes
    mintermes = []
    maxtermes = []

    # Imprime l'en-tête de la table de vérité
    print("|", end="")
    for var in noms_variables:
        print(f" {var} |", end="")
    print(f" {fonction_logique} |")

    # Imprime la ligne de séparation
    print("|", end="")
    for _ in range(n + 1):
        print("---|", end="")
    print()

    # Itère sur toutes les combinaisons possibles de valeurs de vérité
    for i in range(2**n):
        # Convertit l'entier i en une chaîne binaire, puis la remplit avec des zéros à gauche
        ligne = bin(i)[2:].zfill(n)

        # Crée un dictionnaire pour stocker les valeurs de vérité des variables
        dictionnaire_verite = {noms_variables[j]: bool(int(ligne[j])) for j in range(n)}

        # Évalue la fonction logique
        resultat = eval(fonction_logique, {}, dictionnaire_verite)

        # Imprime la ligne de la table de vérité
        print("|", end="")
        for j in range(n):
            print(f" {int(dictionnaire_verite[noms_variables[j]])} |", end="")
        print(f" {int(resultat)} |")

        # Si le résultat est Vrai, ajoute le minterme à la liste
        if resultat:
            minterme = [f"{noms_variables[j]}" if dictionnaire_verite[noms_variables[j]] else f"¬{noms_variables[j]}" for j in range(n)]
            mintermes.append(' × '.join(minterme))
        # Si le résultat est Faux, ajoute le maxterme à la liste
        else:
            maxterme = [f"¬{noms_variables[j]}" if dictionnaire_verite[noms_variables[j]] else f"{noms_variables[j]}" for j in range(n)]
            maxtermes.append(' + '.join(maxterme))

    # Imprime les formes canoniques
    print("\nPremière Forme Canonique (SOP):")
    print(f"F = {' + '.join(mintermes)}")

    print("\nDeuxième Forme Canonique (POS):")
    print(f"F = {'(' + ')('.join(maxtermes) + ')'}")

# Exemple d'utilisation
table_verite_entree()
