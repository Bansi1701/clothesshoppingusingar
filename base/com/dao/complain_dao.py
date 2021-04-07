from base import database
from base.com.vo.complain_vo import ComplainVO
from base.com.vo.login_vo import LoginVO


class ComplainDAO:
    def insert_complain(self, complain_vo):  # user insert the complain
        database.session.add(complain_vo)
        database.session.commit()

    def user_view_complain(self):  # admin side view the all complain
        complain_vo_list = database.session.query(LoginVO, ComplainVO) \
            .filter(LoginVO.login_id == ComplainVO.complain_from_login_id) \
            .all()
        return complain_vo_list

    def insert_complain_reply(self,complain_vo):
        complain_vo_list = ComplainVO.query.get(complain_vo.complain_id)
        return complain_vo_list

    def admin_view_complain(self):  # admin side view the all complain
        complain_vo_list = database.session.query(ComplainVO, LoginVO) \
            .join(LoginVO, ComplainVO.complain_from_login_id == LoginVO.login_id) \
            .all()
        return complain_vo_list

    def delete_complain(self, complain_vo):  # admin delete the complain
        complain_vo_delete = ComplainVO.query.get(complain_vo.complain_id)
        database.session.delete(complain_vo_delete)
        database.session.commit()

    def edit_complain(self, complain_vo):  # admin give the reply of complain ,fetch the complain data
        complain_vo_list = ComplainVO.query.get(complain_vo.complain_id)
        return complain_vo_list

    def update_complain(self, complain_vo):  # update data into complain table
        database.session.merge(complain_vo)
        database.session.commit()
