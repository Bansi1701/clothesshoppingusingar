from flask import *

from base import *


@app.route('/user/cart', methods=['GET'])
def cart():
    try:
        return render_template('user/cart.html')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)
