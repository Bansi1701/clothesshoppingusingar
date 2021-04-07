from flask import *

from base import app
from base.com.vo.register_vo import RegisterVO


@app.route('/user_register', methods=['POST'])
def user_register():
    register_vo = RegisterVO()
    register_vo.user_firstname=request.form.get('firstName')
    register_vo.user_lastname = request.form.get('lastName')
    register_vo.user_firstname = request.form.get('gender')
    register_vo.user_firstname = request.form.get('firstName')
    register_vo.user_firstname = request.form.get('firstName')
    register_vo.user_firstname = request.form.get('firstName')
    register_vo.user_firstname = request.form.get('firstName')
    register_vo.user_firstname = request.form.get('firstName')
    return render_template('admin/register.html')
