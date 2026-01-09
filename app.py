from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = ''

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

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST', 'localhost')  # default to localhost

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}'




if __name__ == '__main__':
    app.run(debug=True)