#Brug polymorph_gui.py som udgangspunkt (kræver pygame).

#Læs koden og kør den. Forklar (skriv fx ned til logbog) og hvilken klasse der er defineret
#og hvad den nedarver fra.

#Fjern variablerne house1 og house2 og lav i stedet en liste med min. 3 huse.
#Tegn dem alle vha. en løkke.

#Lav din egen klasse til en simpel geometrisk tegning fx Z til at tegne Zorros tegn.
#Den skal nedarve fra samme klasse som husene.

#Lav en sprite.Group med både huse og dine egne objekter. Tegn dem alle vha. et kald til draw() på gruppen.

#Lav en underklasse til Sprite kaldet Shape.

    #Tilføj en metode i klassen med signaturen def get_points(self) som skal returnere alle punkter i figuren.

    #Opdater klassen for huse og din egen metode til at nedarve fra Shape i stedet for Sprite.

    #Sørg for at metoden get_points kun er defineret i Shape.

import pygame


class House(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coords = [
            (0, 100),
            (0, 50),
            (25, 0),
            (50, 50),
            (50, 100),
        ]
        self.image = pygame.Surface([50, 100])
        self.image.fill(pygame.Color(255, 255, 255))
        self.rect = pygame.draw.polygon(self.image, (0, 0, 0), self.coords, 5)
        self.rect = self.rect.move(x - 25, y)




pygame.init()
screen = pygame.display.set_mode((500, 500))

#house1 = pygame.sprite.Group(House(50, 100))
#house2 = pygame.sprite.Group(House(250, 100))

hus = [pygame.sprite.Group(House(250, 100)), pygame.sprite.Group(House(50, 100)), pygame.sprite.Group(House(450, 100))]

def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))
        for i in hus:
            i.draw(screen)
        #house1.draw(screen)
        #house2.draw(screen)
        pygame.display.flip()


run()
