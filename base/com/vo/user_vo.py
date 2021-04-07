from base import database
from base.com.vo.city_vo import CityVO
from base.com.vo.state_vo import StateVO
from base.com.vo.login_vo import LoginVO


class RegisterVO(database.Model):
    __tablename__ = 'user_table'
    user_id = database.Column('user_id', database.Integer, primary_key=True, autoincrement=True)
    user_firstname = database.Column('user_firstname', database.String(100))
    user_lastname = database.Column('user_lastname', database.String(100))
    user_gender = database.Column('user_gender', database.String(100))
    user_address= database.column('user_address',database.String(255))
    user_pincode = database.Column('user_pincode', database.Integer)
    user_email = database.column('user_email', database.String(255))
    user_password = database.column('user_password', database.String(255))
    user_state_id = database.Column('user_state_id', database.Integer, database.ForeignKey(StateVO.state_id))
    user_city_id = database.Column('user_city_id', database.Integer, database.ForeignKey(CityVO.city_id))
    user_login_id = database.Column('user_login_id', database.Integer, database.ForeignKey(LoginVO.login_id))


    def as_dict(self):
        return {
            'user_id': self.user_id,
            'user_firstname': self.user_firstname,
            'user_lastname': self.user_lastname,
            'user_gender': self.user_gender,
            'user_address': self.user_address,
            'user_pincode': self.user_pincode,
            'user_state_id': self.user_state_id,
            'user_city_id': self.user_city_id,
            'user_login_id': self.user_login_id
        }


database.create_all()
