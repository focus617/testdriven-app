#!/usr/bin/env python
# -*- coding:utf-8 -*
# @Author   : Zhxu
# @Time     : 19-1-2 下午9:28

# services/users/project/api/microblog.py


from flask import Blueprint, jsonify, request, render_template

# Blueprint config
blog_blueprint = Blueprint('microblog', __name__, template_folder='./templates')


# Demo for Jinja Templates
@blog_blueprint.route('/posts', methods=['GET'])
@blog_blueprint.route('/posts/index', methods=['GET'])
def index():
    user = {'username': 'Zhiyong'}
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
    return render_template('posts.html', title="Zhiyong's", user=user, posts=posts)
