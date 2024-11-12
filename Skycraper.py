class Skyscraper:
    def __init__(self, name, bouwtype, gewicht, hoogte, stad):
        self.name = name
        self.bouwtype = bouwtype
        self.gewicht = gewicht
        self.hoogte = hoogte
        self.stad = stad

    def beschrijf(self):
        return f"Naam: {self.name}, Bouwtype: {self.bouwtype}"

    def __str__(self):
        return f"{self.name} heeft een hoogte van {self.hoogte} meter en ligt in {self.stad}."

    def __repr__(self):
        return f"Skyscraper(name='{self.name}', bouwtype='{self.bouwtype}', hoogte={self.hoogte})"

    def __eq__(self, other):
        return self.name == other.name and self.bouwtype == other.bouwtype

    def __lt__(self, other):
        return self.hoogte < other.hoogte

    def __add__(self, other):
        return self.hoogte + other.hoogte

    def __len__(self):
        return self.hoogte


Burj_Khalifa = Skyscraper("Burj Khalifa", "staal, beton", 500000000, 828, "Dubai")
Taipei_101 = Skyscraper("Taipei 101", "staal, beton", 700000000, 509, "Taipei")
Petronas_Towers = Skyscraper("Petronas Towers", "staal, beton", 35000000, 300, "Kuala Lumpur")


print(Taipei_101.beschrijf())
print(Petronas_Towers)
print(Petronas_Towers == Taipei_101)
print(Burj_Khalifa < Taipei_101)
print(Taipei_101 + Petronas_Towers)
print(len(Burj_Khalifa))