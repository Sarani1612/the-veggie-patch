import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', recipes=mongo.db.recipes.find())


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    current_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('viewrecipe.html', recipe=current_recipe)


@app.route('/categories')
def categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/categories/<category_name>')
def view_category(category_name):
    recipes = mongo.db.recipes.find({"category_name": category_name})
    return render_template('viewcategory.html',
                           recipes=recipes,
                           category_heading=category_name)


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', 
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    new_recipe = {'name': request.form.get('recipe_name'),
                  'category_name': request.form.get('category_name'),
                  'prep_time': request.form.get('prep_time'),
                  'cook_time': request.form.get('cook_time'),
                  'serves': request.form.get('serves'),
                  'ingredients': request.form.get('ingredients'),
                  'image_url': request.form.get('image_url'),
                  'instructions': request.form.get('instructions'),
                  'id_key': request.form.get('id_key')}
    recipes.insert_one(new_recipe)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
