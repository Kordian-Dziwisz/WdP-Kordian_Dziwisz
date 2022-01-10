import pygame as pg
import classes as game
import config as conf
import collisions


def main():
    # initialize the pygame module
    pg.init()

    # display init
    screen = pg.display.set_mode((conf.displayWidth, conf.displayHeight))
    pg.display.set_caption(conf.gameName)

    # load and set the logo
    logo = pg.image.load(conf.logoPath)
    pg.display.set_icon(logo)

    # load sprites
    # sprite.set_alpha(None)
    # sprite.set_colorkey((int('6C', 16), int('74', 16), int('7D', 16)))
    # sprite.set_alpha(120)

    player1 = game.Player(game.Position(0, 0), 100, 50, game.Velocity(
        0, 0), conf.gravity, pg.image.load(conf.character1SpritePath), game.Controls(pg.K_COMMA, pg.K_e, pg.K_a))

    platforms = []
    platforms.append(game.Platform(game.Position(400, 600), 50,
                                   300, pg.image.load(conf.platformsSpritePath)))
    platforms.append(game.Platform(game.Position(800, 700), 50,
                                   300, pg.image.load(conf.platformsSpritePath)))
    platforms.append(game.Platform(game.Position(800, 500), 50,
                                   300, pg.image.load(conf.platformsSpritePath)))
    platforms.append(game.Platform(game.Position(400, 400), 50,
                                   300, pg.image.load(conf.platformsSpritePath)))

    keyPressed = False
    clock = pg.time.Clock()
    running = True

    while running:
        # update screen and objects
        dt = clock.tick(120)
        screen.fill((255, 50, 50))
        # player sprite
        screen.blit(player1.sprite, (player1.position.x, player1.position.y))
        # obstacle sprites
        for platform in platforms:
            screen.blit(platform.sprite,
                        (platform.position.x, platform.position.y))

        pg.display.flip()
        player1.update(dt)

        # collisions
        grounded = collisions.screenEdges(
            conf.displayWidth, conf.displayHeight, conf.gravity, conf.bouncyness, player1)
        collisions.platforms(
            platforms, player1, grounded
        )

        # event handling, gets Lall event from the event queue
        if keyPressed:
            if keyPressed[player1.controls.up]:
                player1.jump()
            if keyPressed[player1.controls.right]:
                player1.accelerateRight()
            if keyPressed[pg.K_a]:
                player1.accelerateLeft()

        for event in pg.event.get():
            keyPressed = pg.key.get_pressed()
            # only do something if the event is of type QUIT
            if event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
