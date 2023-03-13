# Import modules
from flask import Flask, render_template, request

# Create the Flask app
app = Flask(__name__)

# Define a route for the default URL, which loads the template
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
