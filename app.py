import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        exist_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if exist_user:
            flash("A user with this username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        session["user_record"] = request.form.get("username").lower()
        flash("You have been registered!")
        return redirect(url_for("profile", username=session["user_record"]))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        exist_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if exist_user:
            if check_password_hash(exist_user
                                   ["password"], request.form.get("password")):
                session["user_record"] = request.form.get(
                        "username").lower()
                flash("Hello, {}. Ready for a cup of Joe?".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user_record"]))

            else:
                flash(
                    "Oops, enter the correct username and password to Log In")
                return redirect(url_for("log_in"))

        else:

            flash("Oops, enter the correct username and password to Log In")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user_record"]})["username"]

    if session["user_record"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("log_in"))


@app.route("/log_out")
def log_out():
    flash("Log in for the best experience")
    session.pop("user_record")
    return redirect(url_for("log_in"))


@app.route("/full_recipe/<Id_R>")
def full_recipe(Id_R):
    full_recipe = mongo.db.recipes.find_one({"_id": ObjectId(Id_R)})
    return render_template("full_recipe.html", recipe=full_recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
