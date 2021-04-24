from base import database
from base.com.vo.product_vo import ProductVO


class CartVO(database.Model):
    __tablename__ = 'cart_table'
    cart_id = database.Column('cart_id', database.Integer, primary_key=True, autoincrement=True)
    cart_user_id = database.Column('cart_user_id', database.Integer)
    cart_product_id = database.Column('cart_product_id', database.Integer)
    product_quantity = database.Column('product_quantity', database.Integer)

    def as_dict(self):
        return {
            'cart_id': self.cart_id,
            'cart_user_id': self.cart_user_id,
            'cart_product_id': self.cart_product_id,
            'product_quantity': self.product_quantity
        }


database.create_all()
