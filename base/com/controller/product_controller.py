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
            product_dao=ProductDAO()

            product_vo.product_category_name=request.form.get('productCategoryId')
            product_vo.product_subcategory_name=request.form.get('productSubcategoryId')
            product_vo.product_name=request.form.get('productName')
            product_vo.product_description=request.form.get('productDescription')
            product_vo.product_price=request.form.get('productPrice')

            product_dao.insert_product(product_vo)
            return redirect(url_for('admin_view_product'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_insert_product route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_product')
def admin_view_product():
    try:
        if admin_login_session() == 'admin':

            product_dao=ProductDAO()
            product_vo_list = product_dao.view_product()
            print(product_vo_list)
            return render_template('admin/viewProduct.html', product_vo_list=product_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_view_product route exception occured>>>>>>>>>>", ex)



@app.route('/admin/delete_product', methods=['GET'])
def admin_delete_product():
    try:
        if admin_login_session() == 'admin':

            product_dao = ProductDAO()
            product_id = request.args.get('productId')
            product_dao.delete_product(product_id)
            return redirect(url_for('admin_view_product'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("in admin_delete_product route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_product', methods=['GET'])
def admin_edit_product():
    try:
        if admin_login_session() == 'admin':

            product_vo = ProductVO()
            product_dao = ProductDAO()
            category_dao = CategoryDAO()
            subcategory_vo = SubCategoryVO()
            subcategory_dao = SubCategoryDAO()

            product_vo.product_id = request.args.get('productId')
            subcategory_vo.subcategory_category_id = request.args.get('categoryId')
            product_vo_list = product_dao.edit_product(product_vo)
            category_vo_list = category_dao.view_category()
            subcategory_vo_list = subcategory_dao.view_ajax_product_subcategory(subcategory_vo)
            return render_template('admin/editProduct.html',product_vo_list=product_vo_list,
                                   category_vo_list=category_vo_list,subcategory_vo_list=subcategory_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("in admin_edit_product route exception occured>>>>>>>>>>", ex)



@app.route('/admin/update_product', methods=['POST'])
def admin_update_product():
    try:
        if admin_login_session() == 'admin':

            product_vo=ProductVO()
            product_dao=ProductDAO()

            product_vo.product_id = request.form.get('productId')
            product_vo.product_category_name=request.form.get('productCategoryId')
            product_vo.product_subcategory_name=request.form.get('productSubcategoryId')
            product_vo.product_name=request.form.get('productName')
            product_vo.product_description=request.form.get('productDescription')
            product_vo.product_price=request.form.get('productPrice')

            product_dao.update_product(product_vo)
            return redirect(url_for('admin_view_product'))
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_update_product route exception occured>>>>>>>>>>", ex)






