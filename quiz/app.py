from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
from questions import questions
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key in production

@app.route('/')
def index():
    session['score'] = 0
    session['current_question'] = 0
    session['questions_order'] = list(range(len(questions)))
    random.shuffle(session['questions_order'])
    session['answered_questions'] = []
    return render_template('index.html')

@app.route('/question')
def get_question():
    current_question = session.get('current_question', 0)
    questions_order = session.get('questions_order', [])
    
    if current_question >= len(questions):
        return jsonify({
            'finished': True,
            'score': session.get('score', 0),
            'total': len(questions),
            'answered_questions': session.get('answered_questions', [])
        })
    
    question_index = questions_order[current_question]
    question_data = questions[question_index].copy()  # Create a copy to not modify original
    
    # Shuffle the options
    options = question_data['options'].copy()
    random.shuffle(options)
    question_data['options'] = options
    
    return jsonify({
        'finished': False,
        'question': question_data['question'],
        'options': question_data['options'],
        'category': question_data['category'],
        'current_question': current_question + 1,
        'total_questions': len(questions)
    })

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    current_question = session.get('current_question', 0)
    questions_order = session.get('questions_order', [])
    selected_answer = data.get('answer')
    
    if current_question >= len(questions):
        return jsonify({'error': 'Quiz already finished'})
    
    question_index = questions_order[current_question]
    correct_answer = questions[question_index]['answer']
    is_correct = selected_answer == correct_answer
    
    # Store question result
    question_result = {
        'question': questions[question_index]['question'],
        'category': questions[question_index]['category'],
        'your_answer': selected_answer,
        'correct_answer': correct_answer,
        'is_correct': is_correct
    }
    
    answered_questions = session.get('answered_questions', [])
    answered_questions.append(question_result)
    session['answered_questions'] = answered_questions
    
    if is_correct:
        session['score'] = session.get('score', 0) + 1
    
    session['current_question'] = current_question + 1
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': correct_answer,
        'score': session.get('score', 0)
    })

if __name__ == '__main__':
    app.run(debug=True)

