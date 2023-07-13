from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define the quiz questions
questions = [
    {
        'id': 1,
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Rome', 'Madrid'],
        'correct_answer': 'Paris'
    },
    {
        'id': 2,
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
        'correct_answer': 'Mars'
    },
    {
        'id': 3,
        'question': 'What is the largest organ in the human body?',
        'options': ['Heart', 'Liver', 'Brain', 'Skin'],
        'correct_answer': 'Skin'
    }
]

# Store the user's score and wrong answers
score = 0
wrong_answers = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global score, wrong_answers
    
    if request.method == 'POST':
        # Check answers and update the score
        for question in questions:
            selected_option = request.form.get(str(question['id']))
            if selected_option == question['correct_answer']:
                score += 1
            else:
                wrong_answers.append({
                    'question': question['question'],
                    'selected_option': selected_option,
                    'correct_option': question['correct_answer']
                })
        
        # Redirect to the result page with feedback
        return redirect('/result')
    
    return render_template('index.html', questions=questions)

@app.route('/result')
def result():
    global score, wrong_answers
    
    # Display the final score and incorrect answers
    final_score = score
    score = 0  # Reset the score for the next quiz
    
    return render_template('result.html', score=final_score, wrong_answers=wrong_answers)

if __name__ == '__main__':
    app.run(debug=True)
