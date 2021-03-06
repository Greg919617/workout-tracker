from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import bcrypt
app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://workout-tracker:beproductive@localhost:8889/workout-tracker'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    password_hash = db.Column(db.Unicode(100))
    units = db.Column(db.String(3))
    workouts = db.relationship('Workout', backref='user', lazy='dynamic')


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.Column(db.Text)  
    bodyweight = db.Column(db.Numeric)
    exercises = db.relationship('Exercise', backref='workout', lazy='dynamic')

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))



class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    order = db.Column(db.Integer, unique=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))  
    sets = db.relationship('Set', backref='exercise', lazy='dynamic')



class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, unique=True)
    weight = db.Column(db.Numeric)
    reps =db.Column(db.Integer)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id')) 

    

if __name__=='__main__':
    manager.run()  


  


  




