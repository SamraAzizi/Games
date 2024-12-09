from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Configure static folder for assets
app.static_folder = 'assets'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game_state', methods=['POST'])
def update_game_state():
    # Handle game state updates from client
    data = request.get_json()
    # Process game state here if needed
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
