from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

@app.route('/', methods=['GET'])
def index():
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 100)
        session['attempts'] = 0
    return render_template('index.html', message="I'm thinking of a number between 1 and 100.", attempts=session['attempts'])

@app.route('/guess', methods=['POST'])
def guess():
    try:
        guess = int(request.form['guess'])
        if guess < 1 or guess > 100:
            return render_template('index.html', 
                                message="Please enter a number between 1 and 100!", 
                                attempts=session['attempts'])
        
        session['attempts'] += 1
        
        if guess < session['secret_number']:
            message = "Too low! Try a higher number."
        elif guess > session['secret_number']:
            message = "Too high! Try a lower number."
        else:
            message = f"🎉 Congratulations! You found the number {guess} in {session['attempts']} attempts!"
            return render_template('index.html', message=message, success=True, attempts=session['attempts'])
        
        return render_template('index.html', message=message, attempts=session['attempts'])
    except ValueError:
        return render_template('index.html', 
                             message="Please enter a valid number!", 
                             attempts=session['attempts'])

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('secret_number', None)
    session.pop('attempts', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

