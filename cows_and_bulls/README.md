# Cows and Bulls Web Game

A modern web implementation of the classic "Cows and Bulls" number guessing game built with Flask. This game features a beautiful, responsive UI with animations and an intuitive user experience.

## Game Overview

Cows and Bulls is a number guessing game where you need to guess a 4-digit number with unique digits. After each guess, you receive feedback in the form of:
- **Bulls**: Correct digits in correct positions
- **Cows**: Correct digits in wrong positions

## Features

- Modern, responsive UI with smooth animations
- Automatic game state management
- Mobile-friendly design
- Real-time feedback
- Guess history tracking
- Win celebration animations

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cows-and-bulls.git
   cd cows-and-bulls
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

1. When you start the game, a random 4-digit number with unique digits is generated
2. Enter your guess in the input field (must be 4 unique digits)
3. Click "Make Guess" or press Enter to submit your guess
4. You'll receive feedback showing:
   - Number of Bulls (correct digits in correct positions)
   - Number of Cows (correct digits in wrong positions)
5. Use the feedback to refine your next guess
6. Keep guessing until you find the correct number
7. Click "New Game" at any time to start over

## Technical Details

### Project Structure
```
cows_and_bulls/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styles
└── templates/
    └── index.html     # Main game interface
```

### Technologies Used

- **Backend**:
  - Flask 3.0.0
  - Werkzeug 3.0.1
  - Python's random module for number generation

- **Frontend**:
  - HTML5
  - CSS3 with modern features (Grid, Flexbox, Animations)
  - JavaScript (ES6+)
  - Google Fonts (Poppins)

### Key Features Implementation

- **Session Management**: Game state is maintained using Flask sessions
- **Input Validation**: Client and server-side validation for guess inputs
- **Responsive Design**: Mobile-first approach with CSS media queries
- **Animations**: CSS keyframes for smooth transitions and feedback
- **Error Handling**: Comprehensive error checking and user feedback
