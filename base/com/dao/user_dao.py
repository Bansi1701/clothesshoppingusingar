from base.com.vo.user_vo import *


class RegisterDAO:

    def insert_user(self, register_vo):
        database.session.add(register_vo)
        database.session.commit()

