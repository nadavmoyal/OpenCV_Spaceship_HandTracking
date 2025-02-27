![image](https://github.com/user-attachments/assets/0c58de66-6f10-4b1b-8ee1-b16ca328fdc2)

# Spaceship Hand Tracking Game

## Description

The Spaceship Game is an interactive game where the player controls a spaceship using hand gestures. The objective is to avoid asteroids while navigating the spaceship on the screen. The game combines computer vision for hand tracking and implements asteroid movement with collision detection.

## Code Structure

### Key Classes:

- **Asteroid**: Represents asteroids that move around and bounce off screen edges.  
  - Methods: `move()`, `draw()`
  
- **Spaceship**: The player's spaceship follows hand movements detected by the `HandDetector`.  
  - Methods: `update_position()`, `draw()`

- **GameEngine**: Manages game logic, asteroid movement, spaceship control, collision detection, and score tracking.  
  - Methods: `update()`, `check_collision()`, `reset()`

- **Main**: Runs the main game loop, captures video frames, processes hand gestures, and manages the game state.  
  - Methods: `run()`

## How it Works:

1. **Hand Tracking**: The game uses a hand tracking model to control the spaceship's movement.
2. **Asteroids**: The asteroids are placed in random positions and given a random speed. They move at a fixed angle and change direction when they hit the edges of the screen.
3. **Collision Detection**: The game checks if the spaceship collides with an asteroid and ends if so.
4. **Restart Option**: Press the SPACE key after the game ends to restart.

## Required Libraries

- **cvzone**: Hand detection and tracking.
- **screeninfo**: To get screen resolution and manage window size.
- **numpy**: For mathematical operations.
- **mediapipe**: For hand tracking and image processing.

### Installation

To install the required libraries, run:
```bash
pip install cvzone screeninfo numpy mediapipe
```

## How to Run

1. Clone the repository.
2. Install the required libraries.
3. Run the `Main.py` file to start the game.

Alternatively, you can skip the installation and download the EXE file to start the game directly!
## How to Play

- Stand about 1 meter from the screen.
- Left-handed? Use your index finger. Right-handed? Use your pinky finger.
- Avoid asteroids and try to survive as long as possible!

## Download the EXE File

Skip the installation and download the **EXE** file directly:

[Download EXE](https://www.dropbox.com/scl/fi/k6bkgnbdpeojii88nh4q0/Spaceship-Game-v3.exe?rlkey=977gi1vu8krx1ytts2o3lomq1&st=30xoorkc&dl=0)

Enjoy the game, and challenge your friends to beat your score!

## Gameplay Video

Watch the gameplay in action:


https://github.com/user-attachments/assets/3800834f-04e9-4d15-8bee-f7a08e49c03b


