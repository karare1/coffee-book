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
@app.route("/index")
def index():
    return render_template("index.html")


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
        recipes = list(mongo.db.recipes.find(
            {"recipe_by": username}))
        # Id_U = mongo.db.users.find_one({"_id": ObjectId(Id_U)})   
        # favourites = username["favourites"]
        return render_template(
            "profile.html", username=username, recipes=recipes)
            # favourites=favourites)

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


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_image": request.form.get("recipe_url"),
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_intro": request.form.get("recipe_intro"),
            "preparation_time": request.form.get("preparation_time"),
            "difficulty": request.form.get("difficulty"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "recipe_by": session["user_record"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been added")
        return redirect(url_for("recipes"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", catgs=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
