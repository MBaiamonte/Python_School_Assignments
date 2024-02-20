from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route("/")
def show_registration_and_login_forms():
    return render_template('login_registration.html')

@app.route("/user/save_new", methods=['POST'])
def save_new_user():
    if not user.User.validate_user(request.form):
        return redirect("/")
    hashed_password=bcrypt.generate_password_hash(request.form['registration_password'])
    data={
            'first_name':request.form['registration_first_name'],
            'last_name':request.form['registration_last_name'],
            'age':request.form['registration_age'],
            'email':request.form['registration_email'],
            'password':hashed_password
        }
    user_id=user.User.save_new_user(data)
    session["logged_in_user_id"]=user_id
    #could also put it all in one line --> session["logged_in_user_id"]=user.User.save_new_user(data)
    print("session-ed_id=", session["logged_in_user_id"])
    return redirect(f"/user/dashboard/{user_id}")

@app.route("/user/display_all")
def display_all_users():
    all_users_in_db=user.User.get_all_users()
    return render_template("show_all_users.html", all_users=all_users_in_db)


@app.route("/user/login", methods=['POST'])
def user_login():
    data={
        "email":request.form['login_email']
    }
    one_user=user.User.get_user_by_email(data)
    if not one_user:
        flash('Invalid Credentials', 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(one_user.password, request.form['login_password']):
        flash('Invalid password', 'login') #in real life program flash("invalid credentials", 'login)
        return redirect("/")
    session['logged_in_user_id']=one_user.id
    return redirect(f"/user/dashboard/{one_user.id}")


@app.route("/user/dashboard/<int:user_id>")
def show_user_dashboard(user_id):
    if 'logged_in_user_id' not in session: #apply to every get route to stop manual url entry
        return redirect("/")
    data={ "id":user_id}
    some_user=user.User.get_user_by_id(data)
    return render_template("user_profile.html", user=some_user)


@app.route("/user/logout")
def logout_user():
    print('this users id is', session['logged_in_user_id'], ",before session.clear is reached")
    session.clear()
    print(session, "if not empty then logout didn't work")
    return redirect("/")





# 2 options here, you can flash in the controller if one_user returns nothing/no email in db that matchs or set up another static method to validate the login form then call that method in the controller? i think?

