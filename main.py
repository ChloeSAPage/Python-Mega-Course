from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    
    return

@app.route("/api/v1/pillow/")
def pillow():
    return {"definition": "cushion under head", "word": "pillow"}

@app.route("/api/v1/sun/")
def sun():
    return {"definition": "1. ball of fire in sky /n 2. star in solar system/n", "word": "sun"}

app.run(debug=True)