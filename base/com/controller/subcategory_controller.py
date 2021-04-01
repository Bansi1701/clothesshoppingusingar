from flask import *

from base import app
from flask import *
from base import app

from base.com.controller.login_controller import admin_login_session
from base.com.dao.category_dao import CategoryDAO
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.subcategory_vo import SubCategoryVO


@app.route('/admin/load_subcategory', methods=['get'])
def admin_load_subcategory():
    try:
        if admin_login_session() == 'admin':
            category_dao = CategoryDAO()
            category_vo_list = category_dao.view_category()
            return render_template('admin/addSubcategory.html', category_vo_list=category_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print('admin_view_category route exception occured>>>>>>>>>>', ex)


@app.route('/admin/insert_subcategory', methods=['post'])
def admin_insert_subcategory():
    try:
        if admin_login_session() == 'admin':
            subcategory_vo = SubCategoryVO()
            subcategory_dao = SubCategoryDAO()

            subcategory_vo.subcategory_name = request.form.get('subcategoryName')
            subcategory_vo.subcategory_description = request.form.get('subcategoryDescription')
            subcategory_vo.subcategory_category_id = request.form.get('categoryId')

            subcategory_dao.insert_subcategory(subcategory_vo)
            return redirect(url_for('admin_view_subcategory'))
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_insert_subcategory route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_subcategory', methods=['get'])
def admin_view_subcategory():
    try:
        if admin_login_session() == 'admin':
            subcategory_dao = SubCategoryDAO()
            subcategory_vo_list = subcategory_dao.view_subcategory()
            return render_template('admin/viewSubcategory.html', subcategory_vo_list=subcategory_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_view_subcategory route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_subcategory', methods=['GET'])
def admin_delete_subcategory():
    try:
        if admin_login_session() == 'admin':
            subcategory_dao = SubCategoryDAO()
            subcategory_id = request.args.get('subcategoryId')
            subcategory_dao.delete_subcategory(subcategory_id)
            return redirect(url_for('admin_view_subcategory'))
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("in admin_delete_subcategory route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_subcategory', methods=['GET'])
def admin_edit_subcategory():
    try:
        if admin_login_session() == 'admin':
            subcategory_vo = SubCategoryVO()
            subcategory_dao = SubCategoryDAO()
            category_dao = CategoryDAO()

            subcategory_vo.subcategory_id = request.args.get('subcategoryId')
            subcategory_vo_list = subcategory_dao.edit_subcategory(subcategory_vo)
            category_vo_list = category_dao.view_category()
            return render_template('admin/editSubcategory.html', category_vo_list=category_vo_list,
                                   subcategory_vo_list=subcategory_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("in admin_edit_subcategory route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_subcategory', methods=['POST'])
def admin_update_subcategory():
    try:
        if admin_login_session() == 'admin':
            subcategory_vo = SubCategoryVO()
            subcategory_dao = SubCategoryDAO()

            subcategory_vo.subcategory_id = request.form.get('subcategoryId')
            subcategory_vo.subcategory_name = request.form.get('subcategoryName')
            subcategory_vo.subcategory_description = request.form.get('subcategoryDescription')
            subcategory_vo.subcategory_category_id = request.form.get('subcategoryCategoryId')
            subcategory_dao.update_subcategory(subcategory_vo)
            return redirect(url_for('admin_view_subcategory'))
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("in admin_update_subcategory route exception occured>>>>>>>>>>", ex)
