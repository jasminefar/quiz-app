import random

categories = ['General Knowledge', 'Science', 'Math']
difficulties = ['Easy', 'Medium', 'Hard']

questions_data = {
    'General Knowledge': {
        'Easy': [
            {'question': 'What is the capital of France?', 'options': ['Paris', 'London', 'Berlin', 'Madrid'], 'answer': 'Paris'},
            {'question': 'What is 2+2?', 'options': ['3', '4', '5', '6'], 'answer': '4'},
        ],
        'Medium': [
            {'question': 'What is the largest ocean on Earth?', 'options': ['Atlantic', 'Pacific', 'Indian', 'Arctic'], 'answer': 'Pacific'},
            {'question': 'Who wrote "To Kill a Mockingbird"?', 'options': ['Harper Lee', 'J.K. Rowling', 'Ernest Hemingway', 'Mark Twain'], 'answer': 'Harper Lee'},
        ],
        'Hard': [
            {'question': 'In what year was the United Nations established?', 'options': ['1945', '1950', '1960', '1975'], 'answer': '1945'},
            {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Pb', 'Fe'], 'answer': 'Au'},
        ],
    },
    'Science': {
        'Easy': [
            {'question': 'What planet is known as the Red Planet?', 'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'], 'answer': 'Mars'},
            {'question': 'What gas do plants absorb from the atmosphere?', 'options': ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen'], 'answer': 'Carbon Dioxide'},
        ],
        'Medium': [
            {'question': 'What is the hardest natural substance on Earth?', 'options': ['Gold', 'Iron', 'Diamond', 'Platinum'], 'answer': 'Diamond'},
            {'question': 'Who developed the theory of relativity?', 'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Niels Bohr'], 'answer': 'Albert Einstein'},
        ],
        'Hard': [
            {'question': 'What is the speed of light?', 'options': ['300,000 km/s', '150,000 km/s', '450,000 km/s', '600,000 km/s'], 'answer': '300,000 km/s'},
            {'question': 'What is the chemical symbol for the element with atomic number 1?', 'options': ['H', 'He', 'Li', 'Be'], 'answer': 'H'},
        ],
    },
    'Math': {
        'Easy': [
            {'question': 'What is 5+5?', 'options': ['10', '11', '12', '13'], 'answer': '10'},
            {'question': 'What is the square root of 16?', 'options': ['2', '4', '6', '8'], 'answer': '4'},
        ],
        'Medium': [
            {'question': 'What is 12*12?', 'options': ['120', '124', '144', '148'], 'answer': '144'},
            {'question': 'What is the value of Pi (approx)?', 'options': ['2.14', '3.14', '4.14', '5.14'], 'answer': '3.14'},
        ],
        'Hard': [
            {'question': 'What is the derivative of x^2?', 'options': ['x', '2x', 'x^2', '2x^2'], 'answer': '2x'},
            {'question': 'What is the integral of 1/x dx?', 'options': ['x', 'ln(x)', '1/x', 'e^x'], 'answer': 'ln(x)'},
        ],
    }
}

leaderboard = []

def get_questions(category, difficulty):
    return random.sample(questions_data[category][difficulty], len(questions_data[category][difficulty]))

def update_leaderboard(category, difficulty, score, total_questions, time_taken):
    leaderboard.append({
        'category': category,
        'difficulty': difficulty,
        'score': score,
        'total_questions': total_questions,
        'time_taken': time_taken
    })

def get_leaderboard():
    return sorted(leaderboard, key=lambda x: (x['score'], -x['time_taken']), reverse=True)
