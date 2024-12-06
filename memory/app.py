from flask import Flask, render_template, jsonify, request, session
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session

class MemoryGame:
    def __init__(self, size=4):
        self.size = size
        self.symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        # Fixed colors for each symbol
        self.symbol_colors = {
            'A': '#FF6B6B',  # Red
            'B': '#4ECDC4',  # Turquoise
            'C': '#45B7D1',  # Light Blue
            'D': '#96CEB4',  # Sage Green
            'E': '#FFEEAD',  # Light Yellow
            'F': '#D4A5A5',  # Dusty Rose
            'G': '#9B5DE5',  # Purple
            'H': '#F15BB5',  # Pink
            'I': '#00BBF9',  # Sky Blue
            'J': '#00F5D4',  # Mint
            'K': '#FEE440',  # Yellow
            'L': '#8AC926',  # Lime Green
            'M': '#FF99C8',  # Light Pink
            'N': '#FCF6BD',  # Light Yellow
            'O': '#A8E6CF',  # Mint Green
            'P': '#FFB3B3'   # Light Red
        }
        self.board = self.initialize_board()

    def initialize_board(self):
        num_pairs = self.size * self.size // 2
        pairs = random.sample(self.symbols, num_pairs) * 2
        random.shuffle(pairs)
        board = [[None] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                symbol = pairs.pop()
                board[i][j] = {
                    'symbol': symbol,
                    'color': self.symbol_colors[symbol],
                    'revealed': False,
                    'matched': False
                }
        return board

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game')
def new_game():
    print("Starting new game")
    game = MemoryGame()
    session['board'] = [[{
        'symbol': cell['symbol'],
        'color': cell['color'],
        'revealed': cell['revealed'],
        'matched': cell['matched']
    } for cell in row] for row in game.board]
    session['first_click'] = None
    print("Board initialized:", session['board'])
    return jsonify({'status': 'success'})

@app.route('/reveal', methods=['POST'])
def reveal():
    data = request.json
    row, col = data['row'], data['col']
    print(f"Revealing card at position ({row}, {col})")
    
    if 'board' not in session:
        print("No board in session, starting new game")
        return jsonify({'status': 'invalid'})
    
    board = session['board']
    first_click = session.get('first_click')
    
    # Don't allow revealing already matched cards
    if board[row][col]['matched']:
        print(f"Card at ({row}, {col}) is already matched")
        return jsonify({'status': 'invalid'})
    
    # Create current card info
    current_card = {
        'symbol': board[row][col]['symbol'],
        'color': board[row][col]['color'],
        'row': row,
        'col': col
    }
    
    if first_click is None:
        # First card of the pair
        session['first_click'] = (row, col)
        board[row][col]['revealed'] = True
        print(f"First card revealed: {current_card}")
        result = {
            'status': 'first_click',
            'cell': current_card
        }
    else:
        prev_row, prev_col = first_click
        print(f"Second card revealed. Comparing with first card at ({prev_row}, {prev_col})")
        
        # Don't allow clicking the same card twice
        if prev_row == row and prev_col == col:
            print("Same card clicked twice")
            return jsonify({'status': 'invalid'})
        
        # Compare the two cards
        if board[prev_row][prev_col]['symbol'] == board[row][col]['symbol']:
            print("Match found!")
            board[prev_row][prev_col]['matched'] = True
            board[row][col]['matched'] = True
            board[row][col]['revealed'] = True
            result = {
                'status': 'match',
                'cell': current_card,
                'prev_cell': {
                    'symbol': board[prev_row][prev_col]['symbol'],
                    'color': board[prev_row][prev_col]['color'],
                    'row': prev_row,
                    'col': prev_col
                }
            }
        else:
            print("No match")
            # For no match, we'll reveal the second card temporarily
            board[row][col]['revealed'] = True
            result = {
                'status': 'no_match',
                'cell': current_card,
                'prev_cell': {
                    'symbol': board[prev_row][prev_col]['symbol'],
                    'color': board[prev_row][prev_col]['color'],
                    'row': prev_row,
                    'col': prev_col
                }
            }
            # Reset revealed state for both cards
            board[prev_row][prev_col]['revealed'] = False
            board[row][col]['revealed'] = False
        
        session['first_click'] = None
    
    session['board'] = board
    print(f"Updated session. Result: {result}")
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True)
