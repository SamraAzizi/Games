from flask import Flask, render_template, jsonify, session, request
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

class MinesweeperGame:
    def __init__(self, rows=12, cols=12, num_mines=35):  # Increased from 20 to 35 mines
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0] * cols for _ in range(rows)]
        self.mines = []  # Changed from set to list
        self.revealed = [[False] * cols for _ in range(rows)]
        self.game_over = False
        
        self.place_mines()
        self.calculate_numbers()
    
    def place_mines(self):
        while len(self.mines) < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            mine_pos = (row, col)
            if mine_pos not in self.mines:  # Check if mine position is unique
                self.mines.append(mine_pos)
    
    def calculate_numbers(self):
        for row, col in self.mines:
            self.board[row][col] = -1  # -1 represents a mine
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (0 <= i < self.rows and 0 <= j < self.cols and 
                        self.board[i][j] != -1):
                        self.board[i][j] += 1
    
    def reveal(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return False
        
        if self.revealed[row][col]:
            return False
            
        self.revealed[row][col] = True
        
        if (row, col) in self.mines:
            self.game_over = True
            return True
            
        if self.board[row][col] == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (0 <= i < self.rows and 0 <= j < self.cols and 
                        not self.revealed[i][j]):
                        self.reveal(i, j)
        
        return True
    
    def get_game_state(self):
        visible_board = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if self.revealed[i][j]:
                    if (i, j) in self.mines:
                        row.append('*')
                    else:
                        row.append(str(self.board[i][j]) if self.board[i][j] > 0 else '')
                else:
                    row.append('')
            visible_board.append(row)
        
        return {
            'board': visible_board,
            'gameOver': self.game_over,
            'rows': self.rows,
            'cols': self.cols
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-game')
def new_game():
    game = MinesweeperGame()
    session['game'] = game.__dict__
    return jsonify(game.get_game_state())

@app.route('/click', methods=['POST'])
def click():
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    
    game_dict = session.get('game')
    if not game_dict:
        return jsonify({'error': 'No game in progress'}), 400
    
    game = MinesweeperGame()
    # Properly restore game state
    game.rows = game_dict['rows']
    game.cols = game_dict['cols']
    game.num_mines = game_dict['num_mines']
    game.board = game_dict['board']
    game.mines = game_dict['mines']
    game.revealed = game_dict['revealed']
    game.game_over = game_dict['game_over']
    
    game.reveal(row, col)
    session['game'] = game.__dict__
    
    return jsonify(game.get_game_state())

if __name__ == '__main__':
    app.run(debug=True)
