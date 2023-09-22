from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method =="POST":
        first_name = request.form["first_name"]
        print(first_name)
    
    return render_template("index.html")







app.run(debug=True, port=5001)