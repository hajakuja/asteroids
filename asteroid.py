import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen:pygame.Surface):
        pygame.draw.circle(screen, "cadetblue1", self.position, self.radius, width=2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return (None, None)
        else:
            rnd_angle = random.uniform(20.0, 50.0)
            first_vel = self.velocity.rotate(rnd_angle)
            second_vel = self.velocity.rotate(-rnd_angle)
            first_child = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            second_child = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            first_child.velocity = first_vel * 1.8
            second_child.velocity = second_vel * 1.8
            return (first_child, second_child)
