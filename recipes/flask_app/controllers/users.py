from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe
from flask_app.controllers import recipes
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route("/")
def show_login_and_registration():
    # session.clear()  <--- dont use results in flash messages being cleared/not displayed
    return render_template("registration_and_login_forms.html")

@app.route("/user/save_new", methods=['POST'])
def save_new_user():
    # if not user.User.validate_new_user_registration_form(request.form):
    #     print(" registration form not valid")
    #     return redirect("/")
    if not user.User.validate_new_user_registration_form(request.form):
        return redirect("/")
    print("registration form passed validation")
    hashed_password=bcrypt.generate_password_hash(request.form['password'])
    data= {
        'first_name': request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':hashed_password
        }
    print(data)
    session['logged_in_user_id']=user.User.save_new_user(data)
    print("logged in user session=", session['logged_in_user_id'], "if blank, registration didn't work....(/user/save_new)")
    return redirect(f"/user/dashboard/{session['logged_in_user_id']}")

@app.route("/user/login", methods=['POST'])
def login_user_and_validate():
    data={
        'email':request.form['email'],
        'password':request.form['password']
    }
    some_user=user.User.get_user_by_email(data)
    if not some_user:
        flash("No email in db", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(some_user.password, request.form['password']):
        flash("Invalid password", 'login')
        return redirect("/")
#^^^one approach
    # if not user.User.validate_user_login(data):
    #     return redirect("/")
#^^^second approach, coulndt get to work right due to sessioning id. 
    session['logged_in_user_id']=some_user.id
    print("iff you see this then log in was successful","session-ed id=",session['logged_in_user_id'], "XXXXX(/login)XXXXXX")
    return redirect(f"/user/dashboard/{session['logged_in_user_id']}")

@app.route("/user/logout")
def logout_user():
    print("session-ed data before logout",session)
    session.clear()
    print("logout successful if this is blank ->", session, "if not blank then logout was not successful")
    return redirect("/")

@app.route("/user/dashboard/<int:user_id>")
def show_user_dashboard(user_id):
    if 'logged_in_user_id' not in session:
        print("no user logged in, login to view page XXXXXXXXXXXXXXXXXXXXXXX")
        return("/")
    data={"id":session['logged_in_user_id']}
    logged_in_user=user.User.get_user_by_id(data)
    print("user retrieved=",logged_in_user, "(user/dashboard)")
    all_recipes=recipe.Recipe.get_all_recipes_with_users()
    print("all the recipes returned=",all_recipes,"xxxxxxxxxxxxx")
    return render_template("show_user.html", user=logged_in_user, all_recipes=all_recipes )


