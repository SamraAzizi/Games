
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize game state
board = [" "] * 9  # Use a flat list for simplicity
current_player = "X"

def check_winner():
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global current_player, board
    
    position = request.json['position']
    
    # Check if the move is valid
    if position < 0 or position > 8 or board[position] != " ":
        return jsonify({'error': 'Invalid move'})
    
    # Make the move
    board[position] = current_player
    
    # Check for winner
    winner = check_winner()
    if winner:
        response = {'status': 'win', 'winner': winner, 'board': board}
        board = [" "] * 9  # Reset board
        current_player = "X"  # Reset player
        return jsonify(response)
    
    # Check for tie
    if " " not in board:
        response = {'status': 'tie', 'board': board}
        board = [" "] * 9  # Reset board
        current_player = "X"  # Reset player
        return jsonify(response)
    
    # Switch players
    current_player = "O" if current_player == "X" else "X"
    
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
