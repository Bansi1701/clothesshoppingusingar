from flask import render_template,redirect,url_for,request
from base import app

@app.route('/user', methods=['GET'])
def user():
    try:
        return render_template('user/index.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/shop', methods=['GET'])
def shop():
    try:
        return render_template('user/category-list.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/cart', methods=['GET'])
def cart():
    try:
        return render_template('user/cart.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/checkout', methods=['GET'])
def checkout():
    try:
        return render_template('user/checkout.html')
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


@app.route('/user/category-list', methods=['GET'])
def category_list():
    try:
        return render_template('user/category-list.html')
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









