from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Game state
games = {}

def create_initial_state():
    return {
        'ball': {
            'x': 400,
            'y': 300,
            'dx': 3 * random.choice([1, -1]),
            'dy': 3 * random.choice([1, -1])
        },
        'paddles': {'left': 300, 'right': 300},
        'scores': {'left': 0, 'right': 0},
        'powerUp': {'active': False, 'x': 0, 'y': 0, 'type': None},
        'paddleSizes': {'left': 90, 'right': 90},
        'gameOver': False,
        'winner': None
    }

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('join_game')
def handle_join(data):
    game_id = data.get('game_id', 'default')
    if game_id not in games:
        games[game_id] = create_initial_state()
    print(f'Player joined game: {game_id}')
    emit('game_state', games[game_id])

@socketio.on('paddle_move')
def handle_paddle_move(data):
    game_id = data.get('game_id', 'default')
    paddle = data['paddle']
    position = data['position']
    if game_id in games:
        games[game_id]['paddles'][paddle] = position
        emit('game_state', games[game_id], broadcast=True)

@socketio.on('reset_game')
def handle_reset(data):
    game_id = data.get('game_id', 'default')
    if game_id in games:
        print('Resetting game')
        games[game_id] = create_initial_state()
        emit('game_state', games[game_id], broadcast=True)

@socketio.on('update_ball')
def handle_ball_update(data):
    game_id = data.get('game_id', 'default')
    if game_id in games:
        games[game_id].update({
            'ball': data['ball'],
            'scores': data['scores'],
            'powerUp': data.get('powerUp', {'active': False, 'x': 0, 'y': 0, 'type': None}),
            'paddleSizes': data.get('paddleSizes', {'left': 90, 'right': 90}),
            'gameOver': data.get('gameOver', False),
            'winner': data.get('winner', None)
        })
        emit('game_state', games[game_id], broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
