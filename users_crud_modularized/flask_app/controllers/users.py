from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/users")
def show_all_users():
    user=User.get_all()
    return render_template("show_all_users_table.html", all_users=user )

@app.route("/user/create", methods=["POST"])
def add_new_user():
    user_id=User.save(request.form)
    return redirect (f"/users/{user_id}")

@app.route("/user/add_new_form")
def show_new_user_form():
    return render_template("add_new_user_form.html")

@app.route("/users/<int:user_id>")
def show_one_user(user_id):
    user=User.get_one(user_id)
    return render_template("show_user.html", user=user)


@app.route('/user/show_update_form/<int:user_id>')
def show_update_form(user_id):
    user=User.get_one(user_id)
    return render_template("edit_user_form.html", user=user)

@app.route("/user/update", methods=["POST"])
def update_user():
    User.update(request.form)
    user_id=request.form['id']
    return redirect (f"/users/{user_id}")


@app.route('/user/delete/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect("/users")