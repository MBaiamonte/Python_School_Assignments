from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def show_users():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}, 
    {"first_name": "Matthew", "last_name": "Baiamonte"}
    ]
    return render_template("user_table.html", html_jinja_users=users)





if __name__=="__main__":
    app.run(debug=True)
