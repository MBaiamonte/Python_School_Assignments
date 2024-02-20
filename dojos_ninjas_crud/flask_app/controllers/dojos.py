from flask_app import app 
from flask import render_template, request, redirect, session, flash
from flask_app.models import dojo, ninja

@app.route("/dojos")
def show_all_dojos():
    all_dojos=dojo.Dojo.get_all()
    return render_template("add_new_dojo.html" ,all_dojos=all_dojos)

@app.route('/dojos/add', methods=["POST"])
def add_new_dojo():
    dojo.Dojo.save(request.form)
    return redirect("/dojos")

@app.route('/show/dojos_with_ninjas_table/<int:dojo_id>')
def show_dojos_with_ninjas(dojo_id):
    one_dojo=dojo.Dojo.get_dojo_with_ninjas(dojo_id)

    return render_template("show_dojo_and_ninjas_table.html",dojo=one_dojo)

    # changing line 17 paramter from data to dojo id also  moved data dictionary to modles (works fin when in controlller)