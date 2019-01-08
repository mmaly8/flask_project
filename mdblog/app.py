from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja", text="takto vies menit text")

@flask_app.route("/about/")
def view_about():
    return render_template("about.jinja")

@flask_app.route("/articles/")
def view_articles():
    return render_template("articles.jinja")

@flask_app.route("/admin/")
def view_admin():
    return render_template("admin.jinja")

"""
@flask_app.route("/admin/")
def view_admin():
    return "Hello Admin"

@flask_app.route("/admin/<string:name>/")
def view_admin_name(name):
    return "Hello {}".format(name)
"""
