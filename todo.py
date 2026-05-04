import json

FICHIER = "todo.json"
# Charger les données depuis le fichier JSON

def charger():
    try:
        with open(FICHIER, "r") as f:
            return json.load(f)    # lire les données existantes
    except FileNotFoundError:
        return {"todo": [], "doing": [], "done": []}

def sauvegarder(data):
    with open(FICHIER, "w") as f:
        json.dump(data, f, indent=2)

def afficher(data):
    colonnes = ["todo", "doing", "done"]
    print("\n" + "=" * 50)
    print("            TABLEAU KANBAN")
    print("=" * 50)
    for col in colonnes:
        print(f"\n  [{col.upper()}]")
        if data[col]:
             # afficher chaque tâche avec un numéro
            for i, tache in enumerate(data[col], 1):
                print(f"    {i}. {tache}")
        else:
            print("    (vide)")
    print("\n" + "=" * 50)

def ajouter(data):
    tache = input("Nom de la tache: ")
    data["todo"].append(tache)
    sauvegarder(data)
    print(f"Tache '{tache}' ajoutee dans TODO.")

def deplacer(data):
    colonnes = ["todo", "doing", "done"]
    print("Colonnes: 1-TODO  2-DOING  3-DONE")
    try:
        src = int(input("Depuis quelle colonne? (1-3): ")) - 1
        col_src = colonnes[src]
        if not data[col_src]:
            print("Colonne vide!")
            return
        print(f"Taches dans {col_src.upper()}:")
        for i, t in enumerate(data[col_src], 1):
            print(f"  {i}. {t}")
        idx = int(input("Numero de la tache: ")) - 1
        dest = int(input("Vers quelle colonne? (1-3): ")) - 1
        col_dest = colonnes[dest]
        tache = data[col_src].pop(idx)
        data[col_dest].append(tache)
        sauvegarder(data)
        print(f"'{tache}' deplacee vers {col_dest.upper()}.")
    except (ValueError, IndexError):
        print("Choix invalide.")

def supprimer(data):
    colonnes = ["todo", "doing", "done"]
    print("Colonnes: 1-TODO 2-DOING 3-DONE")
    try:
        src = int(input("Depuis quelle colonne? (1-3): ")) - 1
        col = colonnes[src]
        if not data[col]:
            print("Colonne vide!")
            return
        for i, t in enumerate(data[col], 1):
            print(f"  {i}. {t}")
        idx = int(input("Numero de la tache a supprimer: ")) - 1
        tache = data[col].pop(idx)
        sauvegarder(data)
        print(f"'{tache}' supprimee.")
    except (ValueError, IndexError):
        print("Choix invalide.")

def main():
    data = charger()
   # la Boucle principale
    while True:
        afficher(data)
        print("\n1. Ajouter une tâche")
        print("2. Déplacer une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        choix = input("\nChoix: ")
        if choix == "1":
            ajouter(data)
        elif choix == "2":
            deplacer(data)
        elif choix == "3":
            supprimer(data)
        elif choix == "4":
            print("Au revoir!")
            break

if __name__ == "__main__":
    main()
