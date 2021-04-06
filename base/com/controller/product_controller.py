from flask import *
from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO


@app.route('/admin/load_product')
def admin_load_product():
    try:
        if admin_login_session() == 'admin':
            category_dao = CategoryDAO()
            category_vo_list = category_dao.view_category()
            return render_template('admin/addProduct.html', category_vo_list=category_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print('admin_load_product route exception occured>>>>>>>>>>', ex)


@app.route('/admin/ajax_subcategory_product')
def admin_ajax_subcategory_product():
    try:
        if admin_login_session() == 'admin':

            subcategory_dao = SubCategoryDAO()
            subcategory_vo =SubCategoryVO()

            subcategory_vo.subcategory_category_id = request.args.get('productCategoryId')
            subcategory_vo_list = subcategory_dao.view_ajax_product_subcategory(subcategory_vo)

            ajax_product_subcategory = [i.as_dict() for i in subcategory_vo_list]

            return jsonify(ajax_product_subcategory)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print('admin_ajax_subcategory_product route exception occured>>>>>>>>>>', ex)


@app.route('/admin/insert_product',methods=['post'])
def admin_insert_product():
    try:
        if admin_login_session() == 'admin':

            product_vo=ProductVO()

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



