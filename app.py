from flask import Flask, render_template, request, redirect, session
from models import User, Quiz

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        User.register(username, password)
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.login(username, password)
        if user:
            session['user_id'] = user[0]
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        title = request.form['title']
        quiz_id = Quiz.create_quiz(session['user_id'], title)
        return redirect('/dashboard')
    return render_template('create_quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
