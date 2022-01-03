import pygame


def main():

    # initialize the pygame module
    pygame.init()
    displayWidth = 1280
    displayHeight = 720
    # load and set the logo
    logo = pygame.image.load("bg.png")
    pygame.display.set_icon(logo)
    sprite = pygame.image.load("character.png")
    sprite.set_alpha(None)
    sprite.set_colorkey((int('6C', 16), int('74', 16), int('7D', 16)))
    sprite.set_alpha(120)
    pygame.display.set_caption("game")

    screen = pygame.display.set_mode((displayWidth, displayHeight))

    # define a variable to control the main loop
    running = True

    xpos = 0
    ypos = 0
    # how many pixels we move our smiley each frame

    class Velocity:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
    player_v = Velocity(0, 0)
    gravity = 0.1
    clock = pygame.time.Clock()
    # main loop
    while running:
        dt = clock.tick(60)
        # collision with edges of the screen
        # pygame.display.flip()
        screen.fill((255, 120, 120))
        screen.blit(sprite, (xpos, ypos))
        pygame.display.flip()
        isOutside = False
        if (abs(player_v.y) < 0.1*0.9):
            player_v.y = 0
        if (abs(player_v.x) < 0.1*0.9):
            player_v.x = 0
        if ypos < displayHeight - 100:
            player_v.y -= gravity
        if ypos >= displayHeight-100:
            player_v.y = abs(player_v.y) * 0.9
        if ypos <= 0:
            player_v.y = -abs(player_v.y)*0.9
        if xpos >= displayWidth - 50:
            player_v.x = -abs(player_v.x)*0.9
        if xpos <= 0:
            player_v.x = abs(player_v.x)*0.9
        # if ypos < displayHeight - 100 and ypos > 0 and xpos < displayWidth - 50 and xpos > 0 and isOutside:
        #     isOutside = False
        ypos += -player_v.y * dt
        xpos += player_v.x * dt
        print(ypos)

        # event handling, gets Lall event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                sprite
                # change the value to False, to exit the main loop
                running = False
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_COMMA]:
                if (ypos >= displayHeight - 100):
                    player_v.y += 1
            if keyPressed[pygame.K_e]:
                player_v.x += 0.1
            if keyPressed[pygame.K_o]:
                player_v.y += -0.1
            if keyPressed[pygame.K_a]:
                player_v.x += -0.1


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
