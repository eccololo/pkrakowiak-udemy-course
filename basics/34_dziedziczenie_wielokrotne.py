class Czlowiek:

    pochodzenie = "Ziemia"
    imie = "Jack"


class Polak:

    kraj = "Polska"
    imie = "Jan"


class Pilkarz(Czlowiek, Polak):

    def info(self):
        print(f"Utworzony czlowiek pochodzi z planety {self.pochodzenie}.\n" 
        f"Kraj pochodzenia: {self.kraj}.\n"
        f"Nazwa obiektu: {self.imie}.")


pilkarz_1 = Pilkarz()
pilkarz_1.info()
