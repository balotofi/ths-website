# from flask import Blueprint, render_template, request, flash, redirect, url_for 
# from .models import User
# from werkzeug.security import generate_password_hash, check_password_hash
# from . import db
# from flask_login import login_user, login_required, logout_user, current_user


# auth = Blueprint('auth', __name__)

# @auth.route('/results', methods=['GET', 'POST'])
# def results_login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 flash('Logged in successfully!', category='success')
#                 login_user(user, remember=True)
#                 return redirect(url_for('views.results'))
#             else:
#                 flash('Incorrect password, try again.', category='error')
#         else:
#             flash('Email does not exist.', category='error')

#     return render_template("results.html", user=current_user)

# @auth.route('/logout')
# # @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth.results_login'))

# @auth.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         first_name = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email already exists.', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than three characters.', category='error')
#         elif len(first_name) < 2:
#             flash('First name must be greater than two characters.', category='error')
#         elif password1 != password2:
#             flash('The password entered do not match', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least seven characters.', category='error')
#         else:
#             #add user to database
#             new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(user, remember=True)
#             flash('Account created!', category='success')
#             return redirect(url_for('views.home'))

#     return render_template("sign_up.html", user=current_user)

# # @auth.route(/about)
# # def about():
# #     return render_template(about.html)

# # @auth.route(/parents)
# # def parents():
# #     return render_template(parents.html)

# # @auth.route(/classes)
# # def classes():
# #     return render_template(classes.html)

# # @auth.route(/news)
# # def news():
# #     return render_template(news.html)

# # @auth.route(/calendar)
# # def calendar():
# #     return render_template(calendar.html)

# # @auth.route(/contact)
# # def contact():
# #     return render_template(contact.html)