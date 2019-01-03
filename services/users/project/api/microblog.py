#!/usr/bin/env python
# -*- coding:utf-8 -*
# @Author   : Zhxu
# @Time     : 19-1-2 下午9:28

# services/users/project/api/microblog.py


from flask import Blueprint, request, render_template,\
    flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, \
    login_required
from werkzeug.urls import url_parse

from project.api.models import User
from project.api.forms import LoginForm

# Blueprint config
blog_blueprint = Blueprint('blog', __name__, template_folder='./templates')


# Demo for Jinja Templates
@blog_blueprint.route('/posts')
@blog_blueprint.route('/posts/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('posts.html', posts=posts)


@blog_blueprint.route('/posts/login', methods=['GET', 'POST'])
def login():
    # deal with a weird situation - current user has already logged in
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        # for POST method
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('blog.login'))

        # validation passed, then register the user as logged in,
        # so that means that any future pages the user navigates to
        # will have the current_user variable set to that user
        login_user(user, remember=form.remember_me.data)

        # When a user that is not logged in accesses a view,
        # redirect back origin URL after login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('blog.index')
        return redirect(next_page)

    # for GET method
    return render_template('login.html', title='Sign In', form=form)


@blog_blueprint.route('/posts/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.index'))
