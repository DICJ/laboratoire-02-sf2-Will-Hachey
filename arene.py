from personnage import *

class Arene:

    def __init__(self):

        self.liste_personnages = []
        self.historique_combats = []

    def __len__(self):
        return len(self.liste_personnages)


    def afficher_personnages(self):
        if not self.liste_personnages :
            print("Aucun personnage dans l'arène")
        else :
            for position,personnage in enumerate(self.liste_personnages,start=0) :
                print(f"{position}. {personnage}")


    def ajouter_personnage(self):
        print("1. Guerrier")
        print("2. Mage")
        print("3. Archer")
        print("4. Soldat")

        classe = "0"
        while classe not in ["1", "2", "3", "4"]:
            classe = input("Entrer la classe de votre personnage (1-4): ")

        nom = input("Entrer le nom du personnage : ")
        vie = int(input("Entrer la vie du personnage (0-500): "))
        attaque = int(input("Entrer l'attaque du personnage (0-50): "))

        personnage = ""
        if classe == "1":
            force = int(input("Entrer la force du guerrier (1-50): "))
            armure = Armure("Armure de plaque", 12)
            personnage = Guerrier(nom, vie, attaque, force, armure)
        elif classe == "2":
            mana = int(input("Entrer le mana du mage (0-100): "))
            armure = Armure("Armure de plaque", 7)
            personnage = Mage(nom, vie, attaque, mana, armure)
        elif classe == "3":
            dexterite = int(input("Entrer la dextérité de l'archer (40-70): "))
            armure = Armure("Armure de plaque", 5)
            personnage = Archer(nom, vie, attaque, dexterite, armure)
        elif classe == "4":
            armure = Armure("Armure de plaque", 15)
            personnage = Soldat(nom, vie, attaque, armure)

        self.liste_personnages.append(personnage)
        print(f"{personnage.nom} a été ajouté")
        return personnage


    def faire_combattre(self, personnage1, personnage2):

        combat = DetailsCombat(personnage1.nom, personnage2.nom)

        while personnage1.get_vie() > 0 and personnage2.get_vie() > 0:
            # Tour de personnage 1
            combat.incrementer_tour()
            degats = personnage1.attaquer()
            print(f"{personnage1.nom} attaque {personnage2.nom} et lui inflige {degats} dégâts.")
            personnage2.subir_degat(degats)

            if personnage2.get_vie() <= 0:
                print(f"\n{personnage1.nom} a vaincu {personnage2.nom} !")
                combat.definir_vainqueur(personnage1.nom)
                self.historique_combats.append(combat)
                break

            # Tour de personnage 2
            combat.incrementer_tour()
            degats = personnage2.attaquer()
            print(f"{personnage2.nom} attaque {personnage1.nom} et lui inflige {degats} dégâts.")
            personnage1.subir_degat(degats)

            if personnage1.get_vie() <= 0:
                print(f"\n {personnage2.nom} a vaincu {personnage1.nom} !")
                combat.definir_vainqueur(personnage2.nom)
                self.historique_combats.append(combat)
                break

            print(f" {personnage1.nom} (Vie: {personnage1.get_vie()}) | "
                  f"{personnage2.nom} (Vie: {personnage2.get_vie()})\n")

    def afficher_historique(self):
        if not self.historique_combats :
            print("Aucun combat dans l'historique")
        else :
            for combat in self.historique_combats:
                print(f"------------------------------")
                print(f"Personnage #1: {combat.nom_personnage_1}")
                print(f"Personnage #2: {combat.nom_personnage_2}")
                print(f"Vainqueur: {combat.vainqueur}")
                print(f"Nombre de tours: {combat.nombre_tours}")

    def soigner_personnage(self,index):
        combattant = self.liste_personnages[index]
        combattant.reset()

    def nettoyer_arene(self):
        liste_copie = list(self.liste_personnages)
        for combattant in liste_copie:
            if combattant.get_vie() == 0:
                self.liste_personnages.remove(combattant)
        return None

    def lancer_battle_royale(self):
        for combattant in self.liste_personnages:
            combattant.reset()
        while len(self.liste_personnages) >= 2:
            self.faire_combattre(self.liste_personnages[0], self.liste_personnages[1])
            self.nettoyer_arene()
        print(f"Le gagnant est: {self.liste_personnages[0].nom}")
        self.afficher_personnages()
        return None


class DetailsCombat:

    def __init__(self, nom_1: str, nom_2: str):

        self.nom_personnage_1 = nom_1
        self.nom_personnage_2 = nom_2
        self.vainqueur = ""
        self.nombre_tours = 0

    def incrementer_tour(self):
        self.nombre_tours += 1
        return None

    def definir_vainqueur(self, nom_vainqueur):
        self.vainqueur = nom_vainqueur
        return None
