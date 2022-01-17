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
    def __init__(self, position, height, width, velocity, maxVelocity, gravity, sprite, controls, health=1):
        super().__init__(
            position, height, width, sprite, velocity, maxVelocity, gravity)
        self.controls = controls
        self.jumpHeight = 0.9
        self.reloaded = True
        self.reloadDuration = 0.5
        self.health = health
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
