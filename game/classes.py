class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Velocity:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Controls:
    def __init__(self, up, right, left):
        self.up = up
        self.right = right
        self.left = left


class Player:
    def __init__(self, position, height, width, velocity, gravity, sprite, controls):
        self.position = position
        self.height = height
        self.width = width
        self.velocity = velocity
        self.sprite = sprite
        self.controls = controls
        self.gravity = gravity
        self.gravityEnabled = True
        self.maxVelocity = Velocity(0.5, 2)

    def verifyVelocity(self):
        return abs(self.velocity.x) < self.maxVelocity.x and self.velocity.y < self.maxVelocity.y

    def accelerateRight(self, a=0.05):
        if(self.verifyVelocity()):
            self.velocity.x += a

    def accelerateLeft(self, a=0.05):
        if(self.verifyVelocity()):
            self.velocity.x -= a

    def jump(self, v=1):
        print(self.gravityEnabled)
        if self.gravityEnabled == False:
            self.velocity.y = -v
            self.gravityEnabled = True

    def update(self, dt):
        if (self.gravityEnabled and self.verifyVelocity()):
            self.velocity.y += self.gravity
        self.position.x += self.velocity.x * dt
        # print(self.velocity.x)
        if self.velocity.x > 0:
            self.velocity.x -= 0.001 * dt
            if self.velocity.x < 0:
                self.velocity.x = 0
        else:
            self.velocity.x += 0.001 * dt
            if self.velocity.x > 0:
                self.velocity.x = 0
        self.position.y += self.velocity.y * dt


class Platform:
    def __init__(self, position, height, width, sprite):
        self.position = position
        self.height = height
        self.width = width
        self.sprite = sprite
