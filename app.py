# To import the Flask dependency, add the following to your code
from flask import Flask
# Add the following to your code to create a new Flask instance called app
app = Flask(__name__)
# our Flask app has been created—let's create our first route!
@app.route('/')
def hello_world():
    return 'Hello world'
    
