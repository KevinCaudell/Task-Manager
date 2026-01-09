from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')





if __name__ == '__main__':
    app.run(debug=True)