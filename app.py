from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Activate Venv with .\env\Scripts\activate.ps1
# Create Env https://stackoverflow.com/questions/73961938/flask-sqlalchemy-db-create-all-raises-runtimeerror-working-outside-of-applicat

app = Flask(__name__) # just references this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# 3 forward slashes is a relative path and 4 is absolute.
db = SQLAlchemy(app) # initialize the database by passing in the app

# Next, create our model, we are just calling it todo, not actually doing a TODO.
class Todo(db.Model): # below we are setting up the columns.
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) #what holds each task, we don't want this left blank
    date_created = db.Column(db.DateTime, default=datetime.utcnow) #will auto set.

    # now need a function that will return a string when we create a new element

    def __ref__(self):
        return '<Task %r>' % self.id # every time we create an element it will return the task and the ID of that element

# with app.app_context():
#     db.create_all()


# Need to set up an index route so we don't immediately 404.
# in flask, set up routes with the @route decorator.
@app.route('/') 

def index():
    return render_template('index.html')

# for now set debug to true so any errors show up on webpage
if __name__ == "__main__":
    app.run(debug=True)

# To run, use a browser and use http://localhost:5000/
