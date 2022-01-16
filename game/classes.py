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
        self.canGoRight = True
        self.canGoLeft = True
        self.maxVelocity = Velocity(0.5, 2)
        self.enableLogging = False
        self.isGrounded = True
        self.jumpHeight = 0.9

    def verifyVelocity(self, ax=0, ay=0):
        return abs(self.velocity.x)+ax < self.maxVelocity.x and self.velocity.y+ay < self.maxVelocity.y

    def accelerateRight(self, a=0.05):
        if(self.verifyVelocity(0.05, 0)):
            self.velocity.x += a

    def accelerateLeft(self, a=-0.05):
        if(self.verifyVelocity(0.05, 0)):
            self.velocity.x += a

    def jump(self):
        if self.gravityEnabled == False:
            self.velocity.y = -self.jumpHeight
            self.gravityEnabled = True

    def update(self, dt):
        # if (self.enableLogging):
        #     print(self.gravityEnabled)
        if (self.gravityEnabled and self.verifyVelocity()):

            self.velocity.y += self.gravity
        if (self.velocity.x > 0 and self.canGoRight):
            self.position.x += self.velocity.x * dt
        if (self.velocity.x < 0 and self.canGoLeft):
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
    def __init__(self, position, height, width, sprite, speed):
        self.position = position
        self.height = height
        self.width = width
        self.sprite = sprite
        self.speed = speed
        self.isBouncing = False
        self.isMovingRight = True

    def update(self, dt, minX, maxX):
        if (self.isBouncing):
            if (self.position.x < minX):
                self.isMovingRight = True
            if (self.position.x+self.width > maxX):
                self.isMovingRight = False
            if(self.isMovingRight):
                self.position.x += self.speed * dt
            else:
                self.position.x -= self.speed * dt
