from flask import *

from base import *
from base.com.dao.cart_dao import CartDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.product_dao import ProductDAO
from base.com.dao.user_dao import RegisterDAO
from base.com.vo.cart_vo import CartVO
from base.com.vo.login_vo import LoginVO
from base.com.vo.user_vo import RegisterVO


@app.route('/user/checkout', methods=['GET'])
def user_checkout():
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()
        user_vo = RegisterVO()
        user_dao = RegisterDAO()
        cart_vo = CartVO()
        cart_dao = CartDAO()
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
        return render_template('user/checkout.html', product_vo_list=product_vo_list)
    except Exception as ex:
        print("user_checkout route exception occured>>>>>>>>>>", ex)


@app.route('/user/place_order', methods=['get'])
def user_place_order():
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()
        user_vo = RegisterVO()
        user_dao = RegisterDAO()
        cart_vo = CartVO()
        cart_dao = CartDAO()
        product_dao = ProductDAO()

        login_username = request.cookies.get('login_username')
        login_vo.login_username = login_username
        login_id = login_dao.find_login_id(login_vo)
        user_vo.user_login_id = login_id

        cart_vo.cart_user_id = user_dao.find_user_id(user_vo)
        cart_vo_list = cart_dao.view_cart_user_id(cart_vo)
        print("hhhhhhhhhhhhhhhhh>>>>>>>>", cart_vo.cart_user_id)
        product_vo_list = []
        for product in cart_vo_list:
            print(product.cart_product_id)
            temp_product = product_dao.selected_view_product(product.cart_product_id)
            product_vo_list.append([temp_product[0], product])

        for product in product_vo_list:
            cart_vo.cart_id=product[1].cart_id
            cart_dao.delete_cart(cart_vo)

        return redirect(url_for('user_load_dashboard'))
    except Exception as ex:
        print("user_remove_product_from_cart route exception occured>>>>>>>>>>", ex)
