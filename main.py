from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define the quiz questions
firstTask = [
    {       
        'id': 1,
        'question': '1. What do we learn about the speaker from the start?',
        'options': ['A. He was born in London.', 'B. His name is Samuel Johnson', 'C. He is tired of living in London.'],
        'correct_answer': 'A. He was born in London.'
    },
     {       
        'id': 2,
        'question': '2. What do we learn about London?',
        'options': ['A. It was never ruled by the Romans.', 'B. It was built far from the River Thames.', 'C. The Romans called it Londinium'],
        'correct_answer': 'C. The Romans called it Londinium'
    },
     {       
        'id': 3,
        'question': '3. One surprising fact mentioned by the speaker is that ',
        'options': ['A. an amphitheater was used for theatre performances. ', 'B. gladiator fights were held in Londinium.', 'C. no sign from the Roman period can be found in London.'],
        'correct_answer': 'B. gladiator fights were held in Londinium.'
    },
     {       
        'id': 4,
        'question': '4. The City of London is one of the',
        'options': ['A. most modern districts of London.', 'B. largest districts of London by area.', 'C. world’s wealthiest financial districts.'],
        'correct_answer': 'C. world’s wealthiest financial districts.'
    },
     {       
        'id': 5,
        'question': '5. What does the speaker say about Sir Christopher Wren?',
        'options': ['A. He designed St Paul’s Cathedral in London.', 'B. All of his churches are still there in London.', 'C. The Great Fire of London destroyed many of his churches.'],
        'correct_answer': 'A. He designed St Paul’s Cathedral in London.'
    },
     {       
        'id': 6,
        'question': '6. The Great Fire of London started because of ',
        'options': ['A. a strong wind.', 'B. a careless mistake.', 'C. a baker’s secret plan.'],
        'correct_answer': 'B. a careless mistake.'
    },
     {       
        'id': 7,
        'question': '7. You will be awarded a certificate if you',
        'options': ['A. walk sixty-two metres to the baker’s shop.', 'B. take amazing photos of the city’s best views.', 'C. get to the top of the Monument to the Great Fire of London.'],
        'correct_answer': 'C. get to the top of the Monument to the Great Fire of London.'
    },
     {       
        'id': 8,
        'question': '8. Where does the tour guide finish his tour?',
        'options': ['A. At London Bridge.', 'B. At Tower Bridge of London.', 'C. At the Monument to the Great Fire of London.'],
        'correct_answer': 'A. At London Bridge.'
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
        for question in firstTask:
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
    
    return render_template('index.html', questions=firstTask)

@app.route('/result')
def result():
    global score, wrong_answers
    
    # Display the final score and incorrect answers
    final_score = score
    score = 0  # Reset the score for the next quiz
    
    return render_template('result.html', score=final_score, wrong_answers=wrong_answers)

if __name__ == '__main__':
    app.run(debug=True)
