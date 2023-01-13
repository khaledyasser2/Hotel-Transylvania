from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///Database.db'
db=SQLAlchemy(app)
staffPass="joejoesbizzareadventure"
currName=None
currRegNum=None

class Login_Manager(db.Model):
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    name=db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Task %r>" % self.id

class Reservations_Manager(db.Model):
    DateTaken = db.Column(db.String, primary_key=True)
    RoomNum = db.Column(db.Integer, primary_key=True)
    ReservationNum=db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Task %r>" % self.RoomNum

def generateReservationNum(roomNum):
    #random ass way to generate reservation number from room number. Can change later
    return (roomNum*2+3)*4

with app.app_context():
    db.create_all()

@app.route("/", methods=["POST", "GET"])
def login():
    global currName
    if request.method == "POST":
        email = request.form["email"]
        print(email)
        user = db.session.query(Login_Manager.email, Login_Manager.name).filter(Login_Manager.email==email).first()
        print(user)
        if user is not None:
            currName=dict(user)["name"]
            return redirect("/book")
        else:
            return redirect("/register")
    return render_template("Login.html")

@app.route("/staff", methods=["POST", "GET"])
def staff():
    if request.method == "POST":
        password= request.form["password"]
        if password == staffPass:
            if request.form["submit"] == "Checkin":
                return redirect("/checkin")
            else:
                return redirect("/checkout")
        else:
            return redirect("/staff")
    return render_template("Staff.html")

@app.route("/checkout", methods=["POST", "GET"])
def checkout():
    if request.method == "POST":
        name = request.form["name"]
        roomNum = request.form["room"]
        print(name)
        print(roomNum)
        user = Reservations_Manager.query.filter(Reservations_Manager.RoomNum==int(roomNum), 
        Reservations_Manager.Name==name).delete()
        print(user)
        if user != 0:
            db.session.commit()
            return render_template("Complete.html")
        else:
            return render_template("Incomplete.html")
    return render_template("Checkout.html")

@app.route("/checkin", methods=["POST", "GET"])
def checkin():
    if request.method=="POST":
        name = request.form["name"]
        resNum = request.form["reservation"]
        user = Reservations_Manager.query.filter(Reservations_Manager.ReservationNum==int(resNum), 
        Reservations_Manager.Name==name).first()
        if user is not None:
            return render_template("Complete.html")
        else:
            return render_template("Incomplete.html")
    return render_template("Checkin.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    global currName
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]
        lgin = Login_Manager(email=email, password=password, name=name)
        try:
            db.session.add(lgin)
            db.session.commit()
            currName=name
        except:
            print("There is already an account with that email")
            return redirect("/")
        return redirect("/book")
    else:
        #print(Login_Manager.query.order_by(Login_Manager.name))
        return render_template("Register.html")

@app.route("/book", methods=["POST", "GET"])
def book():
    global currName
    global currRegNum
    print(currName)
    if currName is None:
        return redirect("/")
    if request.method == "POST":
        date = request.form["date"]
        room = request.form["room"]
        currRegNum=generateReservationNum(int(room))
        booking = Reservations_Manager(DateTaken=date, RoomNum=room, ReservationNum=currRegNum, Name=currName)
        try:
            db.session.add(booking)
            db.session.commit()
            return redirect("/pay")
        except Exception as e:
            print(e)
            return redirect("/book")
        
    return render_template("Booking.html")

@app.route("/pay", methods=["POST", "GET"])
def pay():
    if currRegNum is not None:
        return render_template("Payment.html", regNum=currRegNum)
    return "Oops"

if __name__=="__main__":
    app.run(debug=True)