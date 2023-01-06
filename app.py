from flask import Flask, render_template, url_for, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    email = db.Column(db.String, primary_key=True)
    passwrod = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Task %r>" % self.id

@app.route("/")
def index():
    return render_template("Login.html")

@app.route("/register")
def register():
    return render_template("Register.html")

if __name__=="__main__":
    app.run(debug=True)