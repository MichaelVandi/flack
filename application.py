import os

from flask import Flask, render_template, session, request
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# List to store usernames
names = []

@app.route("/chat", methods=["GET", "POST"])
def chat():

    return render_template("chat.html", username= session["username"])


@app.route("/" , methods=["GET", "POST"])
def index():
    if session.get("username") is None:
        session["username"] = ""

    if request.method == "GET":
        # Getting the username variable stored in session
        if session["username"] == "":
            return render_template("index.html")

        #If the user already entered a username, open the chat route
        return render_template("chat.html", username=session["username"])

    elif request.method == "POST":
        # Get the username sent from the post request
        username = str(request.form.get("username"))

        # Check in the list of usernames is empty
        if len(names) == 0:
            # No name exists in the list yet, add the user as first
            names.append(username)
            session["username"] = username
            # Open the chat route
            return render_template("chat.html", username= username)

        # if there were pre existing names
        # Check if this particular username didn't exist
        if username in names:
            # Username was already there, return error
            return render_template ("index.html", message= "Username already exists, pick something else")
        else:
            # Username wasn't there, allow
            names.append(username)
            session["username"] = username
            #Open the chat route
            return render_template("chat.html", username=username)

   
