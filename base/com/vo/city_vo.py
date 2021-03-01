from base import database
from base.com.vo.state_vo import StateVO


class CityVO(database.Model):
    __tablename__ = 'city_table'
    city_id = database.Column('city_id', database.Integer, primary_key=True, autoincrement=True)
    city_name = database.Column('city_name', database.String(100))
    city_description = database.Column('city_description', database.String(100))
    city_state_id = database.Column('city_state_id', database.Integer, database.ForeignKey(StateVO.state_id))

    def as_dict(self):
        return {
            'city_id': self.city_id,
            'city_name': self.city_name,
            'city_description': self.city_description,
            'city_state_id': self.city_state_id
        }


database.create_all()
