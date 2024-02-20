from flask_app import app
from flask import render_template,redirect, request,flash, session 
from flask_app.models.user import User  #normaly just call moldes then file to prevent circl import

@app.route('/')
def show_dashboard():
    all_users=User.get_all_users()
    return render_template("dashboard.html", all_users=all_users)

@app.route("/show/new_user_form")
def show_form():
    return render_template("new_user_form.html")

@app.route("/save/new_user", methods=['POST'])
def save_new_user_and_validate():
    if not User.validate_new_user(request.form):
        return redirect('/show/new_user_form')
    User.save_new_user(request.form)
    return redirect("/")