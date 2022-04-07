
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/parents')
def parents():
    return render_template("parents.html")

@views.route('/vacancies')
def vacancies():
    return render_template("vacancies.html")

@views.route('/news')
def news():
    return render_template("news.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")