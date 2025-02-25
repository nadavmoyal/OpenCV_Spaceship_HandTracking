"""
Represents an asteroid that moves on the screen and bounces off edges.

Attributes:
- pos (list[int]): Current (x, y) position.
- speed (list[int]): Movement speed in x and y directions.
- img: The asteroid's image.

Methods:
- move(screen_width, screen_height): Moves the asteroid and handles bouncing off screen edges.
- draw(img): Overlays the asteroid on the given background image and returns the updated image.
"""

import cvzone
from typing import List

BOUNDARY_MARGIN = 0.36  # Class-level constant

class Asteroid:
    def __init__(self, pos: List[int], speed: List[int], img):
        """
        Initializes an asteroid.
        :param pos: The (x, y) position of the asteroid.
        :param speed: The speed of the asteroid in both x and y directions.
        :param img: The asteroid's image.
        """
        self.pos = pos
        self.speed = speed
        self.img = img

    def move(self, screen_width: int, screen_height: int):
        """
         Moves the asteroid and bounces it off the screen edges.
         :param screen_width: Width of the screen.
         :param screen_height: Height of the screen.
         """
        margin_x = screen_width * BOUNDARY_MARGIN
        margin_y = screen_height * BOUNDARY_MARGIN

        if self.pos[1] >= screen_height - margin_y or self.pos[1] <= 0:
            self.speed[1] = -self.speed[1]  # Reverse vertical speed

        if self.pos[0] >= screen_width - margin_x or self.pos[0] <= 0:
            self.speed[0] = -self.speed[0]  # Reverse horizontal speed

        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    def draw(self, img):
        """
        Overlays the asteroid image onto the given background image.

        :param img: The background image.
        :return: The updated image with the asteroid.
        """
        return cvzone.overlayPNG(img, self.img, self.pos)