from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///accountTracker.db'
db=SQLAlchemy(app)
staffPass="joejoesbizzareadventure"

class Login_Manager(db.Model):
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    name=db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Task %r>" % self.id

class Reservations_Manager(db.Model):
    DateTaken = db.Column(db.String, primary_key=True)
    RoomNum = db.Column(db.Integer, nullable=False)
    ReservationNum=db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Task %r>" % self.RoomNum

def generateReservationNum(roomNum):
    #random ass way to generate reservation number from room number. Can change later
    return (roomNum*2+3)*4

with app.app_context():
    db.create_all()

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        print(email)
        exists = db.session.query(Login_Manager.email).filter(Login_Manager.email==email).first() is not None
        if exists:
            return redirect("/book")
        else:
            return redirect("/register")
    return render_template("Login.html")

@app.route("/staff", methods=["POST", "GET"])
def staff():
    if request.method == "POST":
        password= request.form["password"]
        if password == staffPass:
            return render_template("Payment.html")
        else:
            return redirect("/staff")
    return render_template("Staff.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]
        lgin = Login_Manager(email=email, password=password, name=name)
        try:
            db.session.add(lgin)
            db.session.commit()
        except:
            print("There is already an account with that email")
            return redirect("/")
        return redirect("/book")
    else:
        #print(Login_Manager.query.order_by(Login_Manager.name))
        return render_template("Register.html")

@app.route("/book", methods=["POST", "GET"])
def book():
    if request.method == "POST":
        date = request.form["date"]
        room = request.form["room"]
        booking = Reservations_Manager(DateTaken=date, RoomNum=room, ReservationNum=generateReservationNum(int(room)))
        try:
            db.session.add(booking)
            db.session.commit()
        except:
            return redirect("/book")
        return redirect("/pay")
    return render_template("Booking.html")

@app.route("/pay", methods=["POST", "GET"])
def pay():
    return render_template("Payment.html")

if __name__=="__main__":
    app.run(debug=True)