from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pear", "strawberry", "blueberry", 
             "kiwi", "pineapple", "watermelon", "computer", "programming", "keyboard", 
             "elephant", "universe", "basketball", "skyscraper", "adventure", "guitar", 
             "butterfly"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game')
def new_game():
    session['secret_word'] = choose_word()
    session['guessed_letters'] = []
    session['attempts'] = 6
    session['game_over'] = False
    session['message'] = 'Welcome to Hangman!'
    return redirect(url_for('game'))

@app.route('/game')
def game():
    if 'secret_word' not in session:
        return redirect(url_for('new_game'))
    
    displayed_word = display_word(session['secret_word'], session['guessed_letters'])
    return render_template('game.html', 
                         displayed_word=displayed_word,
                         attempts=session['attempts'],
                         guessed_letters=', '.join(sorted(session['guessed_letters'])),
                         message=session.get('message', ''),
                         game_over=session['game_over'])

@app.route('/guess', methods=['POST'])
def guess():
    if 'secret_word' not in session or session['game_over']:
        return redirect(url_for('new_game'))

    guess = request.form.get('guess', '').lower()
    
    if not guess.isalpha() or len(guess) != 1:
        session['message'] = 'Please enter a single letter!'
        return redirect(url_for('game'))

    if guess in session['guessed_letters']:
        session['message'] = 'You already guessed that letter!'
        return redirect(url_for('game'))

    session['guessed_letters'].append(guess)

    if guess in session['secret_word']:
        session['message'] = 'Correct guess!'
        if all(letter in session['guessed_letters'] for letter in session['secret_word']):
            session['message'] = f'Congratulations! You won! The word was: {session["secret_word"]}'
            session['game_over'] = True
    else:
        session['attempts'] -= 1
        session['message'] = 'Wrong guess!'
        if session['attempts'] == 0:
            session['message'] = f'Game Over! The word was: {session["secret_word"]}'
            session['game_over'] = True

    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True)
