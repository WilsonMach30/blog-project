from flask import Flask, render_template, session, request, redirect, url_for
from db import *
import datetime

app = Flask(__name__)
app.secret_key = "yolo"

@app.route("/", methods=["GET", "POST"])
def home():
    # check if user is logged in 
    if "username" in session: 
        user = session["username"]

        # see if there was a submission of new blogs
        submission = request.args.get('submission', False)    

        # sets up blog gallery
        my_blogs = get_blogs(user)
        return render_template("home.html", username = user, submission = submission, my_blogs = my_blogs)
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def log_in():
    # if a form was submitted with log in info
    if request.method == "POST":
        # grab the username and password entered on form
        username = request.form['username']
        password = request.form['password']

        # check credentials
        correct_credentials = check_credentials(username, password)
        if correct_credentials:
            # log user in
            session['username'] = username
            return redirect(url_for("home", username = username))
        else: 
            # return error 
            return render_template("login.html", error = True)
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    # if a form was submitted with log in info
    if request.method == "POST":
        # grab the username and password entered on form
        username = request.form['username']
        password = request.form['password']
        
        # make sure that no user exists
        no_user_exists = check_user_exist(username)
        if no_user_exists == None:
            # make sure password and confirm-password is the same
            if password != request.form['confirm-password']:
                return render_template("signup.html", error = True, error_type = "Passwords do not match")
            create_new_user(username, password)
            return redirect("/login")
        else:
            # throws user already exists error
            return render_template("signup.html", error = True, error_type = "User already exists.")
    return render_template("signup.html")

@app.route("/logout", methods=["GET"])
def log_out():
    session.pop('username')
    return redirect("/")

@app.route("/newblog", methods=["GET", "POST"])
def new_blog():
    # if a form was submitted with blog info 
    if request.method == "POST":
        # grabs the information entered on form
        blog_id = get_last_blog_id() + 1 # gets last blog_id
        title = request.form["title"]
        author = session["username"] # gets current username
        blog_content = request.form["blog-content"]
        last_modified = datetime.datetime.now() # gets current datetime

        create_new_blog(blog_id, title, author, blog_content, last_modified)
        return redirect(url_for("home", submission=True, **request.args))
    return render_template("newblog.html")

if __name__ == "__main__":
    app.debug = True
    app.run()