from base import database


class StateVO(database.Model):
    __tablename__ = 'state_table'
    state_id = database.Column('state_id', database.Integer, primary_key=True, autoincrement=True)
    state_name = database.Column('state_name', database.String(100))
    state_description = database.Column('state_description', database.String(100))

    def as_dict(self):
        return {
            'state_id': self.state_id,
            'state_name': self.state_name,
            'state_description': self.state_description
        }


database.create_all()
