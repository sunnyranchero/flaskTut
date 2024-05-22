from flask import Flask, render_template, url_for, request, redirect
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

    def __repr__(self):
        return '<Task %r>' % self.id # every time we create an element it will return the task and the ID of that element

# with app.app_context():
#     db.create_all()


# Need to set up an index route so we don't immediately 404.
# in flask, set up routes with the @route decorator.
@app.route('/', methods=['POST', 'GET']) 

def index():
    if request.method == 'POST':
        task_content = request.form['content'] #content here is pulled from the text box in the html file
        new_task = Todo(content=task_content) #todo class model

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task.'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # returns a listing of all the db contents
        return render_template('index.html', tasks=tasks)

# create the delete portion, the pk is the easiest identifier
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/') # redirect back to homepage
    except:
        return 'There was a problem deleting that task.'


# for now set debug to true so any errors show up on webpage
if __name__ == "__main__":
    app.run(debug=True)

# To run, use a browser and use http://localhost:5000/
