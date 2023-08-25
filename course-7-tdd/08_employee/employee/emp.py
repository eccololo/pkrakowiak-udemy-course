class Employee:

    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, second_name, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    @property
    def email(self):
        return f"{self.first_name}.{self.second_name}@mail.com"

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))
