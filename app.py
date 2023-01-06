from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///accountTracker.db'
db=SQLAlchemy(app)

class Login_Manager(db.Model):
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    name=db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Task %r>" % self.id

with app.app_context():
   db.create_all()

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return redirect("/book")
    return render_template("Login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]
        lgin = Login_Manager(email=email, password=password, name=name)
        db.session.add(lgin)
        db.session.commit()
        return redirect("/book")
    return render_template("Register.html")

@app.route("/book", methods=["POST", "GET"])
def book():
    if request.method == "POST":
        return redirect("/pay")
    return render_template("Booking.html")

@app.route("/pay", methods=["POST", "GET"])
def pay():
    return render_template("Payment.html")

if __name__=="__main__":
    app.run(debug=True)