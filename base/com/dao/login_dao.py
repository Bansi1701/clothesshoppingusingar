from base.com.vo.login_vo import LoginVO, database


class LoginDAO:
    def validate_login(self, login_vo):
        login_vo_list = LoginVO.query.filter_by(login_username=login_vo.login_username,
                                                login_password=login_vo.login_password)
        return login_vo_list

    def insert_user(self, login_vo):
        database.session.add(login_vo)
        database.session.commit()

    def view_login(self):
        login_vo_list = LoginVO.query.all()
        return login_vo_list


    def find_login_id(self, login_vo):
        login_vo_list = LoginVO.query.filter_by(login_username=login_vo.login_username).all()
        login_id = login_vo_list[0].login_id
        return login_id

    def find_login_username(self, login_vo):
        login_vo_list = LoginVO.query.filter_by(login_id=login_vo.login_id).all()
        login_username = login_vo_list[0].login_username
        return login_username
