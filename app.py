from flask import Flask, render_template, url_for, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///accountTracker.db'
db=SQLAlchemy(app)
#hi
class Login_Manager(db.Model):
    email = db.Column(db.String, primary_key=True)
    passwrod = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Task %r>" % self.id

with app.app_context():
   db.create_all()

@app.route("/")
def index():
    return render_template("Login.html")

@app.route("/register")
def register():
    return render_template("Register.html")

@app.route("/book")
def book():
    return render_template("Booking.html")

@app.route("/pay")
def pay():
    return render_template("Payment.html")

if __name__=="__main__":
    app.run(debug=True)