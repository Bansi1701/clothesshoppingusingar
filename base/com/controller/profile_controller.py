from flask import *

from base import app


@app.route('/admin/load_profile', methods=['GET'])
def admin_load_profile():
    return render_template('admin/profile.html')
