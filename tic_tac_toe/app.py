from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize game state
board = [" "] * 9
current_player = "X"
game_mode = "ai"  # Default to AI mode

def check_winner(board):
    # Define winning combinations
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for line in lines:
        if board[line[0]] != " " and board[line[0]] == board[line[1]] == board[line[2]]:
            return board[line[0]]
    return None

def is_board_full(board):
    return " " not in board

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == " "]

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_board_full(board):
        return 0
    
    empty_cells = get_empty_cells(board)
    
    if is_maximizing:
        best_score = float('-inf')
        for pos in empty_cells:
            board[pos] = "O"
            score = minimax(board, depth + 1, False)
            board[pos] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for pos in empty_cells:
            board[pos] = "X"
            score = minimax(board, depth + 1, True)
            board[pos] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    empty_cells = get_empty_cells(board)
    
    # If it's the first move, randomly choose a position for variety
    if len(empty_cells) == 9:
        return random.choice(empty_cells)
    
    best_score = float('-inf')
    best_move = None
    
    for pos in empty_cells:
        board[pos] = "O"
        score = minimax(board, 0, False)
        board[pos] = " "
        
        if score > best_score:
            best_score = score
            best_move = pos
    
    return best_move

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_mode', methods=['POST'])
def set_mode():
    global game_mode, board, current_player
    game_mode = request.json['mode']
    board = [" "] * 9
    current_player = "X"
    return jsonify({'status': 'success', 'mode': game_mode})

@app.route('/move', methods=['POST'])
def move():
    global current_player, board
    
    position = request.json['position']
    
    # Check if the move is valid
    if position < 0 or position > 8 or board[position] != " ":
        return jsonify({'error': 'Invalid move'})
    
    # Make player's move
    board[position] = current_player
    
    # Check for winner after player's move
    winner = check_winner(board)
    if winner:
        return jsonify({
            'status': 'win',
            'winner': winner,
            'board': board
        })
    
    # Check for tie
    if is_board_full(board):
        return jsonify({
            'status': 'tie',
            'board': board
        })
    
    # If in AI mode and it's O's turn, make AI move
    if game_mode == "ai" and current_player == "X":
        current_player = "O"
        ai_position = get_best_move(board)
        board[ai_position] = current_player
        
        # Check for winner after AI's move
        winner = check_winner(board)
        if winner:
            return jsonify({
                'status': 'win',
                'winner': winner,
                'board': board
            })
        
        # Check for tie after AI's move
        if is_board_full(board):
            return jsonify({
                'status': 'tie',
                'board': board
            })
    
    # Switch players
    current_player = "X"
    
    return jsonify({
        'status': 'ongoing',
        'board': board,
        'current_player': current_player
    })

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board = [" "] * 9
    current_player = "X"
    return jsonify({'board': board, 'current_player': current_player})

if __name__ == '__main__':
    app.run(debug=True)
