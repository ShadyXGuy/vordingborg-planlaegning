#Udkommenter koden der implementerer __add__ og forklar fejlbeskeden ved kørsel.
#Hvilken anden speciel metode er implementeret for klassen Point? Hvad bruges den til i kodeeksemplet?
#Udvid koden med overlæsning af subtraktion og/eller negativt fortegn, se operator module.
#Lav en generisk funktion til at udskrive "Simon says hello" hvor "hello"
#skal være et funktionsargument af en type der implementerer metoden __str__.
#Afprøv både med et Point, et tal og en tekststreng.
from random import randint

from numpy.random import random_integers


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)




a = Point(1, 0)
b = Point(2, 3)

print (a - b)

print (a + b)


def simonSay(say):
    print(f"Simon says {say}")

simonSay("hello") # say: = str
simonSay(2) # say: = int
simonSay(a) # say: = Point