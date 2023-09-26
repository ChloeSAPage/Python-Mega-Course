from datetime import datetime
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


app = Flask(__name__)

app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method =="POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj  = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]
        
        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()
        message_body =f"Thank you for your submission, {first_name}.\n"\
                    f"Here is your data:\n{first_name}\n{last_name}\n{date}\n{occupation}"
        message = Message(subject="New Form submission", sender=app.config["MAIL_USERNAME"],
                        recipients=[email], body=message_body)
        mail.send(message)
        
        flash(f"{first_name}, your form was submitted successfully!", "success")
    
    return render_template("index.html")





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)