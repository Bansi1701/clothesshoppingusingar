from flask import *
from base import app

from base.com.controller.login_controller import admin_login_session
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


@app.route('/admin/load_category')
def admin_load_category():
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/addCategory.html')
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_load_category route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_category', methods=['post'])
def admin_insert_category():
    try:
        if admin_login_session() == 'admin':

            category_vo = CategoryVO()
            category_dao = CategoryDAO()

            category_vo.category_name = request.form.get('categoryName')
            category_vo.category_description = request.form.get('categoryDescription')

            category_dao.insert_category(category_vo)

            return redirect(url_for('admin_view_category'))

        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_insert_category route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_category', methods=['get'])
def admin_view_category():
    try:
        if admin_login_session() == 'admin':

            category_dao = CategoryDAO()
            category_vo_list = category_dao.view_category()
            return render_template('admin/viewCategory.html', category_vo_list=category_vo_list)

        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_view_category route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_category', methods=['get'])
def admin_delete_category():
    try:
        if admin_login_session() == 'admin':

            category_vo = CategoryVO()
            category_dao = CategoryDAO()
            category_vo.category_id = request.args.get('categoryId')
            category_dao.delete_category(category_vo)
            return redirect(url_for('admin_view_category'))

        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        flash('Subcategory is connected with this category')
        print("admin_delete_category route exception occured>>>>>>>>>>", ex)
        return redirect(url_for('admin_view_category'))


@app.route('/admin/edit_category', methods=['get'])
def admin_edit_category():
    try:
        if admin_login_session() == 'admin':

            category_vo = CategoryVO()
            category_dao = CategoryDAO()
            category_vo.category_id = request.args.get('categoryId')
            category_vo_list = category_dao.edit_category(category_vo)
            return render_template('admin/editCategory.html', category_vo_list=category_vo_list)

        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_edit_category route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_category', methods=['post'])
def admin_update_category():
    try:
        if admin_login_session() == 'admin':

            category_vo = CategoryVO()
            category_dao = CategoryDAO()
            category_vo.category_id = request.form.get('categoryId')
            category_vo.category_name = request.form.get('categoryName')
            category_vo.category_description = request.form.get('categoryDescription')

            category_dao.update_category(category_vo)
            return redirect(url_for('admin_view_category'))

        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_update_category route exception occured>>>>>>>>>>", ex)
