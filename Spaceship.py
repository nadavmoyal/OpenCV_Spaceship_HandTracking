"""
Represents a spaceship that follows the user's hand using hand recognition.

Attributes:
- img: The spaceship's image.
- x: The current x position of the spaceship.
- y: The current y position of the spaceship.

Methods:
- update_position(hand_position): Updates the position of the spaceship based on the hand position.
- draw(img): Overlays the spaceship on the given background image and returns the updated image.
"""

import cvzone
import numpy as np

class Spaceship:
    def __init__(self,img) -> None:
        """
        Initializes the spaceship.
        :param img: The image of the spaceship.
        """
        self.img = img
        self.x = 0
        self.y = 0

    def update_position(self,hand_position,screen_height: float)-> None:
        """
        Updates the spaceship's position based on the hand's position.
        :param screen_height:
        :param hand_position: The position of the hand, a dictionary containing the bounding box of the hand (x, y, width, height).
        """
        # bbox: The bounding box of the hand, used to update the spaceship's position based on the hand's coordinates.
        x, y, w, h = hand_position['bbox']
        h1, w1, _ = self.img.shape
        y1 = y - h1 // 2  # Adjust the spaceship's y position to center it on the hand's y position
        self.y = np.clip(y1, 0, screen_height)  # Constrain the y position to a valid range
        self.x = x  # Update the x position based on the hand's x position

    def draw(self, img):
        """
        Overlays the spaceship image onto the given background image.
        :param img: The background image.
        :return: The updated image with the spaceship.
        """
        return cvzone.overlayPNG(img, self.img, (self.x, self.y))