#  Flask Minesweeper

A modern, web-based implementation of the classic Minesweeper game built with Flask and JavaScript. This version features a clean, responsive design and smooth animations for an enhanced gaming experience.

![Minesweeper Game](https://raw.githubusercontent.com/username/minesweeper/main/screenshots/game.png)

##  Features

-  Classic Minesweeper gameplay
-  Responsive design that works on both desktop and mobile
-  Modern UI with smooth animations
-  Left-click to reveal cells
-  Dynamic mine placement
-  Numerical hints showing adjacent mines
-  Quick restart with "New Game" button
-  Color-coded numbers for better visibility

##  Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/username/minesweeper.git
cd minesweeper
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and navigate to:
```
http://localhost:5000
```

## 🎮 How to Play

1. **Starting the Game**
   - Click any cell to start
   - The first click is always safe
   - Numbers reveal how many mines are adjacent to each cell

2. **Game Rules**
   - Each number shows how many mines are in the adjacent cells
   - Left-click to reveal a cell
   - If you reveal a mine, the game is over
   - To win, reveal all cells except the mines

3. **Number Colors**
   - 1 (Blue): One adjacent mine
   - 2 (Green): Two adjacent mines
   - 3 (Red): Three adjacent mines
   - 4 (Purple): Four adjacent mines
   - 5 (Orange): Five adjacent mines
   - 6 (Teal): Six adjacent mines
   - 7 (Black): Seven adjacent mines
   - 8 (Gray): Eight adjacent mines

##  Technical Details

### Project Structure
```
minesweeper/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Documentation
└── templates/
    └── index.html     # Game interface
```

### Technologies Used

- **Backend**
  - Flask 2.3.3: Web framework
  - Flask-Session 0.5.0: Session management
  - Python 3.8+: Programming language

- **Frontend**
  - HTML5: Structure
  - CSS3: Styling with modern features
  - JavaScript: Game logic and interactions
  - Google Fonts (Roboto): Typography

### Game Configuration

The default game settings are:
- Grid Size: 12x12
- Number of Mines: 20
- These can be modified in `app.py`

## 🔧 Customization

### Modifying Grid Size
In `app.py`, update the initialization parameters:
```python
game = MinesweeperGame(rows=12, cols=12, num_mines=20)
```

### Changing Colors
In `templates/index.html`, modify the CSS variables:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    /* ... other color variables ... */
}
```

