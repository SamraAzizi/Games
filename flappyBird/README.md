# Flappy Bird Web Game

A modern web-based implementation of the classic Flappy Bird game using Flask and HTML5 Canvas.



## Features

- Smooth, responsive gameplay
- Modern visual design with gradients and animations
- Score tracking
- Instant restart functionality
- Mobile-friendly controls
- Consistent game difficulty
- Animated bird character with rotation
- Beautifully styled pipes with caps and gradients

## Technologies Used

- **Backend:**
  - Python 3.x
  - Flask 3.0.0
  - Werkzeug 3.0.1

- **Frontend:**
  - HTML5 Canvas
  - JavaScript (ES6+)
  - CSS3 with modern features (Flexbox, Gradients)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flappyBird
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

- Press the **Space bar** or **Up Arrow** key to make the bird fly
- Click or tap the screen (for mobile devices)
- Navigate through the pipes without hitting them
- Don't hit the ground!
- Try to achieve the highest score possible
- When game over, press any key or click to restart

## Game Controls

| Action | Control |
|--------|---------|
| Flap Wings | Space / Up Arrow / Click |
| Start Game | Space / Up Arrow / Click |
| Restart Game | Space / Up Arrow / Click (after game over) |

## Project Structure

```
flappyBird/
├── app.py              # Flask application main file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── assets/            # Game assets directory
│   ├── sprites/       # Image assets
│   └── game.js        # Game logic
└── templates/         # HTML templates
    └── index.html     # Main game page
```

## Game Mechanics

- Bird automatically falls due to gravity
- Each successful pipe passage scores one point
- Collision with pipes or ground ends the game
- Bird rotates based on movement for realistic animation
- Pipes maintain consistent gaps for fair gameplay
- Score is prominently displayed during gameplay

## Technical Details

### Bird Physics
- Gravity constant: 0.25
- Flap speed: -4.6
- Maximum velocity: 10
- Rotation range: -25° to 90°

### Pipe Generation
- Consistent gap size: 120px
- Minimum height: 50px
- Speed: 2px per frame
- Width: 52px
- Spawn interval: Every 100 frames

