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

house1 = pygame.sprite.Group(House(50, 100))
house2 = pygame.sprite.Group(House(250, 100))


def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 255, 255))
        house1.draw(screen)
        house2.draw(screen)
        pygame.display.flip()


run()
