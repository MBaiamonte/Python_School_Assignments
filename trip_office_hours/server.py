from flask import Flask, render_template, redirect, session
app= Flask(__name__)

@app.route("/")
def show_form():
    return render_template("index.html")

@app.route("/redirect", methods=["POST"])
def update_form():
    return redirect("/display")

@app.route("/display")
def display():
    return render_template("display.html")


if __name__=="__main__":
    app.run(debug=True)