import pygame
from logger import log_event

import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle)

            vel2 = self.velocity.rotate(-angle)
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0], self.position[1], self.radius)

            ast2 = Asteroid(self.position[0], self.position[1], self.radius)
            ast1.velocity = vel1 * 1.2
            ast2.velocity = vel2 * 1.2
