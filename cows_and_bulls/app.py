from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key in production

def generate_number():
    # Generate a 4-digit number with unique digits
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def check_guess(secret_number, guess):
    bulls = 0  # Correct digit in correct position
    cows = 0   # Correct digit in wrong position
    
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
            
    return {'bulls': bulls, 'cows': cows}

@app.route('/')
def index():
    if 'secret_number' not in session:
        session['secret_number'] = generate_number()
        session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.json.get('guess', '')
    
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
        return jsonify({'error': 'Please enter a 4-digit number with unique digits'}), 400
    
    session['attempts'] = session.get('attempts', 0) + 1
    result = check_guess(session['secret_number'], guess)
    
    if result['bulls'] == 4:
        response = {
            'message': f'Congratulations! You won in {session["attempts"]} attempts!',
            'won': True,
            **result
        }
        session.pop('secret_number', None)
        session.pop('attempts', None)
    else:
        response = {
            'message': f'{result["bulls"]} bulls and {result["cows"]} cows',
            'won': False,
            **result
        }
    
    return jsonify(response)

@app.route('/new-game', methods=['POST'])
def new_game():
    session['secret_number'] = generate_number()
    session['attempts'] = 0
    return jsonify({'message': 'New game started'})

if __name__ == '__main__':
    app.run(debug=True)
