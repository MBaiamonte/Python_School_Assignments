from flask import Flask, redirect, render_template, request
from users import User
app=Flask(__name__)

@app.route("/")
def show_user_table():
    all_users=User.get_all()
    print(all_users)
    return render_template("user_table.html" ,all_users_in_db=all_users)

@app.route('/new_user_form')
def show_form():
    return render_template("new_user_form.html")

@app.route("/submit_form", methods=["POST"])
def submit_form():
    data={
        "first_name": request.form['first_name'],
        "last_name":request.form['last_name'], 
        "email":request.form['email']
    }
    User.save(data)
    return redirect("/")
    




if __name__ =="__main__":
    app.run(debug=True)

