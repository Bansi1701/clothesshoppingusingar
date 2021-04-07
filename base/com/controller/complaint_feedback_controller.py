from flask import *

from base import app


@app.route('/admin/load_complaints', methods=['GET'])
def admin_load_complaints():
    return render_template('admin/viewComplaints.html')


@app.route('/admin/reply_complaint', methods=['GET'])
def admin_reply_complaint():
    return render_template('admin/replyComplain.html')


@app.route('/admin/view_feedbacks', methods=['GET'])
def admin_view_feedbacks():
    return render_template('admin/viewFeedbacks.html')
