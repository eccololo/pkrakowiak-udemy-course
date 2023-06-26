# Zaimplementuj klase Soldier ktora przyjmie ilosc dni slużby i wypisze ile lat oraz dni ten zolnierz
# slozyl.

class Soldier:
    military_count = 0

    def __init__(self, name, rank, years_of_service):
        self.name = name
        self.rank = rank
        self.years_of_service = years_of_service
        Soldier.military_count += 1

    # Enter your solution here
    @staticmethod
    def calculate_years_of_service(days):
        years = days // 365
        days = days % 365
        return f'{years} year(s), {days} days'
