"""
Oprindelig fra https://github.com/martinrs/karakterbog_paradigme_demo/blob/main/objektorienteret.py

Karakterbog og logbog er begge bøger.
"""

from dataclasses import dataclass


@dataclass
class Fag:
    navn: str
    karakter: int | None = None


class Bog:
    separator = "―"

    def __init__(self, navn: str = "Navnløs"):
        self.navn = navn
        self.data = []

    def __str__(self, indhold: str | None = None) -> str:
        output = ""
        output += self.separator * 35 + "\n\n"
        if indhold is None:
            output += f"Bog for: {self.navn}\n\n"
        else:
            output += indhold
        output += self.separator * 35 + "\n"
        return output


class KarakterBog(Bog):
    def tilføjFag(self, navn: str, karakter: int | None = None):
        self.data.append(Fag(navn, karakter))

    def beregnSnit(self) -> str:
        total = 0
        for fag in self.data:
            total += fag.karakter
        return f"Karaktergennemsnit af {len(self.data)} fag: {round(total / len(self.data), 2)}"

    def genererKarakterOversigt(self) -> str:
        output = ""
        for fag in self.data:
            output += f"Karakteren i {fag.navn.capitalize()} er: {fag.karakter}\n"
        return output

    def __str__(self) -> str:
        indhold = ""
        indhold += f"Karakterbog for: {self.navn}\n\n"
        indhold += self.beregnSnit() + "\n\n"
        indhold += self.genererKarakterOversigt() + "\n"
        return super().__str__(indhold)


class Logbog(Bog):
    def tilføjLog(self, log: str):
        self.data.append(log)

    def __str__(self) -> str:
        indhold = ""
        indhold += f"Logbog for: {self.navn}\n\n"
        for i, log in enumerate(self.data):
            indhold += f"{i+1}. {log}\n"
        return super().__str__(indhold)


if __name__ == "__main__":
    batmans_bog = Bog("Batman")

    print(batmans_bog)

    batmans_kb = KarakterBog("Batman")
    batmans_kb.tilføjFag("spelunking", 7)
    batmans_kb.tilføjFag("crime fighting", 12)
    batmans_kb.separator = "🦇"

    print(batmans_kb)

    batmans_lb = Logbog("Batman")
    batmans_lb.tilføjLog("Faldt i en brønd")
    batmans_lb.tilføjLog("Kæmpede mod Jokeren")

    print(batmans_lb)
