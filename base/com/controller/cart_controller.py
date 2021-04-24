from flask import *

from base import *
from base.com.dao.cart_dao import CartDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.product_dao import ProductDAO
from base.com.dao.user_dao import RegisterDAO
from base.com.vo.cart_vo import CartVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.product_vo import ProductVO
from base.com.vo.user_vo import RegisterVO


@app.route('/user/load_cart', methods=['GET'])
def user_load_cart():
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()
        user_vo = RegisterVO()
        user_dao = RegisterDAO()
        cart_vo = CartVO()
        cart_dao = CartDAO()
        product_vo = ProductVO()
        product_dao = ProductDAO()

        login_username = request.cookies.get('login_username')
        login_vo.login_username = login_username
        login_id = login_dao.find_login_id(login_vo)
        user_vo.user_login_id = login_id

        cart_vo.cart_user_id = user_dao.find_user_id(user_vo)
        cart_vo_list = cart_dao.view_cart_user_id(cart_vo)
        print("cart>>>>>>>>>>", cart_vo_list)
        product_vo_list = []
        for product in cart_vo_list:
            print(product.cart_product_id)
            temp_product = product_dao.selected_view_product(product.cart_product_id)
            product_vo_list.append([temp_product[0], product])
        print(product_vo_list)

        return render_template('user/cart.html', product_vo_list=product_vo_list)
    except Exception as ex:
        print("user_load_cart route exception occured>>>>>>>>>>", ex)


@app.route('/user/add_to_cart', methods=['get'])
def user_add_to_cart():
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()
        user_vo = RegisterVO()
        user_dao = RegisterDAO()
        cart_vo = CartVO()
        cart_dao = CartDAO()

        login_username = request.cookies.get('login_username')
        login_vo.login_username = login_username
        login_id = login_dao.find_login_id(login_vo)
        user_vo.user_login_id = login_id

        cart_user_id = user_dao.find_user_id(user_vo)
        cart_product_id = request.args.get('product_id')
        cart_vo_list = cart_dao.view_cart()

        print('cart_vo_list>>>>>', cart_vo_list)
        for product in cart_vo_list:
            print(type(cart_user_id))
            print(type(product.cart_user_id))
            print(type(cart_product_id))
            print(type(product.cart_product_id))
            if cart_user_id == product.cart_user_id and int(cart_product_id) == product.cart_product_id:
                flash("product is already in cart")
                return redirect(url_for('category_list'))
        else:
            cart_vo.cart_user_id = cart_user_id
            cart_vo.cart_product_id = cart_product_id
            cart_vo.product_quantity = 1
            cart_dao.insert_into_cart(cart_vo)
            return redirect(url_for('category_list'))

    except Exception as ex:
        print("user_add_to_cart route exception occured>>>>>>>>>>", ex)


@app.route('/user/remove_product_from_cart', methods=['get'])
def user_remove_product_from_cart():
    try:
        cart_vo = CartVO()
        cart_dao = CartDAO()

        cart_vo.cart_id = request.args.get('cart_id')
        cart_dao.delete_product_from_cart(cart_vo)

        return redirect(url_for('user_load_cart'))
    except Exception as ex:
        print("user_remove_product_from_cart route exception occured>>>>>>>>>>", ex)


@app.route('/ajax_product_quantity',methods=['get'])
def ajax_product_quantity():
    try:
        cart_vo = CartVO()
        cart_dao = CartDAO()
        cart_vo.cart_id=request.args.get('cart_id')
        cart_vo.product_quantity = request.args.get('count')
        cart_dao.update_cart(cart_vo)

    except Exception as ex:
        print("ajax_product_quantity route exception occured>>>>>>>>>>", ex)

