#  Rock Paper Scissors Web Game

A cute and interactive web-based implementation of the classic Rock Paper Scissors game built with Flask. Play against the computer in a beautifully designed interface!

##  Features

-  Simple and intuitive user interface
-  Cute design with animations and emojis
-  Play against a computer opponent
-  Responsive design - works on both desktop and mobile
-  Smooth animations and visual feedback
-  Instant results display

##  Getting Started

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system. You can check your Python version by running:
```bash
python --version
```

### Installation

1. Clone the repository or download the files:
```bash
git clone https://github.com/yourusername/rock_paper_scissors.git
cd rock_paper_scissors
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required dependencies:
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

##  How to Play

1. Open the game in your web browser
2. Choose your move by clicking one of three buttons:
   -  Rock
   -  Paper
   -  Scissors
3. The computer will make its choice
4. The result will be displayed immediately with a nice animation
5. Play again as many times as you want!

##  Game Rules

-  Rock beats Scissors
-  Scissors beats  Paper
-  Paper beats  Rock
- If both players choose the same option, it's a tie!

##  Technical Details

### Project Structure
```
rock_paper_scissors/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── templates/
    └── index.html     # Game interface
```

### Technologies Used

- **Backend:**
  - Flask 2.3.3 - Python web framework
  - Werkzeug 2.3.7 - WSGI web application library

- **Frontend:**
  - HTML5
  - CSS3 (with animations)
  - JavaScript (Fetch API)
  - Google Fonts (Comic Neue)


