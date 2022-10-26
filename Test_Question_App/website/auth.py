from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import current_user

auth = Blueprint('auth', __name__)


@auth.route('/admin-sign-in', methods=['GET', 'POST'])
def sign_in():
    return render_template("admin_sign_in.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/questionnaire',  methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        title = request.form.get('title')
        role = request.form.get('role')
        reports_to = request.form.get('reportsTo')
        fun_fact = request.form.get('funFact')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(title) < 2:
            flash('Title must be greater than 1 character.', category='error')
        elif len(role) < 2:
            flash('Role must be greater than 1 character.', category='error')
        elif len(reports_to) < 2:
            flash('Who you report to must be greater than 1 character.',
                  category='error')
        elif len(fun_fact) < 2:
            flash('Fun-fact must be greater than 1 character.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name,
                            title=title, role=role, reports_to=reports_to, fun_fact=fun_fact)
            db.session.add(new_user)
            db.session.commit()
            flash('Questionarrie Completed!', category='success')
            return redirect(url_for('views.home'))

    return render_template("questionnaire.html", user=current_user)
