import pygame
import projektUre
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
import time

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 1200
Y = 1000

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y), pygame.RESIZABLE)

pygame.display.set_caption('Epic Gamer Watch')

font = pygame.font.Font('freesansbold.ttf', 32)



watch = pygame.time.Clock()

#ur til loop
ur = projektUre.Ur()

hour = Dropdown(
    display_surface, 120, 57, 100, 15, name='Select Day',
    choices=[
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'
    ],
    borderRadius=3, colour=pygame.Color('green'),  direction='down', textHAlign='centre',
)

minute = Dropdown(
    display_surface, 230, 57, 100, 15, name='Select Hour',
    choices=[
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'
    ],
    borderRadius=3, colour=pygame.Color('green'),  direction='down', textHAlign='centre',
)

second = Dropdown(
    display_surface, 340, 57, 100, 15, name='Select Minute',
    choices=[
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'
    ],
    borderRadius=3, colour=pygame.Color('green'),  direction='down', textHAlign='centre',
)



def print_value():
    print(hour.getSelected(), minute.getSelected(), second.getSelected())

def reset_value():
    hour.reset()
    minute.reset()
    second.reset()

button = Button(
    display_surface, 10, 50, 100, 30, text='Print Value', fontSize=30,
    margin=20, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0),
    radius=5, onClick=print_value, font=pygame.font.SysFont('freesansbold', 20),
    textVAlign='centre', textHAlign='centre'
)

resetButton = Button(
    display_surface, 10, 100, 100, 30, text='Reset', fontSize=30,
    margin=20, inactiveColour=(0, 120, 120), pressedColour=(0, 255, 0),
    radius=5, onClick=reset_value, font=pygame.font.SysFont('freesansbold', 20),
    textVAlign='centre', textHAlign='centre'
)


# infinite loop
while True:

    display_surface.fill(white)


    #text = font.render(str(projektUre.updateTimer()[2]), True, green, blue)
    ur.updateTimer()
    text = font.render(str(f"{ur.day:02} / {ur.month:02} / {ur.year} \n {ur.hour:02}:{ur.minute:02}:{ur.second:02}"), True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    display_surface.blit(text, textRect)

    textRect.center = (X // 2, Y // 2)

    projektUre.alarm.setTime(hour.getSelected(), minute.getSelected(), second.getSelected())

    print(hour.getSelected(), minute.getSelected(), second.getSelected())



    if projektUre.alarm.check():
        print("WAKE UP AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        alarmtext = font.render("ALARM!", True, (255, 0, 0))
        alarmRect = alarmtext.get_rect()
        alarmRect.center = (X // 2, Y // 2)
        display_surface.blit(alarmtext, alarmRect)



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        # Draws the surface object to the screen.

    pygame_widgets.update(pygame.event.get())
    pygame.display.update()
    watch.tick(60)