from flask import Flask, render_template, request   # We imported render_template
import pyshorteners

app = Flask(__name__)  # We created a Flask instance called app

@app.route("/", methods=['POST', 'GET'])
def home():
  if request.method=="POST":
    url_received = request.form["url"]
    short_url = pyshorteners.Shortener().tinyurl.short(url_received)
    return render_template("index.html", new_url=short_url, old_url=url_received)
  else:
    return render_template('index.html')
    
@app.route("/about") # We created a route decorator
def about(): # We created a view function
    return render_template("about.html") # We returned a string
    
if __name__ == "__main__": # We used this to run the Flask application only if the script is directly executed from the Python interpreter and not used as an imported module
    app.run(debug=True) # We ran the Flask app in debug mode
    