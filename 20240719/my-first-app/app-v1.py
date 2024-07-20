from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p><b>Maheswaran</b>"

@app.route("/")
def index():
    return "<h3>Home Page</h3>"    
@app.route("/about")
def about():
    return "<h3>About Us</h3>"  
@app.route("/services")
def services():
    return "<h3>Services</h3>"  