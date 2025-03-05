from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"  # Explicit table name to avoid conflicts
    User_id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(32), unique=True, nullable=False)
    Passhash = db.Column(db.String(256), nullable=False)
    FullName = db.Column(db.String(64), nullable=True)
    Qualification = db.Column(db.String(128), nullable=True)
    DOB = db.Column(db.Date, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

class Subject(db.Model):
    __tablename__ = "subjects"
    Sub_id = db.Column(db.Integer, primary_key=True)
    SubName = db.Column(db.String(64), unique=True, nullable=False)
    Sub_Description = db.Column(db.Text, nullable=True)

class Chapter(db.Model):
    __tablename__ = "chapters"
    Ch_id = db.Column(db.Integer, primary_key=True)
    Ch_name = db.Column(db.String(128), nullable=False)
    Ch_description = db.Column(db.Text, nullable=True)
    Sub_id = db.Column(db.Integer, db.ForeignKey("subjects.Sub_id"), nullable=False)

    subject = db.relationship("Subject", backref=db.backref("chapters", lazy=True))

class Quiz(db.Model):
    __tablename__ = "quizzes"
    Q_id = db.Column(db.Integer, primary_key=True)
    Ch_id = db.Column(db.Integer, db.ForeignKey("chapters.Ch_id"), nullable=False)
    Date_of_quiz = db.Column(db.Date, nullable=False)
    Time_duration = db.Column(db.Integer, nullable=False)  # in minutes
    No_of_questions = db.Column(db.Integer, nullable=False)
    Total_marks = db.Column(db.Integer, nullable=False)

    chapter = db.relationship("Chapter", backref=db.backref("quizzes", lazy=True))

class Question(db.Model):
    __tablename__ = "questions"
    Qs_id = db.Column(db.Integer, primary_key=True)
    Q_id = db.Column(db.Integer, db.ForeignKey("quizzes.Q_id"), nullable=False)
    Qs_statement = db.Column(db.Text, nullable=False)
    Marks = db.Column(db.Integer, nullable=False)

    quiz = db.relationship("Quiz", backref=db.backref("questions", lazy=True))

class Option(db.Model):
    __tablename__ = "options"
    O_id = db.Column(db.Integer, primary_key=True)
    Qs_id = db.Column(db.Integer, db.ForeignKey("questions.Qs_id"), nullable=False)
    O_statement = db.Column(db.Text, nullable=False)
    Is_correct = db.Column(db.Boolean, nullable=False, default=False)

    question = db.relationship("Question", backref=db.backref("options", lazy=True))

class Score(db.Model):
    __tablename__ = "scores"
    S_id = db.Column(db.Integer, primary_key=True)
    Q_id = db.Column(db.Integer, db.ForeignKey("quizzes.Q_id"), nullable=False)
    User_id = db.Column(db.Integer, db.ForeignKey("users.User_id"), nullable=False)  # Fixed table reference
    Timestamp = db.Column(db.DateTime, nullable=False)
    Total_scored = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", backref=db.backref("scores", lazy=True))
    quiz = db.relationship("Quiz", backref=db.backref("scores", lazy=True))

# Creating tables
with app.app_context():
    db.create_all()
