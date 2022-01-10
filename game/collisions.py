def screenEdges(width, height, gravity, bouncyness, player):
    if (abs(player.velocity.y) < gravity*bouncyness):
        player.velocity.y = 0
    if player.position.y > height - 100:
        player.position.y = height - 100
        player.gravityEnabled = False
        # player.velocity.y = -abs(player.velocity.y) * bouncyness
        player.velocity.y = 0
    # if player.position.y <= 0: BOUNCING FROM TOP OF THE SCREEN
    #     player.velocity.y = -abs(player.velocity.y)*bouncyness
        return True
    if player.position.x > width - 50:
        player.position.x = width - 50
        player.velocity.x = -abs(player.velocity.x)*bouncyness
    if player.position.x < 0:
        player.velocity.x = abs(player.velocity.x)*bouncyness
        player.position.x = 0


def platforms(platforms, player, grounded):
    for platform in platforms:
        if player.position.x + player.width >= platform.position.x and player.position.x <= platform.position.x+platform.width and player.position.y + player.height >= platform.position.y and player.position.y <= platform.position.y:
            print('platform collision')
            # entering platform
            if(player.position.y + player.height <= platform.position.y + platform.height):
                player.position.y = platform.position.y - player.height
                player.gravityEnabled = False
            else:
                player.velocity.y = 0
                if (player.position.x + player.width > platform.position.x):
                    player.velocity.x = 0
                    player.position.x = platform.position.x - player.width - platform.width
                if player.position.x < platform.position.x + platform.width:
                    player.velocity.x = 0
                    player.position.x = platform.position.x + platform.width
            return True
    if (not grounded):
        player.gravityEnabled = True
    return False
