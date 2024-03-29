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
    # find all documents from recipes collection and assign them to recipes
    # variable
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/find", methods=["GET", "POST"])
def find():
    # the query sent by the user
    question = request.form.get("question")
    # get a list of recipes using the text search
    recipes = list(mongo.db.recipes.find({"$text": {"$search": question}}))
    # get a list of recipes using a regular expression, which will look inside
    # an array, a match a query in a string
    ingredients_list_search = list(mongo.db.recipes.find({"ingredients": {
        "$elemMatch": {"$regex": f'^.*{question}.*'}}}))
    # combine the two searches
    combined = recipes + ingredients_list_search

    # list to check for duplicates
    seen = []
    # list to return of results
    results = []

    # iterate over the combined lists
    for recipe in combined:
        # if the recipe name is in the seen list, skip this recipe, becasuse
        # its a duplicate
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
    # data from the form will be posted to mongodb
    if request.method == "POST":
        exist_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    # check if the username already exist in our database and if so,
    # display a flask message and redirect a user back to sign_up page
    # to sign up with another username
        if exist_user:
            flash("A user with this username already exists")
            return redirect(url_for("sign_up"))
    # if the username does not exist we gather data from the form
        sign_up = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "favourites": []
        }
    # insert the dictionary with variable "sign_up" into mongodb
        mongo.db.users.insert_one(sign_up)
    # put a user into a session cookie
        session["user_record"] = request.form.get("username").lower()
        Id_U = mongo.db.users.find_one(
                {"username": session["user_record"]})["_id"]
        favourites = list(mongo.db.users.find(
            {"favourites": ObjectId(Id_U)}))
    # display a flash message and redirect a user to their profile
        flash("You have been registered!")
        return redirect(url_for("profile", username=session["user_record"],
                        favourites=favourites))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # look for a single user within our users-collection
        exist_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if the exist_user variable found a match in the database
        if exist_user:
            # check if password matches
            if check_password_hash(exist_user
                                   ["password"], request.form.get("password")):
                session["user_record"] = request.form.get(
                        "username").lower()
            # message for a logged in user and they are redirected to their
            # profile page
                flash("Hello, {}. Ready for a cup of Joe?".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user_record"]))
        # if username and password are not matched, then flash messages
        # are displayed and a user redirected to the same log in page
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
    # retrieve username from mongodb and then display
    # in profile template
    username = mongo.db.users.find_one(
        {"username": session["user_record"]})["username"]

    if session["user_record"]:
        # if a user created a recipe save it in created recipe tab
        recipes = list(mongo.db.recipes.find(
            {"recipe_by": username}))
        if "user" in session:
            if session["user_record"] == username:
                user = mongo.db.users.find_one(
                       {"username": session["user_record"]})
                favourites = list(mongo.db.recipes.find(
                    {"_id": {"$in": user["favourites"]}}
                    ))
        user = mongo.db.users.find_one({"username": session["user_record"]})

        favourites = list(mongo.db.recipes.find({"_id": {
            "$in": user['favourites']}}))
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

    if "user_record" in session:
        user = mongo.db.users.find_one({"username": session["user_record"]})
        # convert the favoutrites array to a str of objectId's
        favourites = [str(f) for f in user['favourites']]
        # if the recipe id, is in the favourites list, then show the remove
        # button, otherwise show the add button
        favourite_button_text = 'Remove from favourites' if str(full_recipe[
            '_id']) in favourites else 'Add to favourites'

        return render_template("full_recipe.html", recipe=full_recipe,
                               favourites=favourites, user=user,
                               favourite_button_text=favourite_button_text)
    else:
        return render_template("full_recipe.html", recipe=full_recipe)


@app.route("/favourites/<Id_R>", methods=["GET", "POST"])
def favourites(Id_R):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(Id_R)})
    if "user_record" in session:
        if session["user_record"] != recipe["recipe_by"]:
            user = mongo.db.users.find_one(
                {"username": session["user_record"]})
            favourites = user["favourites"]

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

    return redirect(url_for("full_recipe", Id_R=Id_R, favourites=favourites,
                            user=user, recipe=recipe))


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
    return render_template("add_recipe.html", catgs=categories,
                           diff=difficulties)


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
    return render_template("edit_recipe.html", recipe=recipe, catgs=categories,
                           diff=difficulties)


@app.route("/delete_recipe/<Id_R>")
def delete_recipe(Id_R):
    mongo.db.recipes.delete_one({"_id": ObjectId(Id_R)})
    flash("Your recipe has been removed")
    return redirect(url_for("profile", username=session['user_record']))


@app.route("/coffee_categ")
def coffee_categ():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
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


@app.route("/edit_coffee_categ/<Id_C>", methods=["GET", "POST"])
def edit_coffee_categ(Id_C):
    # submit edited dictionary and replace the old data
    if request.method == "POST":
        update = {
            "category_name": request.form.get("category_name"),
            "category_img": request.form.get("category_img")
        }
        mongo.db.categories.replace_one({"_id": ObjectId(Id_C)}, update)
        # once data edited, flash message will appear
        flash("New Coffee Category has been Updated")
        return redirect(url_for("coffee_categ"))

    category = mongo.db.categories.find_one({"_id": ObjectId(Id_C)})
    return render_template("edit_coffee_categ.html", Id_C=category)


@app.route("/delete_coffee_categ/<Id_C>")
def delete_coffee_categ(Id_C):
    # call the categories collection on mongodb and remove a category with
    # a specific id
    mongo.db.categories.delete_one({"_id": ObjectId(Id_C)})
    # once removed, flash message will appear
    flash("Coffee Category has been Deleted")
    # redirect admin back to all categories
    return redirect(url_for("coffee_categ"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
