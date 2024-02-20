from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key="ngrbjgsnlknbwgnlkb"

@app.route("/")
def display_count():
    return render_template("index.html")

@app.route("/increase_count")
def increase_count():
    if 'visits' not in session:
        session['visits']=1
    else:
        session['visits']+=1
        print("key dosent exist")
    return redirect("/")

@app.route('/destroy_session')
def destroy_session():
    # session.clear()   <<--- works as well just remove comment
    session.pop('visits')
    session['visits']=1
    return redirect("/")

@app.route("/two_visits")
def add_two_visits():
    if 'visits' not in session:
        session['visits']=3
    else:
        session['visits']+=2
    return redirect ("/")


if __name__=="__main__":
    app.run(debug=True)