from flask import *

from base import app
from base.com.dao.state_dao import StateDAO
from base.com.vo.state_vo import StateVO


@app.route('/admin/load_state')
def admin_load_state():
    try:
        return render_template('admin/addState.html')

    except Exception as ex:
        print("admin_load_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_state', methods=['post'])
def admin_insert_state():
    try:
        state_vo = StateVO()
        state_dao = StateDAO()

        state_vo.state_name = request.form.get('state_name')
        state_vo.state_description = request.form.get('state_description')

        state_dao.insert_state(state_vo)

        return redirect(url_for('admin_view_state'))

    except Exception as ex:
        print("admin_insert_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_state', methods=['get'])
def admin_view_state():
    try:
        state_dao = StateDAO()
        state_vo_list = state_dao.view_state()
        return render_template('admin/viewState.html', state_vo_list=state_vo_list)

    except Exception as ex:
        print("admin_view_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_state', methods=['get'])
def admin_delete_state():
    try:
        state_vo = StateVO()
        state_dao = StateDAO()
        state_vo.state_id = request.args.get('state_id')
        state_dao.delete_state(state_vo)
        return redirect(url_for('admin_view_state'))

    except Exception as ex:
        print("admin_delete_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_state', methods=['get'])
def admin_edit_state():
    try:
        state_vo = StateVO()
        state_dao = StateDAO()
        state_vo.state_id = request.args.get('state_id')
        state_vo_list = state_dao.edit_state(state_vo)
        return render_template('admin/editState.html', state_vo_list=state_vo_list)

    except Exception as ex:
        print("admin_edit_state route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_state', methods=['post'])
def admin_update_state():
    try:
        state_vo = StateVO()
        state_dao = StateDAO()
        state_vo.state_id = request.form.get('state_id')
        state_vo.state_name = request.form.get('state_name')
        state_vo.state_description = request.form.get('state_description')

        state_dao.update_state(state_vo)
        return redirect(url_for('admin_view_state'))

    except Exception as ex:
        print("admin_update_state route exception occured>>>>>>>>>>", ex)
