from arene import Arene


def afficher_menu():
    print("\n---------------- MENU ----------------")
    print("1. Ajouter un personnage")
    print("2. Voir les personnages dans l’arène")
    print("3. Faire combattre deux personnages")
    print("4. Afficher l'historique des combats")
    print("5. Soigner un personnage")
    print("6. Nettoyer l'arène")
    print("7. Nombre de combattants dans l'arène")
    print("8. Lancer le Battle Royale")
    print("9. Quitter")

arene = Arene()

choix = "0"
while choix != "9":
    afficher_menu()
    choix = input("Quel est votre choix (1-9)? ")
    if choix == "1":
        arene.ajouter_personnage()
    elif choix == "2":
        arene.afficher_personnages()
    elif choix == "3":
        if len(arene.liste_personnages) >= 2 :
            arene.afficher_personnages()
            index_1 = int(input("Entrer le numéro du premier combattant\n"))
            arene.afficher_personnages()
            index_2 = int(input("Entrer le numéro du deuxième combattant\n"))
            arene.faire_combattre(arene.liste_personnages[index_1], arene.liste_personnages[index_2])
        else :
            print("Vous devez avoir au moins deux combattants pour faire un combat!")
    elif choix == "4":
        arene.afficher_historique()
    elif choix == "5":
        arene.afficher_personnages()
        index_soins = int(input("Entrer le numéro du combattant\n"))
        arene.soigner_personnage(index_soins)
    elif choix == "6":
        arene.nettoyer_arene()
    elif choix == "7":
        print(f"Nombre de combattants: {len(arene)}")
    elif choix == "8":
        arene.lancer_battle_royale()
    elif choix == "9":
        print("\nGAME OVER")
    else:
        print("\nCHOIX INVALIDE, RÉESSAYEZ")
