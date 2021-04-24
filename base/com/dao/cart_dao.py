from base.com.vo.cart_vo import *
from base.com.vo.product_vo import *


class CartDAO:

    def insert_into_cart(self, cart_vo):
        database.session.add(cart_vo)
        database.session.commit()

    def view_cart(self):
        state_vo_list = CartVO.query.all()
        return state_vo_list

    def view_cart_user_id(self,cart_vo):
        cart_vo_list = CartVO.query.filter_by(cart_user_id=cart_vo.cart_user_id).all()
        return cart_vo_list

    def delete_product_from_cart(self, cart_vo):
        cart_vo_list = CartVO.query.get(cart_vo.cart_id)
        database.session.delete(cart_vo_list)
        database.session.commit()

    def update_cart(self, cart_vo):
        database.session.merge(cart_vo)
        database.session.commit()

    def delete_cart(self, cart_vo):
        cart_vo_list = CartVO.query.get(cart_vo.cart_id)
        database.session.delete(cart_vo_list)
        database.session.commit()
