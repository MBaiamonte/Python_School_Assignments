from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models import ninja, dojo


@app.route("/ninja/show/add_new_ninja_form")
def show_new_ninja_form():
	all_dojos= dojo.Dojo.get_all()
	print("all dojos", all_dojos)
	return render_template("new_ninja_form.html", all_dojos=all_dojos)

@app.route("/ninjas/add_new", methods=['POST'])
def save_new_ninja():
	print("request.form for save new ninja", request.form)
	ninja.Ninja.save_ninja(request.form)
	return redirect("/dojos")

@app.route('/ninjas/delete/<int:ninja_id>')
def delete_one_ninja(ninja_id):
	ninja.Ninja.delete_ninja(ninja_id)
	return redirect(f'/show/dojos_with_ninjas_table/{dojo_id}')

