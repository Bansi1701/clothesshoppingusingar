from datetime import timedelta

from flask import render_template, redirect, request, url_for, make_response, flash

from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.dao.state_dao import StateDAO
from base.com.vo.login_vo import LoginVO

global_loginvo_list = []
global_login_secretkey_set = {0}


@app.route('/', methods=['GET'])
def load_login():
    try:
        state_dao = StateDAO()
        state_vo_list = state_dao.view_state()
        return render_template('user/login.html', state_vo_list=state_vo_list)
    except Exception as ex:
        print("load_login route exception occured>>>>>>>>>>", ex)


@app.route("/admin/validate_login", methods=['POST'])
def admin_validate_login():
    try:
        global global_loginvo_list
        global global_login_secretkey_set

        login_username = request.form.get('loginUsername')
        login_password = request.form.get('loginPassword')

        login_vo = LoginVO()
        login_dao = LoginDAO()

        login_vo.login_username = login_username
        login_vo.login_password = login_password

        login_vo_list = login_dao.validate_login(login_vo)
        login_list = [i.as_dict() for i in login_vo_list]
        print("in admin_validate_login login_list>>>>>>>>>>>", login_list)
        len_login_list = len(login_list)
        if len_login_list == 0:
            error_message = 'username or password is incorrect !'
            flash(error_message)
            return redirect('/')
        elif login_list[0]['login_status'] == 'inactive':
            error_message = 'You have been temporarily blocked by website admin !'
            flash(error_message)
            return redirect('/')
        else:
            for row1 in login_list:
                login_id = row1['login_id']
                login_username = row1['login_username']
                login_role = row1['login_role']
                login_secretkey = row1['login_secretkey']
                login_vo_dict = {
                    login_secretkey: {'login_username': login_username, 'login_role': login_role, 'login_id': login_id}}
                if len(global_loginvo_list) != 0:
                    for i in global_loginvo_list:
                        tempList = list(i.keys())
                        global_login_secretkey_set.add(tempList[0])
                    login_secretkey_list = list(global_login_secretkey_set)
                    if login_secretkey not in login_secretkey_list:
                        global_loginvo_list.append(login_vo_dict)
                else:
                    global_loginvo_list.append(login_vo_dict)
                if login_role == 'admin':
                    response = make_response(redirect(url_for('admin_load_dashboard')))
                    response.set_cookie('login_secretkey', value=login_secretkey, max_age=timedelta(minutes=30))
                    response.set_cookie('login_username', value=login_username, max_age=timedelta(minutes=30))
                    login_secretkey = request.cookies.get('login_secretkey')
                    login_username = request.cookies.get('login_username')
                    print("in admin_validate_login login_secretkey>>>>>>>>>>>>>>>", login_secretkey)
                    print("in admin_validate_login login_username>>>>>>>>>>>>>>>", login_username)
                    return response
                elif login_role == 'user':
                    response = make_response(redirect(url_for('user_load_dashboard')))
                    response.set_cookie('login_secretkey', value=login_secretkey, max_age=timedelta(minutes=30))
                    response.set_cookie('login_username', value=login_username, max_age=timedelta(minutes=30))
                    login_secretkey = request.cookies.get('login_secretkey')
                    login_username = request.cookies.get('login_username')
                    print("in user_validate_login login_secretkey>>>>>>>>>>>>>>>", login_secretkey)
                    print("in user_validate_login login_username>>>>>>>>>>>>>>>", login_username)
                    return response
                else:
                    return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_validate_login route exception occured>>>>>>>>>>", ex)


@app.route('/admin/load_dashboard', methods=['GET'])
def admin_load_dashboard():
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/index.html')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_load_dashboard route exception occured>>>>>>>>>>", ex)


@app.route('/user/load_dashboard', methods=['GET'])
def user_load_dashboard():
    try:
        if admin_login_session() == 'user':
            return render_template('user/index.html')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("user_load_dashboard route exception occured>>>>>>>>>>", ex)


@app.route('/admin/login_session')
def admin_login_session():
    try:
        global global_loginvo_list
        login_role_flag = ""
        print("before login_role_flag=", login_role_flag)
        print("before len(login_role_flag)>>>>>>>>>>", len(login_role_flag))

        login_secretkey = request.cookies.get('login_secretkey')
        print("in admin_login_session login_secretkey>>>>>>>>>", login_secretkey)

        if login_secretkey is None:
            return redirect('/')
        for i in global_loginvo_list:
            if login_secretkey in i.keys():
                if i[login_secretkey]['login_role'] == 'admin':
                    login_role_flag = "admin"
                if i[login_secretkey]['login_role'] == 'user':
                    login_role_flag = "user"

        print("after login_role_flag>>>>>>>>>>", login_role_flag)
        print("after len(login_role_flag)>>>>>>>>>>", len(login_role_flag))

        if len(login_role_flag) != 0:
            print("<<<<<<<<<<<<<<<<True>>>>>>>>>>>>>>>>>>>>")
        return login_role_flag
    except Exception as ex:
        print("admin_login_session route exception occured>>>>>>>>>>", ex)


@app.route("/admin/logout_session", methods=['GET'])
def admin_logout_session():
    try:
        global global_loginvo_list
        login_secretkey = request.cookies.get('login_secretkey')
        login_username = request.cookies.get('login_username')
        print("in admin_logout_session login_secretkey>>>>>>>>>", login_secretkey)
        print("in admin_logout_session login_username>>>>>>>>>", login_username)
        print("in admin_logout_session type of login_secretkey>>>>>>>>>", type(login_secretkey))
        print("in admin_logout_session type of login_username>>>>>>>>>", type(login_username))

        response = make_response(redirect('/'))
        if login_secretkey is not None and login_username is not None:
            response.set_cookie('login_secretkey', login_secretkey, max_age=0)
            response.set_cookie('login_username', login_username, max_age=0)
            for i in global_loginvo_list:
                if login_secretkey in i.keys():
                    global_loginvo_list.remove(i)
                    print("in admin_logout_session global_loginvo_list>>>>>>>>>>>>>>>", global_loginvo_list)
                    break

        return response
    except Exception as ex:
        print("in admin_logout_session route exception occured>>>>>>>>>>", ex)
