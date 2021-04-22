import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import *

from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.dao.user_dao import RegisterDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.user_vo import RegisterVO


@app.route('/user_register', methods=['POST'])
def user_register():
    login_dao = LoginDAO()
    login_vo = LoginVO()

    login_username = request.form.get('userEmail')

    login_secretkey = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(32))
    print("in user_insert_user login_secretkey>>>>>>>", login_secretkey)
    login_vo_list = login_dao.view_login()
    print("in user_insert_user login_vo_list>>>>>>", login_vo_list)
    if len(login_vo_list) != 0:
        for i in login_vo_list:
            if i.login_secretkey == login_secretkey:
                login_secretkey = ''.join(
                    (random.choice(string.ascii_letters + string.digits)) for x in range(32))
            elif i.login_username == login_username:
                error_message = "The username is already exists !"
                flash(error_message)
                return redirect(url_for('load_login'))

    login_password = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
    print("in user_insert_user login_password>>>>>>>>>", login_password)

    sender = "noreply.fooday@gmail.com"
    receiver = login_username
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "PYTHON PASSWORD"
    msg.attach(MIMEText(login_password, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    '''Pass word add akr'''
    server.login(sender, "LOL@12345")
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

    login_vo.login_role = 'user'
    login_vo.login_status = 'active'
    login_vo.login_username = login_username
    login_vo.login_password = login_password
    login_vo.login_secretkey = login_secretkey

    login_dao.insert_user(login_vo)

    register_vo = RegisterVO()
    register_dao = RegisterDAO()
    register_vo.user_firstname = request.form.get('firstName')
    register_vo.user_lastname = request.form.get('lastName')
    register_vo.user_gender = request.form.get('gender')
    register_vo.user_address = request.form.get('address')
    register_vo.user_pincode = request.form.get('pincode')
    register_vo.user_state_id = request.form.get('stateId')
    register_vo.user_city_id = request.form.get('cityId')
    register_vo.user_login_id = login_vo.login_id
    register_dao.insert_user(register_vo)

    return redirect('/')
