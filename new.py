#https://stackoverflow.com/questions/39709065/making-pygame-sprites-disappear-in-python

import pygame
pygame.init()
pygame.font.init() #Initialize fonts so we can have text appear when bricks are destroyed


screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

"""class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height):
        # Call the parent class (Sprite) constructor
        #super(Button, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 100, color)
        self.image = pygame.Surface((width, height))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, (0,0))
        print("Is Text Working?")"""

#https://stackoverflow.com/questions/23056597/python-pygame-writing-text-in-sprite

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size=(32, 32), image=None): #Create the button
        super(Button, self).__init__()
        if image is None: #If there is no image when the Button is made, use this default rectangle
            self.rect = pygame.Rect(pos, size)
            self.image = pygame.Surface(size)
        else: #Otherwise, use the image
            self.image = image
            self.rect = image.get_rect(topleft=pos)
        self.pressed = False

    def update(self): #Update the button!
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0] #https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed Boolean returns true if left mouse button is pressed
        if self.rect.collidepoint(*mouse_pos) and mouse_clicked:
            self.kill()  # Will remove itself from all pygame groups.


image = pygame.Surface((100, 40))
image.fill((255, 0, 0))
buttons = pygame.sprite.Group()

#image = pygame.image.load("brick.png").convert_alpha() #This will put our custom brick in (messily)

buttons.add(
    Button(pos=(50, 25), image=image),
    Button(pos=(151, 25), image=image),
    Button(pos=(252, 25), image=image),
    Button(pos=(353, 25), image=image),
    Button(pos=(100, 70), image=image),
    Button(pos=(201, 70), image=image),
    Button(pos=(303, 70), image=image),
    Button(pos=(50, 115), image=image),
    Button(pos=(151, 115), image=image),
    Button(pos=(252, 115), image=image),
    Button(pos=(353, 115), image=image),
    Button(pos=(100, 160), image=image),
    Button(pos=(201, 160), image=image),
    Button(pos=(303, 160), image=image),
    Button(pos=(50, 205), image=image),
    Button(pos=(151, 205), image=image),
    Button(pos=(252, 205), image=image),
    Button(pos=(353, 205), image=image)

)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                buttons.add(Button(pos=(50, 25), image=image))
            elif event.key == pygame.K_2:
                buttons.add(Button(pos=(50, 75), image=image))
            elif event.key == pygame.K_3:
                buttons.add(Button(pos=(50, 125), image=image))

    buttons.update()  # Calls the update method on every sprite in the group.
    screen.fill((255, 255, 255))
    buttons.draw(screen)  # Draws all sprites to the given Surface.

    font = pygame.font.Font('freesansbold.ttf', 32)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    X = 400
    Y = 400

    text = font.render('GeeksForGeeks', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    image.blit(text, textRect)


    pygame.display.flip()
