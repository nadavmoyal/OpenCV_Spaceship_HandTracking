"""
Represents the main game engine that runs the spaceship game, handles input,
updates the game state, and manages game over and restart.

Attributes:
- game (Game): The Game object that contains the game's logic and data.

Methods:
- __init__(): Initializes the game engine and the Game object.
- run(): Main game loop that captures video, processes hand gestures,
         updates the game, and handles game over and restart logic.
- display_game_over(img): Displays the game over screen.
"""

import cv2
import cvzone
from Game import Game

ESC_KEY = 27
SPACE_KEY = 32

class GameEngine:
    def __init__(self):
        self.game = Game()

    def run(self):
        """
        Main game loop that:
        - Captures video frames and processes them.
        - Detects hands and updates the game state.
        - Displays the game frame with updated information.
        - Handles the game over screen and restart option.
        """
        while True:
            try:
                _, img = self.game.cap.read()
            except Exception as e:
                print(f"Error capturing video: {e}")
                break

            img = cv2.flip(img, 1)  # Flip the image horizontally for mirror effect
            hands, img = self.game.detector.findHands(img, flipType=False)  # Detect hands

            img = cv2.addWeighted(img, 0.8, self.game.imgBackground, 0.2, 0)  # Overlay background
            img = self.game.update(img, hands)  # Update game state

            cv2.imshow("Spaceship Game", img)  # Show the game frame
            key = cv2.waitKey(1)
            if key == ESC_KEY:  # ESC to exit
                self.game.game_over = True

            if self.game.game_over:  # Game over condition
                game_over_img = self.display_game_over(img)
                cv2.imshow("Spaceship Game", game_over_img)

                while True:
                    key = cv2.waitKey(1)
                    if key == SPACE_KEY:  # Space to restart
                        self.game.reset()
                        break
                    elif key == ESC_KEY:  # ESC to exit
                        self.game.cap.release()
                        cv2.destroyAllWindows()
                        return

    def display_game_over(self, img):
        """
        Displays the game over screen.
        """
        game_over_img = img.copy()
        cvzone.putTextRect(game_over_img, "Game Over", [300, 300],
                           scale=7, thickness=6, offset=20, colorR=(0, 0, 0))
        cvzone.putTextRect(game_over_img, f'Your Score: {self.game.total_score}', [200, 450],
                           scale=7, thickness=6, offset=20, colorR=(0, 0, 0))
        cvzone.putTextRect(game_over_img, f'Press SPACE to restart', [250, 600],
                           scale=4, thickness=6, offset=15, colorT=(000, 255, 000), colorR=(0, 0, 0))
        return game_over_img


if __name__ == "__main__":
    engine = GameEngine()
    engine.run()
