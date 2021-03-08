from flask import *

from base import app


@app.route('/admin/load_register', methods=['GET'])
def admin_load_register():
    return render_template('admin/register.html')
