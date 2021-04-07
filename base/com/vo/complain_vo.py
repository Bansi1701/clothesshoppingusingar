from base import database
from base.com.vo.login_vo import LoginVO


class ComplainVO(database.Model):
    __tablename__ = "complain_table"
    complain_id = database.Column("complain_id", database.Integer, primary_key=True, autoincrement=True)
    complain_subject = database.Column("complain_subject", database.String(255), nullable=False)
    complain_description = database.Column("complain_description", database.String(255), nullable=False)
    complain_datetime = database.Column("complain_datetime", database.DateTime)
    complain_status = database.Column("complain_status", database.String(20))
    complain_from_login_id = database.Column("complain_from_login_id", database.Integer, database.ForeignKey(LoginVO.login_id))
    complain_to_login_id = database.Column("complain_to_login_id", database.Integer, database.ForeignKey(LoginVO.login_id))
    complain_reply_description = database.Column("complain_reply_description", database.String(255))
    complain_reply_datetime = database.Column("complain_reply_datetime", database.DateTime)

    def as_di1ct(self):
        return {
            "complain_id": self.complain_id,
            "complain_subject": self.complain_subject,
            "complain_description": self.complain_description,
            "complain_datetime": self.complain_datetime,
            "complain_status": self.complain_status,
            "complain_from_login_id": self.complain_from_login_id,
            "complain_to_login_id": self.complain_to_login_id,
            "complain_reply_description": self.complain_reply_description,
            "complain_reply_datetime": self.complain_reply_datetime,
        }


database.create_all()
