class Armure :


    def __init__(self, nom: str, armure : int) :
        self.nom = nom
        self._armure = 0
        self.set_armure(armure)


    def set_armure(self, armure : int):
        if 0 <= armure <= 15:
            self._armure = armure
        elif armure < 0:
            self._armure = 0
        else:
            self._armure = 15

    def get_armure(self) -> int:
        return self._armure

