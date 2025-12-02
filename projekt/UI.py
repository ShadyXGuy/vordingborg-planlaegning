import pygame
import projektUre

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Show Text')

font = pygame.font.Font('freesansbold.ttf', 32)



watch = pygame.time.Clock()


# infinite loop
while True:

    display_surface.fill(white)


    text = font.render(str(projektUre.updateTimer()[2]), True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    display_surface.blit(text, textRect)

    textRect.center = (X // 2, Y // 2)



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        # Draws the surface object to the screen.
    pygame.display.update()
    watch.tick(60)