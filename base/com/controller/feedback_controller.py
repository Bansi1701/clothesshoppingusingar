import datetime

from base import app
from base.com.controller.login_controller import *
from base.com.dao.feedback_dao import FeedbackDAO
from base.com.vo.feedback_vo import FeedbackVO


@app.route('/admin/load_complaints', methods=['GET'])
def admin_load_complaints():
    return render_template('admin/viewComplaints.html')


@app.route('/admin/reply_complaint', methods=['GET'])
def admin_reply_complaint():
    return render_template('admin/addReply.html')


@app.route('/admin/view_feedbacks', methods=['GET'])
def admin_view_feedback():
    try:
        if admin_login_session() == 'admin':
            feedback_dao = FeedbackDAO()

            feedback_vo_list = feedback_dao.admin_view_feedback()
            return render_template("admin/viewFeedbacks.html", feedback_vo_list=feedback_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_view_feedback route exception occured>>>>>>>>>>", ex)

@app.route('/user/load_feedback', methods=['GET'])
def user_load_feedback():
    try:
        if admin_login_session() == 'user':
            return redirect("/user/view_feedback")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in user_load_feedback route exception occured>>>>>>>>>>", ex)


@app.route('/user/insert_feedback', methods=['POST'])
def user_insert_feedback():
    try:
        if admin_login_session() == 'user':
            feedback_rating = request.form.get("rating")
            feedback_description = request.form.get("feedbackDescription")
            feedback_date = datetime.datetime.now()
            print(">>>>>>>>>", feedback_rating, type(feedback_rating))

            feedback_dao = FeedbackDAO()
            feedback_vo = FeedbackVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            feedback_vo.feedback_rating = feedback_rating
            feedback_vo.feedback_description = feedback_description
            feedback_vo.feedback_datetime = feedback_date
            feedback_vo.feedback_login_id = login_id
            print('data>>>>>>>>>', feedback_vo.feedback_login_id)

            feedback_dao.insert_feedback(feedback_vo)
            return redirect(url_for('user_view_feedback'))
        else:
            return admin_logout_session()

    except Exception as ex:
        print("in user_add_feedback route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_feedback', methods=['GET'])
def user_view_feedback():
    try:
        if admin_login_session() == 'user':
            feedback_dao = FeedbackDAO()
            feedback_vo = FeedbackVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)
            feedback_vo.feedback_login_id = login_id
            feedback_vo_list = feedback_dao.user_view_feedback()
            print("feedback_vo_list>>>>>>>>", feedback_vo_list)

            return render_template("user/viewFeedback.html", feedback_vo_list=feedback_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in user_view_feedback route exception occured>>>>>>>>>>", ex)
