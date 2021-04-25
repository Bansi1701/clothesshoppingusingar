from flask import *

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.state_dao import StateDAO
from base.com.vo.state_vo import StateVO


@app.route('/admin/load_state')
def admin_load_state():
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/addState.html')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_load_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_state', methods=['post'])
def admin_insert_state():
    try:
        if admin_login_session() == 'admin':

            state_vo = StateVO()
            state_dao = StateDAO()

            state_vo.state_name = request.form.get('stateName')
            state_vo.state_description = request.form.get('stateDescription')

            state_dao.insert_state(state_vo)

            return redirect(url_for('admin_view_state'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_insert_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_state', methods=['get'])
def admin_view_state():
    try:
        if admin_login_session() == 'admin':

            state_dao = StateDAO()
            state_vo_list = state_dao.view_state()
            return render_template('admin/viewState.html', state_vo_list=state_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_view_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_state', methods=['get'])
def admin_delete_state():
    try:
        if admin_login_session() == 'admin':

            state_vo = StateVO()
            state_dao = StateDAO()
            state_vo.state_id = request.args.get('stateId')
            state_dao.delete_state(state_vo)
            return redirect(url_for('admin_view_state'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        flash('Area or City is connected with this entity')
        print("admin_delete_state route exception occured>>>>>>>>>>", ex)
        return redirect(url_for('admin_view_state'))


@app.route('/admin/edit_state', methods=['get'])
def admin_edit_state():
    try:
        if admin_login_session() == 'admin':

            state_vo = StateVO()
            state_dao = StateDAO()
            state_vo.state_id = request.args.get('stateId')
            state_vo_list = state_dao.edit_state(state_vo)
            return render_template('admin/editState.html', state_vo_list=state_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_edit_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_state', methods=['post'])
def admin_update_state():
    try:
        if admin_login_session() == 'admin':

            state_vo = StateVO()
            state_dao = StateDAO()
            state_vo.state_id = request.form.get('stateId')
            state_vo.state_name = request.form.get('stateName')
            state_vo.state_description = request.form.get('stateDescription')

            state_dao.update_state(state_vo)
            return redirect(url_for('admin_view_state'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_update_state route exception occured>>>>>>>>>>", ex)
