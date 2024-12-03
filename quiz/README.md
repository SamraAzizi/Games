# Interactive Quiz Web Application

A modern, responsive web-based quiz application built with Flask, featuring dynamic questions, beautiful animations, and instant feedback.

##  Features

- **Dynamic Question System**
  - 20 questions across 5 categories
  - Randomized question order
  - Shuffled answer options
  - Real-time score tracking

- **Modern User Interface**
  - Responsive design for all devices
  - Smooth animations and transitions
  - Progress tracking
  - Beautiful gradient color scheme
  - Interactive feedback system

- **Categories**
  - General Knowledge
  - Science
  - History
  - Technology
  - Sports

##  Main Components

### 1. Backend (`app.py`)
- Flask application setup
- Route handlers:
  - `/`: Main quiz interface
  - `/question`: Serves questions
  - `/check_answer`: Validates answers
- Session management for score tracking
- Answer validation logic

### 2. Question Bank (`questions.py`)
- Structured question storage
- Each question contains:
  - Question text
  - Multiple choice options
  - Correct answer
  - Category

### 3. Frontend (`templates/index.html`)
- Responsive HTML structure
- Modern CSS styling:
  - Custom animations
  - Gradient effects
  - Mobile-first design
- Interactive JavaScript:
  - Dynamic question loading
  - Answer validation
  - Score updates
  - Progress tracking

##  Requirements

- Python 3.x
- Flask 2.3.3
- python-dotenv 1.0.0

##  Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd quiz
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

##  How to Play

1. Click "Start Quiz" to begin
2. Read each question carefully
3. Select your answer from the options
4. Get immediate feedback on your choice
5. View your final score and detailed results at the end
6. Click "Try Again" to restart with randomized questions

##  Styling Features

- **Color Scheme**
  - Primary: Modern blue gradient
  - Success: Teal for correct answers
  - Error: Pink for incorrect answers
  - Background: Subtle gradient overlay

- **Animations**
  - Fade-in transitions
  - Smooth button hover effects
  - Progress bar animations
  - Result screen transitions

- **Responsive Design**
  - Mobile-friendly layout
  - Adaptive typography
  - Touch-friendly buttons
  - Flexible container sizing

##  Customization

### Adding New Questions
Edit `questions.py` and add new questions following this format:
```python
{
    "category": "Your Category",
    "question": "Your Question?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Correct Option"
}
```

### Modifying Styles
The styles are defined in `templates/index.html` using CSS variables:
```css
:root {
    --primary-color: #4361ee;
    --secondary-color: #3f37c9;
    --success-color: #4cc9f0;
    --error-color: #f72585;
}
```


