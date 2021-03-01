from base import database
from base.com.vo.city_vo import CityVO
from base.com.vo.state_vo import StateVO


class AreaVO(database.Model):
    __tablename__ = 'area_table'
    area_id = database.Column('area_id', database.Integer, primary_key=True, autoincrement=True)
    area_name = database.Column('area_name', database.String(100))
    area_pincode = database.Column('area_pincode', database.Integer)
    area_state_id = database.Column('area_state_id', database.Integer, database.ForeignKey(StateVO.state_id))
    area_city_id = database.Column('area_city_id', database.Integer, database.ForeignKey(CityVO.city_id))

    def as_dict(self):
        return {
            'area_id': self.area_id,
            'area_name': self.area_name,
            'area_pincode': self.area_pincode,
            'area_state_id': self.area_state_id,
            'area_city_id': self.area_city_id
        }


database.create_all()
