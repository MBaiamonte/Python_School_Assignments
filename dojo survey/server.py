from flask import Flask, session, redirect, render_template, request
app=Flask(__name__)
app.secret_key='bgrfdbfbrbgb'

@app.route("/")
def show_form():
    session.clear()
    return render_template("user_form.html")

@app.route("/process", methods=['POST'])
def process_form():
    session['name']=request.form['name']
    session['dojo_location']=request.form['dojo_location']
    session['fav_lang']= request.form['fav_lang']
    session['comment']=request.form['comment']
    return redirect("/result")

@app.route("/result")
def show_user_info():
    return render_template("display_user.html", name=session['name'],dojo_location=session['dojo_location'], fav_lang=session['fav_lang'], comment=session['comment'])

if __name__=="__main__":
    app.run(debug=True)