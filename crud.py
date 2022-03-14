import pymongo
from flask import Flask, render_template

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/razer"

mongo = pymongo(app)

UPLOAD_FOLDER = "static/assets"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/razer")
def home_page():
    computer = mongo.db.computer.find({})
    return render_template("razer.html",computer=computer)

if __name__ == "__main__":
    app.run(debug=True)
