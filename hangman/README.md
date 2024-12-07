# Hangman Web Game

A modern, web-based version of the classic Hangman word guessing game built with Flask. This game features a clean, responsive design and an intuitive user interface.

## Features

- Classic Hangman gameplay
- Modern, responsive web interface
- Mobile-friendly design
- Session-based game state management
- Input validation and error handling
- Immediate feedback on guesses
- Random word selection from a curated list

## Requirements

- Python 3.x
- Flask 2.3.3
- Werkzeug 2.3.7

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd hangman
   ```

2. Install the required packages:
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

1. Click "Start New Game" to begin
2. Type a single letter and click "Guess" or press Enter
3. You have 6 attempts to guess the word correctly
4. The game shows which letters you've already guessed
5. Start a new game at any time by clicking the "New Game" button

## Project Structure

```
hangman/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css  # Game styling
└── templates/
    ├── index.html     # Welcome page
    └── game.html      # Game interface
```

## Development

The game is built with:
- **Flask**: Web framework
- **HTML5**: Structure
- **CSS3**: Styling with modern features
- **JavaScript**: Enhanced user interactions


