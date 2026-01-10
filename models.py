from extensions import db   

class User(db.Model):
    __tablename__ = 'USER'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    tasks = db.relationship('Task', backref='user', lazy=True)  

class Task(db.Model):
    __tablename__ = 'TASK'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.String(20), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('USER.id'), nullable=False)