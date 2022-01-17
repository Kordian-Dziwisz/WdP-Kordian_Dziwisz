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
    bulletSprite = pg.image.load(
        conf.bulletSpritePath).convert()
    bulletSprite.set_colorkey((255, 255, 255))
    bulletSprite = pg.transform.scale(bulletSprite, (20, 20))

    # main game objects init
    player1 = game.Player(game.Position(0, 0), 100, 50, game.Velocity(
        0, 0), game.Velocity(0.5, 2), conf.gravity, pg.image.load(conf.character1SpritePath).convert(), game.Controls(pg.K_COMMA, pg.K_e, pg.K_a, pg.K_o))
    player1.enableLogging = True
    player2 = game.Player(game.Position(conf.displayWidth-100, 0), 100, 50, game.Velocity(
        0, 0), game.Velocity(0.5, 2), conf.gravity, pg.image.load(conf.character2SpritePath).convert(), game.Controls(pg.K_c, pg.K_n, pg.K_h, pg.K_t))
    players = [player1, player2]

    platforms = []
    platforms.append(game.Platform(game.Position(400, 600), 50,
                                   300, pg.image.load(conf.platformsSpritePath).convert(), game.Velocity(0.5, 0)))
    platforms.append(game.Platform(game.Position(800, 700), 50,
                                   300, pg.image.load(conf.platformsSpritePath).convert(), game.Velocity(0.5, 0)))
    platforms.append(game.Platform(game.Position(800, 500), 50,
                                   300, pg.image.load(conf.platformsSpritePath).convert(), game.Velocity(0.5, 0)))
    platforms.append(game.Platform(game.Position(400, 400), 50,
                                   300, pg.image.load(conf.platformsSpritePath).convert(), game.Velocity(0.5, 0)))
    platforms[2].isBouncing = True

    bullets = []

    keyPressed = False
    clock = pg.time.Clock()
    running = True

    while running:
        # clock
        dt = clock.tick(60)
        screen.fill((255, 50, 50))

        # sprites updates
        for player in players:
            screen.blit(player.sprite,
                        (player.position.x, player.position.y))
        for platform in platforms:
            screen.blit(platform.sprite,
                        (platform.position.x, platform.position.y))
        for bullet in bullets:
            screen.blit(bullet.sprite, (bullet.position.x, bullet.position.y))

        # object updates
        for player in players:
            player.update(dt)
        for platform in platforms:
            platform.update(dt, 0, conf.displayWidth)
        for bullet in bullets:
            bullet.update(dt, 0)
        pg.display.flip()

        # collisions
        collisions.screenEdges(player1)
        collisions.screenEdges(player2)
        collisions.platforms(
            platforms, player1
        )
        collisions.platforms(
            platforms, player2
        )
        collisions.bullets(bullets, players=players)

        # player deaths
        for player in players:
            if player.dead:
                players.remove(player)
                running = False

        # event handling, gets Lall event from the event queue
        if keyPressed:
            for player in players:
                if keyPressed[player.controls.right]:
                    player.accelerateRight()
                if keyPressed[player.controls.left]:
                    player.accelerateLeft()
                if keyPressed[player.controls.up]:
                    player.jump()
                if keyPressed[player.controls.shoot]:
                    bullet = player.shoot(
                        game.Velocity(1, 0), bulletSprite)
                    if(bullet):
                        bullets.append(bullet)

        for event in pg.event.get():
            # only do something if the event is of type QUIT
            keyPressed = pg.key.get_pressed()
            if event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False

                # run the main function only if this module is executed as the main script
                # (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
