from flask import Flask, render_template, request, redirect, url_for, session
import quiz_data
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html', categories=quiz_data.categories, difficulties=quiz_data.difficulties)

@app.route('/quiz', methods=['POST'])
def quiz():
    category = request.form['category']
    difficulty = request.form['difficulty']
    session['category'] = category
    session['difficulty'] = difficulty
    session['score'] = 0
    session['start_time'] = time.time()
    questions = quiz_data.get_questions(category, difficulty)
    session['questions'] = questions
    session['current_question'] = 0
    return redirect(url_for('question'))

@app.route('/question')
def question():
    if 'questions' not in session or session['current_question'] >= len(session['questions']):
        return redirect(url_for('index'))
    question_data = session['questions'][session['current_question']]
    return render_template('quiz.html', question=question_data['question'], options=question_data['options'], question_number=session['current_question']+1, total_questions=len(session['questions']))

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer']
    correct_answer = session['questions'][session['current_question']]['answer']
    if answer == correct_answer:
        session['score'] += 1
    session['current_question'] += 1
    if session['current_question'] >= len(session['questions']):
        return redirect(url_for('result'))
    return redirect(url_for('question'))

@app.route('/result')
def result():
    total_questions = len(session['questions'])
    score = session['score']
    time_taken = int(time.time() - session['start_time'])
    quiz_data.update_leaderboard(session['category'], session['difficulty'], score, total_questions, time_taken)
    return render_template('result.html', score=score, total_questions=total_questions, time_taken=time_taken)

@app.route('/leaderboard')
def leaderboard():
    leaderboard_data = quiz_data.get_leaderboard()
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)