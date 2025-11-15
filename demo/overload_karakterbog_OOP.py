"""
Oprindelig fra https://github.com/martinrs/karakterbog_paradigme_demo/blob/main/objektorienteret.py
Overlæsning og generiske funktioner kan også udføres i funktionel og procedural paradigme


Overlæsning:
    - Konstruktøren for begge klasser er allerede overlæst.
    - Karakterbog har også operatorer overlæst:
        - __str__ metoden overlæst for at give en pæn udskrift.
        - __add__ metoden overlæst for at kunne lægge to karakterbøger sammen (selvom det i praksis er spøjst).


Generisk funktion:
    - Som udgangspunkt alle funktioner i Python. Vi kan angive datatyper, men det gennemtvinges ikke.
    - Vi kan fx angive Batmans navn (str) som et tal uden problemer.
"""


class Fag:
    def __init__(self, navnet, karakteren=None):
        self.navn = navnet
        self.karakter = karakteren


class KarakterBog:
    separator = "―"

    def __init__(self, elev="Navnløs"):
        self.elevNavn = elev
        self.data = []

    def tilføjFag(self, fag):
        self.data.append(fag)

    def beregnSnit(self):
        total = 0
        for fag in self.data:
            total += fag.karakter
        return f"Karaktergennemsnit af {len(self.data)} fag: {round(total / len(self.data), 2)}"

    def genererKarakterOversigt(self):
        output = ""
        for fag in self.data:
            output += f"Karakteren i {fag.navn.capitalize()} er: {fag.karakter}\n"
        return output

    def __str__(self):
        output = ""
        output += self.separator * 35 + "\n\n"
        output += f"Karakterbog for: {self.elevNavn}\n\n"
        output += self.beregnSnit() + "\n\n"
        output += self.genererKarakterOversigt() + "\n"
        output += self.separator * 35 + "\n"
        return output

    def __add__(self, other):
        kb = KarakterBog(f"{self.elevNavn} og {other.elevNavn}")
        kb.data.extend(self.data)
        kb.data.extend(other.data)
        return kb


if __name__ == "__main__":
    martins = KarakterBog("Martin")
    martins.tilføjFag(Fag("dansk", 4))
    martins.tilføjFag(Fag("programmering", 12))
    martins.tilføjFag(Fag("innovation", -3))
    martins.tilføjFag(Fag("teknologi", -3))
    martins.tilføjFag(Fag("opvask", 12))
    martins.tilføjFag(Fag("racerbil", 12))

    batmans = KarakterBog("Batman")
    batmans.tilføjFag(Fag("spelunking", 7))
    batmans.tilføjFag(Fag("romancing", 2))
    batmans.tilføjFag(Fag("public speaking", -3))
    batmans.tilføjFag(Fag("ninja", 10))
    batmans.tilføjFag(Fag("crime fighting", 12))
    batmans.separator = "🦇"

    print(batmans)
    print(martins)

    # print(martins + batmans)
