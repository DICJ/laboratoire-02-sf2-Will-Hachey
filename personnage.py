from random import randint
from armure import *

class Personnage:


    def __str__(self):
        return f"{self.nom} | Vie: {self.get_vie()} | Attaque: {self.get_attaque()} | Armure: {self.armure.get_armure()}"

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure):

        # Attributs publics
        self.nom = nom

        # Attributs privés
        self._vie = 0
        self._vie_max = 0
        self.set_vie(vie)
        self.set_vie_max()
        self._attaque = 0
        self.set_attaque(attaque)
        self.armure = armure

    def set_vie(self, vie: int) -> None:
        if 0 <= vie <= 500:
            self._vie = vie
        elif vie < 0:
            self._vie = 0
        else:
            self._vie = 500

    def get_vie(self) -> int:
        return self._vie

    def set_vie_max(self):
        self._vie_max = self._vie
        return None

    def get_vie_max(self):
        return self._vie_max

    def set_attaque(self, attaque: int) -> None:
        if 0 <= attaque <= 50:
            self._attaque = attaque
        elif attaque < 0:
            self._attaque = 0
        else:
            self._attaque = 50

    def get_attaque(self) -> int:
        return self._attaque

    def subir_degat (self, degats: int) -> None:
        degat_final = degats - self.armure.get_armure()
        self.set_vie(self.get_vie() - degat_final)
        return None

    def reset(self):
        self._vie = self._vie_max
        return None


class Guerrier(Personnage):

    def __str__(self):
        return f"{self.nom} | Vie: {self.get_vie()} | Attaque: {self.get_attaque()} | Force: {self.get_force()} | Armure: {self.armure.get_armure()}"

    def __init__(self, nom: str, vie: int, attaque: int, force: int, armure: Armure):

        super().__init__(nom, vie, attaque, armure)

        # Attributs privés
        self._force = 0
        self.set_force(force)

    def set_force(self, force: int) -> None:
        if 1 <= force <= 50:
            self._force = force
        elif force < 1:
            self._force = 1
        else:
            self._force = 50

    def get_force(self) -> int:
        return self._force

    def attaquer(self) -> int:
        degats = int(self.get_attaque() + (self.get_force() / 2) + randint(-2, 2))
        return degats


class Mage(Personnage):

    def __str__(self):
        return f"{self.nom} | Vie: {self.get_vie()} | Attaque: {self.get_attaque()} | Mana: {self.get_mana()} | Armure: {self.armure.get_armure()}"

    def __init__(self, nom: str, vie: int, attaque: int, mana: int, armure: Armure):

        super().__init__(nom, vie, attaque, armure)

        # Attributs privés
        self._mana = 0
        self._mana_max = 0
        self.set_mana(mana)
        self.set_mana_max()

    def set_mana(self, mana: int) -> None:
        if 0 <= mana <= 100:
            self._mana = mana
        elif mana < 0:
            self._mana = 0
        else:
            self._mana = 100

    def get_mana(self) -> int:
        return self._mana

    def set_mana_max(self):
        self._mana_max = self._mana
        return None

    def get_mana_max(self):
        return self._mana_max

    def diminuer_mana(self) -> None:
        diminution = randint(15,25)
        if self.get_mana() >= diminution:
            self.set_mana(self.get_mana() - diminution)
        else:
            print("MANA INSUFFISANT")
            self.set_mana(0)
        return None

    def attaquer(self):
        self.diminuer_mana()
        degats = 0
        if self.get_mana() > 0:
            degats = self.get_attaque() + 60
        return degats

    def reset(self):
        super().reset()
        self.set_mana(self._mana_max)
        return None


class Archer(Personnage) :

    def __str__(self):
        return f"{self.nom} | Vie: {self.get_vie()} | Attaque: {self.get_attaque()} | Dexterite: {self.get_dexterite()} | Armure: {self.armure.get_armure()}"

    def __init__(self,nom : str,vie : int,attaque : int,dexterite : int, armure: Armure):

        super().__init__(nom, vie, attaque, armure)

        # - attributs privés
        self._dexterite = 0
        self.set_dexterite(dexterite)

    def set_dexterite(self, dexterite : int):
        if 40 <= dexterite <= 70 :
            self._dexterite = dexterite
        elif dexterite <= 40 :
            self._dexterite = 40
        else :
            self._dexterite = 70

    def get_dexterite(self) -> int :
        return self._dexterite

    def attaquer(self):
        nombre_aleatoire = randint(0,100)
        if nombre_aleatoire < self.get_dexterite() :
           degat = 2 * (self.get_attaque() + 15)
           return degat
        else :
            degat = self.get_attaque() + 15
            return  degat


class Soldat(Personnage):

    def __str__(self):
        return f"{self.nom} | Vie: {self.get_vie()} | Attaque: {self.get_attaque()} | Armure: {self.armure.get_armure()}"

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure):

        super().__init__(nom, vie, attaque, armure)


    def attaquer(self) -> int:
        degats = int(self.get_attaque())
        return degats

    def subir_degat (self, degats: int) -> None:
        degat_final = int(round((degats - self.armure.get_armure()) * 0.90, 0))
        self.set_vie(self.get_vie() - degat_final)
        return None