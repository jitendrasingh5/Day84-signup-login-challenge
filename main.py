from flask import Flask, request,redirect
from replit import db

app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def new_user():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name":form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route("/login", methods=["POST"])
def DOlogin():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    return redirect("/login")
  else:
    if form["password"] == db[form["username"]]["password"]:
      return f"""Hello {db[form["username"]]["name"]}"""
    else:
      return redirect("login")




      
  

@app.route("/login")
def login():
  page = ""
  f = open("static/login.html", "r")
  page = f.read()
  f.close()
  return page
  

@app.route("/signup")
def signup():
  page = ""
  f = open("static/sign.html", "r")
  page = f.read()
  f.close()
  return page





@app.route('/')
def index():
  page = ""
  f = open("static/home.html", "r")
  page = f.read()
  f.close()
  return page
  


app.run(host='0.0.0.0', port=81)

