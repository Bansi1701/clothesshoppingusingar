from base import database


class LoginVO(database.Model):
    __tablename__ = 'login_table'
    login_id = database.Column('login_id', database.Integer, primary_key=True, autoincrement=True)
    login_username = database.Column('login_username', database.String(100), nullable=False)
    login_password = database.Column('login_password', database.String(100), nullable=False)
    login_role = database.Column('login_role', database.String(100), nullable=False)
    login_status = database.Column('login_status', database.String(100), nullable=False)
    login_secretkey = database.Column('login_secretkey', database.String(100), nullable=False)

    def as_dict(self):
        return {
            'login_id': self.login_id,
            'login_username': self.login_username,
            'login_password': self.login_password,
            'login_role': self.login_role,
            'login_status': self.login_status,
            'login_secretkey': self.login_secretkey
        }


database.create_all()
