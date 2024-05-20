from flask import Flask, render_template, url_for

app = Flask(__name__) # just references this file

# Need to set up an index route so we don't immediately 404.
# in flask, set up routes with the @route decorator.
@app.route('/') 

def index():
    return render_template('index.html')

# for now set debug to true so any errors show up on webpage
if __name__ == "__main__":
    app.run(debug=True)

# To run, use a browser and use http://localhost:5000/
