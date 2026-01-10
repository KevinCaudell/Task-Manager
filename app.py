from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db   
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@localhost/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)

from models import User, Task

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/calendar')
def calendar_page():
    return render_template('calendar.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/settings')
def settings_page():
    return render_template('settings.html')

@app.route('/tasks')
def tasks_page():
    all_tasks = Task.query.all()
    return render_template('tasks.html', tasks=all_tasks)

@app.route('/signup')
def signup_page():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)