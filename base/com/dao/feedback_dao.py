from base import database
from base.com.vo.feedback_vo import FeedbackVO
from base.com.vo.login_vo import LoginVO


class FeedbackDAO:
    def insert_feedback(self, feedback_vo):
        database.session.add(feedback_vo)
        database.session.commit()

    def user_view_feedback(self):
        feedback_vo_list = database.session.query(LoginVO, FeedbackVO) \
            .filter(LoginVO.login_id == FeedbackVO.feedback_login_id) \
            .all()
        return feedback_vo_list

    def admin_view_feedback(self):
        feedback_vo_list = database.session.query(FeedbackVO, LoginVO) \
            .join(LoginVO, FeedbackVO.feedback_login_id == LoginVO.login_id) \
            .all()
        return feedback_vo_list

    def delete_feedback(self, feedback_vo):
        feedback_vo_delete = FeedbackVO.query.get(feedback_vo.feedback_id)
        database.session.delete(feedback_vo_delete)
        database.session.commit()
