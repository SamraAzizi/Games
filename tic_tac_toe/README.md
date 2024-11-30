# Tic Tac Toe Web Game

A modern, responsive web-based implementation of the classic Tic Tac Toe game built with Flask and modern web technologies.

![Tic Tac Toe Game](game-preview.png)

## Features

- Clean and intuitive user interface
- Smooth animations and transitions
- Modern glassmorphism design
- Fully responsive for all devices
- Real-time game state updates
- Easy game reset functionality
- Win and tie detection
- Different colors for X and O

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Modern CSS with Flexbox and Grid
- **Fonts**: Google Fonts (Poppins)
- **Animations**: CSS Keyframes

## Prerequisites

- Python 3.6 or higher
- Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
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

1. The game starts with Player X
2. Players take turns clicking on empty cells to place their symbol (X or O)
3. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins
4. If all cells are filled and no player has won, the game is a tie
5. Click "New Game" to reset the board at any time

## Project Structure

```
tic-tac-toe/
│
├── app.py              # Flask application and game logic
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
│
└── templates/
    └── index.html     # Game interface and frontend logic
```

## Game Features

### Backend (app.py)
- Game state management
- Move validation
- Win condition checking
- API endpoints for game actions

### Frontend (index.html)
- Responsive grid layout
- Interactive game board
- Real-time updates
- Visual feedback
- Smooth animations
- Mobile-friendly design

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the classic Tic Tac Toe game
- Modern UI design principles
- Flask web framework
- The open-source community

## Future Improvements

- Add multiplayer support
- Implement AI opponent
- Add sound effects
- Save game statistics
- Add player names
- Create difficulty levels
- Add game history
- Implement user accounts

---

Made with ❤️ by [Your Name]
