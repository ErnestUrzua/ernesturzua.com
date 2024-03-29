from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Defining the home page of our site

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("home"))

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
