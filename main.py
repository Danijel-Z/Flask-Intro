# Såna här klasser används inom databaser,
# eller för att kommunicera med /ändra databasen
class Player:
    namn = ""
    jersey = ""
    team = "Apollo"


p1 = Player()
p1.namn = "alaska"

p2 = Player()
p2.namn = "bleach"

# Offentliga/Public variablar inom Klasser
# En bra OOP, Objekt Orienterad Kod


class Employee:
    BaseHourSalary = 100
    SeniorHourSalary = 150

    def __init__(self, namn: str, alder: int):
        self._namn = namn
        self._alder = alder

    def calculateYearSalary(self):
        if self._alder < 1972:
            return self._alder * Employee.SeniorHourSalary
        return self._alder * Employee.BaseHourSalary


Emp = Employee("Danijel", 2001)
årslön = Emp.calculateYearSalary()
print(årslön)
