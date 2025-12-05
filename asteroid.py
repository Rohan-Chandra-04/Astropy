from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid split")
        new_angle = random.randint(20, 50)

        new_vel_vect1 = self.velocity.rotate(new_angle)
        new_vel_vect2 = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astro_child1 = Asteroid(self.position.x, self.position.y, new_radius)
        astro_child2 = Asteroid(self.position.x, self.position.y, new_radius)
        astro_child1.velocity = new_vel_vect1 * 1.2
        astro_child2.velocity = new_vel_vect2 * 1.2




