#!/usr/bin/env python
# -*- coding:utf-8 -*
# @Author   : Zhxu
# @Time     : 18-12-29 下午3:58

# services/users/project/api/users.py


from flask import Blueprint, jsonify


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
