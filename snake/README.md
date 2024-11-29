# Snake Game 🐍 

A classic Snake game implemented as a web application using Python Flask for the backend and JavaScript for the game logic.

## Features

- Smooth snake movement with arrow key controls
- Score tracking system
- Food spawning system
- Pause functionality (Space bar)
- Responsive canvas-based gameplay
- Modern UI with retro-style fonts
- Wraparound walls (snake appears on opposite side)

## Technologies Used

- **Backend:**
  - Python 3.x
  - Flask 2.0.1
  - Gunicorn 20.1.0

- **Frontend:**
  - HTML5 Canvas
  - JavaScript (ES6+)
  - CSS3 with animations
  - Google Fonts (Press Start 2P)

## Project Structure

```
snake/
├── app.py              # Flask server
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── static/
│   └── game.js        # Game logic
└── templates/
    └── index.html     # Game interface
```

## How to Run

1. Navigate to the project directory
2. Start the Flask server:
   ```bash
   python app.py
   ```
3. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## Game Controls

- **Arrow Keys:** Control snake direction
- **Space Bar:** Pause/Resume game

## Game Rules

1. Use arrow keys to guide the snake
2. Eat food (red circles) to grow longer
3. Each food item adds 10 points to your score
4. Snake wraps around the screen edges
5. Game continues until you choose to stop

## Development

This project uses:
- Flask for serving the web application
- HTML5 Canvas for rendering the game
- JavaScript for game mechanics
- CSS for styling and animations
