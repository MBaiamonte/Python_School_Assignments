from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe
from flask_app.controllers import users

@app.route("/recipes/show/new_form")
def show_add_new_recipes_form():
    return render_template("add_new_recipe_form.html")

@app.route('/recipes/add_new', methods=['POST'])
def validate_and_add_new_recipe():
    if 'logged_in_user_id' not in session:
        print("no user logged in, login to view page")
        return("/")
    data={
        'name':request.form['name'],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'date_cooked':request.form['date_cooked'],
        'under_30':request.form['under_30'],
        'user_id':request.form['user_id']
    }
    if not recipe.Recipe.validate_recipe_form(data):
        return redirect("/recipes/show/new_form")
    print(data)
    recipe.Recipe.save_new_recipe(data)
    return redirect(f"/user/dashboard/{session['logged_in_user_id']}")

@app.route('/recipe/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    data={'id':recipe_id}
    recipe.Recipe.delete_recipe(data)
    return redirect(f"/user/dashboard/{session['logged_in_user_id']}")

@app.route("/recipe/show/update_form/<int:recipe_id>")
def show_recipe_update_form(recipe_id):
    if 'logged_in_user_id' not in session:
        print("no user logged in, login to view page")
        return("/")
    data={'id':recipe_id}
    this_recipe=recipe.Recipe.get_one_recipe(data)
    return render_template("update_recipe_form.html", recipe=this_recipe)

@app.route("/recipe/update/<int:recipe_id>", methods=['POST'])
def validate_and_update_recipe(recipe_id):
    data={
        'id':recipe_id,
        'name':request.form['name'],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'date_cooked':request.form['date_cooked'],
        'under_30':request.form['under_30'],
    }
    if not recipe.Recipe.validate_recipe_form(data):
        return redirect (f"/recipe/show/update_form/{session['logged_in_user_id']}")
    recipe.Recipe.update_recipe(data)
    return redirect(f"/user/dashboard/{session['logged_in_user_id']}")

@app.route("/recipe/show/<int:recipe_id>")
def show_one_recipe(recipe_id):
    data={'id':recipe_id}
    user_data={'id':session['logged_in_user_id']}
    one_recipe=recipe.Recipe.get_one_recipe_with_user(data)
    print("returned recipe info->>",one_recipe, "XXXXXXXXXXXXXXXXXXXXXXX")
    logged_in_user=user.User.get_user_by_id(user_data)
    return render_template("show_one_recipe.html", recipe=one_recipe ,logged_in_user=logged_in_user)