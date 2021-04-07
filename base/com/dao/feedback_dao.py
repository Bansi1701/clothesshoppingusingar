from base import database
from base.com.vo.feedatabaseack_vo import FeedatabaseackVO
from base.com.vo.login_vo import LoginVO


class FeedatabaseackDAO:
    def insert_feedatabaseack(self, feedatabaseack_vo):
        database.session.add(feedatabaseack_vo)
        database.session.commit()

    def user_view_feedatabaseack(self):
        feedatabaseack_vo_list = database.session.query(LoginVO, FeedatabaseackVO) \
            .filter(LoginVO.login_id == FeedatabaseackVO.feedatabaseack_login_id) \
            .all()
        return feedatabaseack_vo_list

    def admin_view_feedatabaseack(self):
        feedatabaseack_vo_list = database.session.query(FeedatabaseackVO, LoginVO) \
            .join(LoginVO, FeedatabaseackVO.feedatabaseack_login_id == LoginVO.login_id) \
            .all()
        return feedatabaseack_vo_list

    def delete_feedatabaseack(self, feedatabaseack_vo):
        feedatabaseack_vo_delete = FeedatabaseackVO.query.get(feedatabaseack_vo.feedatabaseack_id)
        database.session.delete(feedatabaseack_vo_delete)
        database.session.commit()
