"""
Represents the game logic, including asteroid movement, spaceship control,
collision detection, and score tracking.

Attributes:
- imgBackground (numpy.ndarray): Background image of the game.
- asteroid_img (numpy.ndarray): Image of the asteroid.
- spaceship_img (numpy.ndarray): Image of the spaceship.
- cap (cv2.VideoCapture): Capture object for video input from the camera.
- screen_width (int): Width of the screen.
- screen_height (int): Height of the screen.
- game_over (bool): A flag to indicate if the game is over.
- detector (HandDetector): Hand detection object for tracking hand gestures.
- start_time (float): The time when the game started.
- total_score (int): The player's score.
- asteroids (list): List of Asteroid objects representing the obstacles in the game.
- spaceship (Spaceship): The Spaceship object controlled by the player.

Methods:
- __init__(): Initializes the game, loads assets, and sets up the camera.
- generate_asteroid_pos(): Generates a random position for the asteroid on the screen.
- generate_asteroid_speed(): Generates a random speed for the asteroid.
- check_collision(): Checks for a collision between the spaceship and any asteroid.
- reset(): Resets the game, including the score, asteroids, and other parameters.
- update(): Updates the game state, including hand tracking, spaceship movement,
  asteroid movement, and collision detection.
"""
import os
import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
import time
from Asteroid import Asteroid
from Spaceship import Spaceship
import screeninfo
import random

class Game:
    def __init__(self):
        """
        Initializes the game, loads assets, and sets up the camera.
        """
        # # Assets (images)
        self.imgBackground = cv2.imread("Background.png")
        self.asteroid_img = cv2.imread("Asteroid_img.png", cv2.IMREAD_UNCHANGED)
        self.spaceship_img = cv2.imread("spaceship_img.png", cv2.IMREAD_UNCHANGED)

        # def resource_path(relative_path):
        #     """Returns the absolute path to the resource, works for dev and for PyInstaller."""
        #     try:
        #         # PyInstaller creates a temporary folder and stores path in _MEIPASS
        #         base_path = sys._MEIPASS
        #     except Exception:
        #         base_path = os.path.abspath(".")
        #     return os.path.join(base_path, relative_path)
        #
        # self.imgBackground = cv2.imread(resource_path("Background.png"))
        # self.asteroid_img = cv2.imread(resource_path("Asteroid_img.png"), cv2.IMREAD_UNCHANGED)
        # self.spaceship_img = cv2.imread(resource_path("spaceship_img.png"), cv2.IMREAD_UNCHANGED)

        # Video capture settings
        self.cap = cv2.VideoCapture(0)
        screen = screeninfo.get_monitors()[0]
        self.screen_width, self.screen_height = screen.width, screen.height
        self.cap.set(3, self.screen_width)
        self.cap.set(4, self.screen_height)
        cv2.namedWindow("Spaceship Game", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Spaceship Game", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Game variables
        self.game_over = False
        self.start_time = time.time()
        self.total_score = 0

        # Random generation parameters
        self.min_pos = 0.35
        self.max_pos = 0.55

        # Collision detection parameters
        self.spaceship_collision_offset = 80  # The offset of the spaceship from the asteroid
        self.collision_threshold = 50  # The threshold range for collision detection

        # Hand detection and spaceship control
        self.detector = HandDetector(detectionCon=0.8, maxHands=1)

        # Create asteroid and spaceship objects
        self.asteroids = [
            Asteroid(self.generate_asteroid_pos(), self.generate_asteroid_speed(min_speed=10, max_speed=20),
                     self.asteroid_img)
            for _ in range(4)
        ]
        self.spaceship = Spaceship(self.spaceship_img)

    def generate_asteroid_pos(self):
        """
        Generates a random position for the asteroid within the game screen.
        Returns: list: [x, y] representing the asteroid's position.
        """
        x = random.randint(int(self.screen_width * self.min_pos), int(self.screen_width * self.max_pos))
        y = random.randint(int(self.screen_height * self.min_pos), int(self.screen_height * self.max_pos))
        return [x, y]

    @staticmethod
    def generate_asteroid_speed(min_speed=10, max_speed=20):
        """
        Generates random asteroid speeds along both axes.
        Returns:
            list: [speed_x, speed_y] representing the asteroid's movement speed.
        """
        return [random.randint(min_speed, max_speed), random.randint(min_speed, max_speed)]

    def check_collision(self):
        """
        Checks for a collision between the spaceship and any asteroid.
        Returns: bool: True if a collision is detected, False otherwise.
        """
        for asteroid in self.asteroids:
            ax, ay = asteroid.pos
            # Check if the distance between the spaceship and the asteroid is smaller than the defined thresholds
            if (abs(ax - (self.spaceship.x + self.spaceship_collision_offset)) < self.collision_threshold and
                    abs(ay - self.spaceship.y) < self.collision_threshold):
                return True
        return False

    def reset(self):
        """
        Resets the game, including the score, asteroids, and other parameters.
        """
        self.game_over = False
        self.start_time = time.time()
        self.total_score = 0
        self.asteroids = [
            Asteroid(self.generate_asteroid_pos(), self.generate_asteroid_speed(min_speed=10,max_speed=20), self.asteroid_img)
            for _ in range(4)
        ]

    def update(self, img, hands):
        """
        Updates the game state, including hand tracking, spaceship movement,
        asteroid movement, and collision detection.
        Args:
            img (numpy.ndarray): The current frame of the game.
            hands (list): A list of detected hand objects, if any.
        Returns:
            numpy.ndarray: The updated image after applying changes.
        """
        if hands:
            for hand in hands:
                self.spaceship.update_position(hand,self.screen_height)
                img = self.spaceship.draw(img)
                if self.check_collision():
                    self.game_over = True
                    self.total_score = int(round(time.time() - self.start_time, 2) * 17.5)

        for asteroid in self.asteroids:
            asteroid.move(self.screen_width,self.screen_height)
            img = asteroid.draw(img)

        return img
