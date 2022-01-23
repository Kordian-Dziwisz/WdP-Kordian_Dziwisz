import pygame as pg
import classes as game
import config as conf
import collisions
import json
import copy


def main():
    # initialize the pygame module
    pg.init()
    pg.font.init()

    # display init
    screen = pg.display.set_mode((conf.displayWidth, conf.displayHeight))
    pg.display.set_caption(conf.gameName)

    # load and set the logo
    logo = pg.image.load(conf.logoPath)
    pg.display.set_icon(logo)

    # load highscores from files
    file = open('highscores.json', 'r')
    highscores = file.read()
    highscores = json.loads(highscores)
    print(highscores)

    # game phases
    # gamePhases = ('menu', 'game', 'pause', 'gameover', 'high_scores')
    activeGamePhase = 'menu'

    # config UI Elements
    UIElements = {}

    # UI categories
    UIElements['menu'] = game.UIElementGroup()
    UIElements['pause'] = game.UIElementGroup()
    UIElements['game'] = game.UIElementGroup()
    UIElements['high_scores'] = game.UIElementGroup()
    UIElements['gameover'] = game.UIElementGroup()

    # menu UI
    UIElements['menu'].texts['new_game'] = game.UITextBox(
        pg, 'Roboto Black', 50, 'Start a new game', game.Position(100, 100), (255, 255, 255))
    UIElements['pause'].texts['resume'] = game.UITextBox(
        pg, 'Roboto Black', 50, 'Resume', game.Position(100, 100), (255, 255, 255))
    UIElements['menu'].texts['high_scores'] = game.UITextBox(
        pg, 'Roboto Black', 40, 'Show Highscores', game.Position(100, 200), (255, 255, 255))
    UIElements['menu'].texts['exit'] = game.UITextBox(
        pg, 'Roboto Black', 40, 'exit', game.Position(100, 500), (255, 255, 255))
    UIElements['menu'].rects['menu_bg'] = game.UIRect(
        pg, size=game.Size(400, conf.displayHeight), color=(0, 0, 0))
    UIElements['menu'].texts['player_1_input_header'] = game.UITextBox(
        pg, 'Roboto Black', 40, 'Player 1 name:', game.Position(510, 110), (255, 255, 255))
    UIElements['menu'].texts['player_1_name'] = game.UITextBox(
        pg, 'Roboto Black', 40, 'adam', game.Position(510, 160), (255, 255, 255))
    UIElements['menu'].rects['player_1_input'] = game.UIRect(
        pg, game.Position(500, 100), game.Size(300, 100), (100, 100, 100))
    UIElements['menu'].texts['player_2_input_header'] = game.UITextBox(
        pg, 'Roboto Black', 40, 'Player 2 name:', game.Position(510, 310), (255, 255, 255))
    UIElements['menu'].texts['player_2_name'] = game.UITextBox(
        pg, 'Roboto Black', 40, 'eve', game.Position(510, 360), (255, 255, 255))
    UIElements['menu'].rects['player_2_input'] = game.UIRect(
        pg, game.Position(500, 300), game.Size(300, 100), (255, 255, 100))
    UIElements['menu'].rects['player_2_input'].changeColor((255, 255, 255))

    # pause UI
    UIElements['pause'].texts['exit'] = game.UITextBox(
        pg, 'Roboto Black', 40, 'exit', game.Position(100, 500))
    UIElements['pause'].rects['menu_bg'] = game.UIRect(
        pg, size=game.Size(400, conf.displayHeight))

    # game UI
    UIElements['game'].texts['player_1_hp'] = game.UITextBox(
        pg, 'Roboto Black', 30, 'Player hp: 0', game.Position(30, 30))
    UIElements['game'].texts['player_2_hp'] = game.UITextBox(
        pg, 'Roboto Black', 30, 'Player hp: 0', game.Position(30, 80))

    # gameover UI
    UIElements['gameover'].texts['winner'] = game.UITextBox(
        pg, 'Roboto Black', 30, 'The winner is: Player', game.Position(100, 100), (0, 0, 0))
    UIElements['gameover'].texts['return'] = game.UITextBox(
        pg, 'Roboto Black', 30, 'Click here to return to menu', game.Position(100, 150), (0, 0, 0))

    # highscores UI
    UIElements['gameover'].texts['winner'] = game.UITextBox(
        pg, 'Roboto Black', 30, '', game.Position(100, 100), (0, 0, 0))

    # load bullet sprites
    bulletSprite = pg.image.load(
        conf.bulletSpritePath).convert()
    bulletSprite = pg.transform.scale(bulletSprite, (20, 20))

    # main game objects init
    player1 = game.Player(game.Position(0, 0), 100, 50, game.Velocity(
        0, 0), game.Velocity(0.5, 2), conf.gravity, pg.image.load(conf.character1SpritePath).convert(), game.Controls(pg.K_COMMA, pg.K_e, pg.K_a, pg.K_o), 5, 'Adam')
    player2 = game.Player(game.Position(conf.displayWidth-100, 0), 100, 50, game.Velocity(
        0, 0), game.Velocity(0.5, 2), conf.gravity, pg.image.load(conf.character2SpritePath).convert(), game.Controls(pg.K_c, pg.K_n, pg.K_h, pg.K_t), 5, 'Eve')
    players = [player1, player2]

    # add player ref to hp info
    UIElements['game'].texts['player_1_hp'].playerRef = players[0]
    UIElements['game'].texts['player_2_hp'].playerRef = players[1]

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
    platforms[3].isBouncing = True

    bullets = []

    clock = pg.time.Clock()
    running = True
    keyPressed = False
    mouse_key_presses = [False, False, False]

    while running:
        # clock
        dt = clock.tick(60)
        screen.fill((255, 50, 50))

        if activeGamePhase in ('menu', 'pause'):
            # draw UI elements
            texts = UIElements[activeGamePhase].texts
            rects = UIElements[activeGamePhase].rects
            # print(UIElements)
            for rectKey in rects:
                if (not rects[rectKey].hidden):
                    screen.blit(rects[rectKey].surface,
                                rects[rectKey].position.toTuple())
            for textKey in texts:
                if (not texts[textKey].hidden):
                    screen.blit(texts[textKey].surface,
                                texts[textKey].position.toTuple())
            # detect input
            # start game
            _ngtext = UIElements['menu'].texts['new_game']
            _mpos = pg.mouse.get_pos()
            if _mpos[0] > _ngtext.position.x and _mpos[0] < _ngtext.position.x + _ngtext.surface.get_width() and _mpos[1] > _ngtext.position.y and _mpos[1] < _ngtext.position.y + _ngtext.surface.get_height():
                if mouse_key_presses[0]:
                    activeGamePhase = 'game'

            # highscores
            _ngtext = UIElements['menu'].texts['high_scores']
            if _mpos[0] > _ngtext.position.x and _mpos[0] < _ngtext.position.x + _ngtext.surface.get_width() and _mpos[1] > _ngtext.position.y and _mpos[1] < _ngtext.position.y + _ngtext.surface.get_height():
                if mouse_key_presses[0]:
                    pass
                    # activeGamePhase = 'high_scores'

            # exit
            _ngtext = UIElements['menu'].texts['exit']
            if _mpos[0] > _ngtext.position.x and _mpos[0] < _ngtext.position.x + _ngtext.surface.get_width() and _mpos[1] > _ngtext.position.y and _mpos[1] < _ngtext.position.y + _ngtext.surface.get_height():
                if mouse_key_presses[0]:
                    running = False

            pg.display.flip()

        elif activeGamePhase in ('game'):
            screen.fill((0, 0, 0))
            # ui
            texts = UIElements[activeGamePhase].texts
            for textKey in texts:
                if (not texts[textKey].hidden):
                    _newText = texts[textKey].text.split(' ')
                    # print(_newText)
                    _newText[-1] = str(texts[textKey].playerRef.health)
                    _newText[0] = str(texts[textKey].playerRef.name)

                    texts[textKey].update(' '.join(_newText))
                    screen.blit(texts[textKey].surface,
                                texts[textKey].position.toTuple())

            for player in players:
                screen.blit(player.sprite,
                            (player.position.x, player.position.y))
            for platform in platforms:
                screen.blit(platform.sprite,
                            (platform.position.x, platform.position.y))
            for bullet in bullets:
                screen.blit(bullet.sprite,
                            (bullet.position.x, bullet.position. y))
            # sprites updates

            # object updates
            for player in players:
                player.update(dt)
            for platform in platforms:
                platform.update(dt, 0, conf.displayWidth)
            for bullet in bullets:
                bullet.update(dt, 0)
            pg.display.flip()

            # collisions
            for player in players:
                collisions.screenEdges(player)
                collisions.platforms(
                    platforms, player
                )
                collisions.bullets(bullets, players=players)
            if (texts['player_1_hp'].text[-1] == 0):
                pass

            # player deaths
            for player in players:
                if player.dead:
                    players.remove(player)
                    activeGamePhase = 'gameover'

            # player event handling, gets Lall event from the event queue
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
        elif activeGamePhase in ('gameover'):
            screen.fill((255, 255, 255))
            texts = UIElements[activeGamePhase].texts
            _newText = texts['winner'].text.split(' ')
            _newText[-1] = players[0].name
            texts['winner'].update(' '.join(_newText))
            # print(UIElements)
            for textKey in texts:
                if (not texts[textKey].hidden):
                    # center text
                    texts[textKey].position.x = conf.displayWidth / \
                        2-texts[textKey].surface.get_width() / 2
                    screen.blit(texts[textKey].surface,
                                texts[textKey].position.toTuple())

            # reset player information
            player1 = game.Player(game.Position(0, 0), 100, 50, game.Velocity(
                0, 0), game.Velocity(0.5, 2), conf.gravity, pg.image.load(conf.character1SpritePath).convert(), game.Controls(pg.K_COMMA, pg.K_e, pg.K_a, pg.K_o), 5, 'Adam')
            player2 = game.Player(game.Position(conf.displayWidth-100, 0), 100, 50, game.Velocity(
                0, 0), game.Velocity(0.5, 2), conf.gravity, pg.image.load(conf.character2SpritePath).convert(), game.Controls(pg.K_c, pg.K_n, pg.K_h, pg.K_t), 5, 'Eve')
            players = [player1, player2]
            UIElements['game'].texts['player_1_hp'].playerRef = players[0]
            UIElements['game'].texts['player_2_hp'].playerRef = players[1]

            # return to menu
            _ngtext = UIElements['gameover'].texts['return']
            _mpos = pg.mouse.get_pos()
            if _mpos[0] > _ngtext.position.x and _mpos[0] < _ngtext.position.x + _ngtext.surface.get_width() and _mpos[1] > _ngtext.position.y and _mpos[1] < _ngtext.position.y + _ngtext.surface.get_height():
                if mouse_key_presses[0]:
                    activeGamePhase = 'menu'
            pg.display.flip()

        for event in pg.event.get():
            keyPressed = pg.key.get_pressed()
            if keyPressed[pg.K_q] and activeGamePhase == 'game':
                activeGamePhase = 'pause'

            if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP:
                mouse_key_presses = pg.mouse.get_pressed()

            if event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False

                # run the main function only if this module is executed as the main script
                # (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
