import tkinter as tk
from tkinter import messagebox

# Example questions
# Each question is a dictionary with the question text, a list of options, and the correct answer.
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Stephen King"], "answer": "Harper Lee"},
]

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.current_question = 0
        self.score = 0

        self.question_var = tk.StringVar()
        self.question_label = tk.Label(self.master, textvariable=self.question_var, font=("Arial", 16))
        self.question_label.pack(pady=(20, 10))

        self.options_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="Option " + str(i + 1), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.options_buttons.append(button)

        self.score_var = tk.StringVar()
        self.score_label = tk.Label(self.master, textvariable=self.score_var, font=("Arial", 14))
        self.score_label.pack(pady=(10, 20))

        self.load_question()

    def load_question(self):
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_var.set(q["question"])
            for i, option in enumerate(q["options"]):
                self.options_buttons[i].config(text=option)
        else:
            self.end_quiz()

    def check_answer(self, choice):
        correct_answer = questions[self.current_question]["answer"]
        if questions[self.current_question]["options"][choice] == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Wrong!", f"The correct answer was: {correct_answer}")
        self.current_question += 1
        self.score_var.set(f"Score: {self.score}")
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your final score is: {self.score}/{len(questions)}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
