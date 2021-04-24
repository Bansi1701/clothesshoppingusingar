from flask import render_template

from base import app
from base.com.dao.product_dao import ProductDAO


@app.route('/user', methods=['GET'])
def user():
    try:
        return render_template('user/index.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)



@app.route('/user/dashboard', methods=['GET'])
def dashboard():
    try:
        return render_template('user/dashboard.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/category-boxed', methods=['GET'])
def category_boxed():
    try:
        return render_template('user/category-boxed.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/category-4cols', methods=['GET'])
def category_list():
    try:
        product_dao = ProductDAO()
        product_vo_list = product_dao.view_product()
        print("product>>>>>>>>", product_vo_list)
        return render_template('user/category-4cols.html', product_vo_list=product_vo_list)
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/blog-listing', methods=['GET'])
def blog_listing():
    try:
        return render_template('user/blog-listing.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/faqs', methods=['GET'])
def faqs():
    try:
        return render_template('user/faq.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/404', methods=['GET'])
def error_404():
    try:
        return render_template('user/404.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/about', methods=['GET'])
def about():
    try:
        return render_template('user/about.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/contact', methods=['GET'])
def contact():
    try:
        return render_template('user/contact.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/login', methods=['GET'])
def login():
    try:
        return render_template('user/login.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/product-extended', methods=['GET'])
def product_extended():
    try:
        return render_template('user/product-extended.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/men_bottom_wear', methods=['GET'])
def men_bottom_wear():
    try:
        product_dao = ProductDAO()
        product_vo_list = product_dao.view_product()
        print("product>>>>>>>>", product_vo_list)
        return render_template('user/men_bottom_wear.html', product_vo_list=product_vo_list)
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/men_upper_wear', methods=['GET'])
def men_upper_wear():
    try:
        product_dao = ProductDAO()
        product_vo_list = product_dao.view_product()
        print("product>>>>>>>>", product_vo_list)
        return render_template('user/men_upper_wear.html', product_vo_list=product_vo_list)
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/children_upper_wear', methods=['GET'])
def children_upper_wear():
    try:
        product_dao = ProductDAO()
        product_vo_list = product_dao.view_product()
        print("product>>>>>>>>", product_vo_list)
        return render_template('user/children_upper_wear.html', product_vo_list=product_vo_list)
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/children_outfit', methods=['GET'])
def children_outfit():
    try:
        product_dao = ProductDAO()
        product_vo_list = product_dao.view_product()
        print("product>>>>>>>>", product_vo_list)
        return render_template('user/children_outfit.html', product_vo_list=product_vo_list)
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)
