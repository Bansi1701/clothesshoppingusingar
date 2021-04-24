from base.com.vo.user_vo import *

class RegisterDAO:

    def insert_user(self, register_vo):
        database.session.add(register_vo)
        database.session.commit()

    def find_user_id(self, user_vo):
        user_vo_list = RegisterVO.query.filter_by(user_login_id =user_vo.user_login_id).all()
        user_id = user_vo_list[0].user_id
        return user_id

