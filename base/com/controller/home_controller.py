from flask import *
from base import app


@app.route('/')
def admin_load_dashboard():
    try:
        return render_template('admin/index.html')
    except Exception as ex:
        print("admin_load_dashboard route exception occured>>>>>>>>>>", ex)
