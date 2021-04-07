from base import database
from base.com.vo.login_vo import LoginVO


class FeedbackVO(database.Model):
    __tablename__ = "feedback_table"
    feedback_id = database.Column("feedback_id", database.Integer, primary_key=True, autoincrement=True)
    feedback_description = database.Column("feedback_description", database.String(255), nullable=False)
    feedback_rating = database.Column("feedback_rating", database.Integer, nullable=False)
    feedback_datetime = database.Column("feedback_datetime", database.DateTime)
    feedback_login_id = database.Column("feedback_login_id", database.Integer, database.ForeignKey(LoginVO.login_id))

    def as_di1ct(self):
        return {
            "feedback_id": self.feedback_id,
            "feedback_description": self.feedback_description,
            "feedback_rating": self.feedback_rating,
            "feedback_datetime": self.feedback_datetime,
            "feedback_login_id": self.feedback_login_id,
        }


database.create_all()
