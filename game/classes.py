import config as conf
import pygame as pg
import copy
import asyncio
import time
import math


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def toTuple(self):
        return (self.x, self.y)


class Size:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def toTuple(self):
        return (self.width, self.height)


class Velocity:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __neg__(self):
        return Velocity(-self.x, -self.y)


class Controls:
    def __init__(self, up, right, left, shoot):
        self.up = up
        self.right = right
        self.left = left
        self.shoot = shoot


class UIElementGroup:
    def __init__(self, texts=False, rects=False):
        if not texts:
            self.texts = {}
        if not rects:
            self.rects = {}
        # self.texts = texts
        # self.rects = rects


class UITextBox:
    def __init__(self, pg, font='Roboto', size=30, text='', position=Position(), color=(0, 0, 0), playerRef=None):
        self.font = pg.font.SysFont(font, size)
        self.surface = self.font.render(text, False, color)
        self.color = color
        self.text = text
        self.position = position
        self.hidden = False
        self.playerRef = playerRef

    def update(self, text):
        self.text = text
        self.surface = self.font.render(self.text, False, self.color)


class UIRect:
    def __init__(self, pg, position=Position(), size=Size(), color=False):
        self.pg = pg
        if not color:
            color = (255, 255, 255)
        self.rect = pg.Rect(position.toTuple(), size.toTuple())
        self.surface = pg.Surface(size.toTuple())
        pg.draw.rect(
            self.surface, color, self.rect)
        self.position = position
        self.size = size
        self.hidden = False

    def changeColor(self, color=(255, 255, 255)):
        self.pg.draw.rect(self.surface, color, self.rect)


class PhysicalObject:
    def __init__(self, position, height, width, sprite, velocity=Velocity(0, 0), maxVelocity=Velocity(math.inf, math.inf), gravity=conf.gravity):
        self.position = position
        self.height = height
        self.width = width
        self.sprite = sprite
        self.velocity = velocity
        self.maxVelocity = maxVelocity
        self.gravity = gravity
        self.canGoRight = True
        self.canGoLeft = True
        self.isGrounded = True

    def verifyVelocity(self, a=Velocity(0, 0)):
        return abs(self.velocity.x+a.x) < self.maxVelocity.x and self.velocity.y+a.y < self.maxVelocity.y

    def update(self, dt, friction=0.001):
        if (self.verifyVelocity(Velocity(0, self.gravity))):
            self.velocity.y += self.gravity
        if (self.velocity.x > 0 and self.canGoRight):
            self.position.x += self.velocity.x * dt
        if (self.velocity.x < 0 and self.canGoLeft):
            self.position.x += self.velocity.x * dt
        if self.velocity.x > 0:
            self.velocity.x -= friction * dt
            if self.velocity.x < 0:
                self.velocity.x = 0
        else:
            self.velocity.x += friction * dt
            if self.velocity.x > 0:
                self.velocity.x = 0
        self.position.y += self.velocity.y * dt


class Player(PhysicalObject):
    def __init__(self, position, height, width, velocity, maxVelocity, gravity, sprite, controls, health=1, name=''):
        super().__init__(
            position, height, width, sprite, velocity, maxVelocity, gravity)
        self.controls = controls
        self.jumpHeight = 0.9
        self.reloaded = True
        self.reloadDuration = 0.5
        self.health = health
        self.name = name
        self.dead = False
        self.isTurnedRight = True

    def accelerateRight(self, a=0.05):
        if(self.verifyVelocity(Velocity(a, 0))):
            self.velocity.x += a
            if self.velocity.x > 0:
                self.isTurnedRight = True

    def accelerateLeft(self, a=-0.05):
        if(self.verifyVelocity(Velocity(a, 0))):
            self.velocity.x += a
            if self.velocity.x < 0:
                self.isTurnedRight = False

    def jump(self):
        if self.gravity == 0:
            self.velocity.y = -self.jumpHeight
            self.gravity = conf.gravity

    def reload(self):
        time.sleep(self.reloadDuration)
        self.reloaded = True
        return True

    def shoot(self, velocity, sprite):
        if (self.reloaded):
            self.reloaded = False
            loop = asyncio.get_event_loop()
            future1 = loop.run_in_executor(None, self.reload)
            return Bullet(copy.deepcopy(self.position), 20, 20, sprite, self, velocity, gravity=0) if self.isTurnedRight else Bullet(copy.deepcopy(self.position), 20, 20, sprite, self, -velocity, gravity=0)
        else:
            return False

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        self.dead = True


class Platform:
    def __init__(self, position, height, width, sprite, velocity):
        self.position = position
        self.height = height
        self.width = width
        self.sprite = sprite
        self.velocity = velocity
        self.isBouncing = False

    def update(self, dt, minX, maxX):
        if (self.isBouncing):
            if (self.position.x < minX):
                self.velocity.x = abs(self.velocity.x)
            if (self.position.x+self.width > maxX):
                self.velocity.x = -abs(self.velocity.x)
            self.position.x += self.velocity.x * dt


class Bullet(PhysicalObject):
    def __init__(self, position, height, width, sprite, owner, velocity=Velocity(1, 0), maxVelocity=Velocity(math.inf, math.inf), gravity=0, damage=1):
        super().__init__(position, height, width, sprite, velocity, maxVelocity, gravity)
        self.owner = owner
        self.damage = damage
