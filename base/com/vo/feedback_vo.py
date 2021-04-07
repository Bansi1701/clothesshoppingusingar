from base import database
from base.com.vo.login_vo import LoginVO


class FeedatabaseackVO(database.Model):
    __tablename__ = "feedatabaseack_table"
    feedatabaseack_id = database.Column("feedatabaseack_id", database.Integer, primary_key=True, autoincrement=True)
    feedatabaseack_description = database.Column("feedatabaseack_description", database.String(255), nullable=False)
    feedatabaseack_rating = database.Column("feedatabaseack_rating", database.Integer, nullable=False)
    feedatabaseack_datetime = database.Column("feedatabaseack_datetime", database.DateTime)
    feedatabaseack_login_id = database.Column("feedatabaseack_login_id", database.Integer, database.ForeignKey(LoginVO.login_id))

    def as_di1ct(self):
        return {
            "feedatabaseack_id": self.feedatabaseack_id,
            "feedatabaseack_description": self.feedatabaseack_description,
            "feedatabaseack_rating": self.feedatabaseack_rating,
            "feedatabaseack_datetime": self.feedatabaseack_datetime,
            "feedatabaseack_login_id": self.feedatabaseack_login_id,
        }


database.create_all()
