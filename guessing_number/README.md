# Number Guessing Game 

A modern, web-based number guessing game built with Flask. This interactive game challenges players to guess a randomly generated number between 1 and 100, providing feedback to help them find the correct answer.

## Features

- **Modern Web Interface**: Clean and responsive design that works on all devices
- **Interactive Gameplay**: Real-time feedback on each guess
- **Session Management**: Keeps track of game state and attempts
- **Error Handling**: Graceful handling of invalid inputs
- **Animations**: Smooth transitions and visual feedback
- **Mobile-Friendly**: Responsive design that adapts to screen size

## Technologies Used

- **Backend**: Python 3.x with Flask 3.0.0
- **Frontend**: HTML5, CSS3
- **Dependencies**: See requirements.txt

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd guessing_number
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

1. When you start the game, the computer will randomly select a number between 1 and 100
2. Enter your guess in the input field
3. Click "Submit Guess" or press Enter
4. The game will tell you if your guess is:
   - Too high
   - Too low
   - Correct!
5. Keep guessing until you find the correct number
6. Click "Start New Game" to play again

## Game Rules

- You can only enter numbers between 1 and 100
- Each guess counts as an attempt
- The game keeps track of how many attempts you make
- You can start a new game at any time

## Project Structure

```
guessing_number/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
│
├── static/
│   └── styles.css     # CSS styling
│
└── templates/
    └── index.html     # Game interface template
```

## Customization

You can customize the game by:
1. Modifying the CSS in `static/styles.css` to change the appearance
2. Adjusting the number range in `app.py`
3. Adding new features like:
   - Different difficulty levels
   - High score tracking
   - Multiple players

## Troubleshooting

- If the server doesn't start, make sure no other application is using port 5000
- If styles don't load, clear your browser cache
- For any Python errors, ensure all dependencies are correctly installed
