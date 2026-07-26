tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        tache = input("Entrez une tâche : ")
        tasks.append(tache)
        print("Tâche ajoutée avec succès !")

    elif choix == "2":
        if len(tasks) == 0:
            print("Aucune tâche.")
        else:
            print("\nListe des tâches :")
            for i, tache in enumerate(tasks, start=1):
                print(f"{i}. {tache}")

    elif choix == "3":
        if len(tasks) == 0:
            print("Aucune tâche à supprimer.")
        else:
            for i, tache in enumerate(tasks, start=1):
                print(f"{i}. {tache}")

            numero = int(input("Numéro de la tâche : "))

            if 1 <= numero <= len(tasks):
                tasks.pop(numero - 1)
                print("Tâche supprimée.")
            else:
                print("Numéro invalide.")

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Choix invalide.")
