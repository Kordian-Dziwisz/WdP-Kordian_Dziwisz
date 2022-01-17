import config as conf


def screenEdges(player, screenWidth=conf.displayWidth, screenHeight=conf.displayHeight, gravity=conf.gravity, bouncyness=conf.bouncyness):
    player.isGrounded = False
    if player.position.y > screenHeight - 100:
        # print('fallen')
        # print(player.position.y)
        player.position.y = screenHeight - 100
        player.gravity = 0
        # player.velocity.y = -abs(player.velocity.y) * bouncyness
        player.velocity.y = 0
    # if player.position.y <= 0: BOUNCING FROM TOP OF THE SCREEN
    #     player.velocity.y = -abs(player.velocity.y)*bouncyness
        player.isGrounded = True
    if player.position.x > screenWidth - 50:
        player.position.x = screenWidth - 50
        player.velocity.x = -abs(player.velocity.x)*bouncyness
    if player.position.x < 0:
        player.position.x = 0
        player.velocity.x = abs(player.velocity.x) * bouncyness


def platforms(platforms, player):
    tolerance = 10
    for platform in platforms:
        if player.position.x + player.width >= platform.position.x and player.position.x <= platform.position.x+platform.width and player.position.y + player.height >= platform.position.y and player.position.y <= platform.position.y:
            # print('platform collision')
            # entering platform
            if (player.position.y <= platform.position.y + tolerance):
                if (player.position.y+player.height <= platform.position.y + platform.height + tolerance):
                    player.position.y = platform.position.y - player.height
                    player.gravity = 0
                    player.velocity.y = 0
                else:
                    player.position.y = platform.position.y + tolerance
                    player.velocity.y = 0
            else:
                if (player.position.x + player.width < platform.position.x+tolerance):
                    player.velocity.x = 0
                    player.position.x = platform.position.x - player.width
                elif player.position.x+player.width > platform.position.x + platform.width-tolerance:
                    player.velocity.x = 0
                    player.position.x = platform.position.x + platform.width
            return True
    if (not player.isGrounded):
        # print('enabling gravity')
        player.gravity = conf.gravity
    return False


def bullets(bullets, screenWidth=conf.displayWidth, screenHeight=conf.displayHeight, player=None, platforms=[]):
    for bullet in bullets:
        if bullet.position.y > screenHeight - bullet.height or bullet.position.y < 0 or bullet.position.x > screenWidth - bullet.width or bullet.position.x < 0:
            # print('outofboundaries')
            print(bullet)
            bullets.remove(bullet)
