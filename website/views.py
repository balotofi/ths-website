#PUTTY: c:users/myname/.ssh/known hosts - 192.168.181.192 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKp3IEyYqW9zzqpsXPzVt/OZZQk8FD0PXxB9E5ealC2fONqT2Vj6bZnJ0wPP7evTx8PKFfJENfsnoQDZLtMhTP0=
#from xmlrpc.client import boolean

from flask import Blueprint, render_template

#from flask_login import login_required, current_user
#from . import db

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

@views.route('/results', methods=['GET', 'POST'])
# @login_required
def results():
#     if request.method == 'POST':
#         note = request.form.get('note')
    return render_template("results.html") #(user=current_user)

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/gallery')
def gallery():
    return render_template("gallery.html")

@views.route('/parent_dashboard')
def parent_dashboard():
    return render_template("parent_dashboard.html")

@views.route('/teacher_dashboard')
def teacher_dashboard():
    return render_template("teacher_dashboard.html")
