class Czlowiek:

    def __init__(self, imie, nazwisko):
        
        self.imie = imie
        self.nazwisko = nazwisko

    def info(self):
        print(f"{self.imie} {self.nazwisko}")


class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, nazwa_klubu):
        super().__init__(imie, nazwisko)
        self.klub = nazwa_klubu

    def info_o_zawodniku(self):
        print(f"Klub: {self.klub}")

pilkarz_1 = Pilkarz("Kamil", "Mila", "Bayern")
pilkarz_2 = Pilkarz("Krzysztof", "Piątek", "AC Milan")

pilkarz_1.info()
pilkarz_1.info_o_zawodniku()

pilkarz_2.info()
pilkarz_2.info_o_zawodniku()