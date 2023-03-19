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
    # generate data from recipes collection on mongodb
    # find all documents from recipes collection and assign them to recipes variable
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/find", methods=["GET", "POST"])
def find():
    # the query sent by the user
    question = request.form.get("question")
    # get a list of recipes using the text search
    recipes = list(mongo.db.recipes.find({"$text": {"$search": question}}))
    # get a list of recipes using a regular expression, which will look inside an array, a match a query in a string
    ingredients_list_search = list(mongo.db.recipes.find({"ingredients": {"$elemMatch": {"$regex": f'^.*{question}.*'}}}))
    # combine the two searches
    combined = recipes + ingredients_list_search

    # list to check for duplicates
    seen = []
    # list to return of results
    results = []

    # iterate over the combined lists
    for recipe in combined:
        # if the recipe name is in the seen list, skip this recipe, becasuse its a duplicate
        if recipe['recipe_name'] in seen:
            continue
        # otherwise, add the recipe to the results array
        else:
            # add recipe to result list
            results.append(recipe)
            # add the name to the seen list
            seen.append(recipe['recipe_name'])

    return render_template("recipes.html", recipes=results)


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
            "password": generate_password_hash(request.form.get("password")),
            "favourites": []
        }
        mongo.db.users.insert_one(sign_up)

        session["user_record"] = request.form.get("username").lower()
        Id_U = mongo.db.users.find_one(
                {"username": session["user_record"]})["_id"]
        favourites = list(mongo.db.users.find(
            {"favourites": ObjectId(Id_U)}))

        flash("You have been registered!")
        return redirect(url_for("profile", username=session["user_record"], favourites=favourites))
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
        if "user" in session:
            if session["user_record"] == username:
            # user variable to grab user's data
                user = mongo.db.users.find_one(
                    {"username": session["user_record"]})
                
                favourites = list(mongo.db.recipes.find(
                    {"_id": {"$in": user["favourites"]}}
                    ))
        user = mongo.db.users.find_one({"username": session["user_record"]})

        favourites = list(mongo.db.recipes.find({"_id": {"$in": user['favourites']}}))
        print(favourites)

        # Id_U = mongo.db.users.find_one(
        #         {"username": session["user_record"]})["_id"]
        # favourites = list(mongo.db.users.find(
        #     {"favourites": ObjectId(Id_U)}))
        # favourites = mongo.db.users.find_one(
        #     {"favourites": ObjectId(Id_U)})
        # user_fav = mongo.db.users.find_one(
        #     {"_id": ObjectId(Id_U)})
        # favourites = user_fav["favourites"]
        return render_template(
            "profile.html", username=username, recipes=recipes,
            favourites=favourites)

    return redirect(url_for("log_in"))


@app.route("/log_out")
def log_out():
    flash("Log in for the best experience")
    session.pop("user_record")
    return redirect(url_for("log_in"))


@app.route("/full_recipe/<Id_R>")
def full_recipe(Id_R):
    full_recipe = mongo.db.recipes.find_one({"_id": ObjectId(Id_R)})
    # return render_template("full_recipe.html", recipe=full_recipe)
    if session["user_record"]:
        user = mongo.db.users.find_one({"username": session["user_record"]})
        # convert the favoutrites array to a str of objectId's
        favourites = [str(f) for f in user['favourites']]
        # if the recipe id, is in the favourites list, then show the remove button, otherwise show the add button
        favourite_button_text = 'Remove from favourites' if str(full_recipe['_id']) in favourites else 'Add to favourites'


        # if ObjectId(Id_R) in favourites:
        #     favourites = True
        # else:
        #     favourites = False
    # else:
        # favourites = False
        # Id_U = mongo.db.users.find_one(
        #     {"username": session["user_record"]})["_id"]
        # user_fav = mongo.db.users.find_one(
        #     {"_id": ObjectId(Id_U)})
        # favourites = mongo.db.users.find_one(
        #     {"favourites": ObjectId(Id_U)})["favourites"]
        # favourites = user_fav["favourites"]
        # create_U = mongo.db.users.find_one(
        #     {"username": session["user_record"]})["creator"]
    return render_template("full_recipe.html", recipe=full_recipe, favourites=favourites, user=user, favourite_button_text=favourite_button_text)


@app.route("/favourites/<Id_R>", methods=["GET", "POST"])
def favourites(Id_R):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(Id_R)})
    if "user_record" in session:
        if session["user_record"] != recipe["recipe_by"]:
            user = mongo.db.users.find_one(
                {"username": session["user_record"]})
            favourites = user["favourites"]
            print(favourites)

            # Checks if recipe is already in cookbook
            if ObjectId(Id_R) not in favourites:
                # Adds recipe_id to user's cookbook
                mongo.db.users.update_one({"username": session["user_record"]},
                                          {"$push": {"favourites": ObjectId(
                                                    Id_R)}})
                flash("Recipe Added to My Cookbook")
                return redirect(url_for("full_recipe", Id_R=Id_R))

            else:
                # If recipe is already in cookbook, remove it from the cookbook
                mongo.db.users.update_one({"username": session["user_record"]},
                                          {"$pull": {"favourites": ObjectId(
                                                    Id_R)}})
                flash("Recipe Removed")
                return redirect((url_for("full_recipe", Id_R=Id_R)))

    return redirect(url_for("full_recipe", Id_R=Id_R, favourites=favourites, user=user, recipe=recipe))


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
    difficulties = mongo.db.difficulties.find().sort("difficulty", 1)
    return render_template("add_recipe.html", catgs=categories, diff=difficulties)


@app.route("/edit_recipe/<Id_R>", methods=["GET", "POST"])
def edit_recipe(Id_R):
    if request.method == "POST":
        update = {
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
        mongo.db.recipes.replace_one({"_id": ObjectId(Id_R)}, update, True)
        flash("Your updated recipe has been stored")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(Id_R)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulties = mongo.db.difficulties.find().sort("difficulty", 1)
    return render_template("edit_recipe.html", recipe=recipe, catgs=categories, diff=difficulties)


@app.route("/delete_recipe/<Id_R>")
def delete_recipe(Id_R):
    mongo.db.recipes.delete_one({"_id": ObjectId(Id_R)})
    flash("Your recipe has been removed")
    return redirect(url_for("profile", username=session['user_record']))


@app.route("/coffeee_categ")
def coffee_categ():
    categories = list(mongo.db.categories.find().sort("category_name", 1 ))
    return render_template("coffee_categ.html", categ=categories)


@app.route("/add_coffee_categ", methods=["GET", "POST"])
def add_coffee_categ():
    # if the function is called it will grab data from the form and
    # instert it into the mongodb
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_img": request.form.get("category_img")
        }
        mongo.db.categories.insert_one(category)
        # once inserted, it will display flash message and redirect
        # an admin to coffee_categ page
        flash("New Coffee Category has been Added")
        return redirect(url_for("coffee_categ"))
    # otherwise get method will display an empty form
    return render_template("add_coffee_categ.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
