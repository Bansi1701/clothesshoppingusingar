from flask import *

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.area_dao import AreaDAO
from base.com.dao.city_dao import CityDAO
from base.com.dao.state_dao import StateDAO
from base.com.vo.area_vo import AreaVO
from base.com.vo.city_vo import CityVO
from base.com.vo.state_vo import StateVO


@app.route('/admin/load_area', methods=['get'])
def admin_load_area():
    try:
        if admin_login_session() == 'admin':
            state_dao = StateDAO()
            state_vo_list = state_dao.view_state()
            return render_template('admin/addArea.html', state_vo_list=state_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print('admin_load_area route exception occured>>>>>>>>>>', ex)


@app.route('/admin/ajax_area_city', methods=['get'])
def admin_ajax_area_city():
    try:
        if admin_login_session() == 'admin':

            city_dao = CityDAO()
            city_vo = CityVO()

            city_vo.city_state_id = request.args.get('stateId')
            city_vo_list = city_dao.view_ajax_area_city(city_vo)

            ajax_area_city = [i.as_dict() for i in city_vo_list]

            return jsonify(ajax_area_city)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print('admin_ajax_area_city route exception occured>>>>>>>>>>', ex)


@app.route('/admin/insert_area', methods=['post'])
def admin_add_area():
    try:
        if admin_login_session() == 'admin':

            area_vo = AreaVO()
            area_dao = AreaDAO()

            area_vo.area_name = request.form.get('areaName')
            area_vo.area_pincode = request.form.get('areaPincode')
            area_vo.area_city_id = request.form.get('areaCityId')
            area_vo.area_state_id = request.form.get('areaStateId')

            area_dao.insert_area(area_vo)
            return redirect(url_for('admin_view_area'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_insert_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_area', methods=['get'])
def admin_view_area():
    try:
        if admin_login_session() == 'admin':

            area_dao = AreaDAO()
            area_vo_list = area_dao.view_area()
            print(area_vo_list)
            return render_template('admin/viewArea.html', area_vo_list=area_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_view_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_area', methods=['get'])
def admin_delete_area():
    try:
        if admin_login_session() == 'admin':

            area_dao = AreaDAO()
            area_id = request.args.get('areaId')
            area_dao.delete_area(area_id)
            return redirect(url_for('admin_view_area'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("in admin_delete_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_area', methods=['get'])
def admin_edit_area():
    try:
        if admin_login_session() == 'admin':

            area_vo = AreaVO()
            area_dao = AreaDAO()
            state_dao = StateDAO()
            state_vo = StateVO()
            city_vo = CityVO()
            city_dao = CityDAO()

            area_vo.area_id = request.args.get('areaId')
            city_vo.city_state_id = request.args.get('stateId')
            area_vo_list = area_dao.edit_area(area_vo)
            state_vo_list = state_dao.view_state()
            city_vo_list = city_dao.view_ajax_area_city(city_vo)
            return render_template('admin/editArea.html', state_vo_list=state_vo_list,
                                   area_vo_list=area_vo_list, city_vo_list=city_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("in admin_edit_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_area', methods=['POST'])
def admin_update_area():
    try:
        if admin_login_session() == 'admin':

            area_vo = AreaVO()
            area_dao = AreaDAO()

            area_vo.area_id = request.form.get('areaId')
            area_vo.area_name = request.form.get('areaName')
            area_vo.area_pincode = request.form.get('areaPincode')
            area_vo.area_city_id = request.form.get('cityId')
            area_vo.area_state_id = request.form.get('stateId')

            area_dao.update_area(area_vo)
            return redirect(url_for('admin_view_area'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("in admin_update_area route exception occured>>>>>>>>>>", ex)
