from base.com.vo.city_vo import *
from base.com.vo.state_vo import *


class CityDAO:

    def insert_city(self, city_vo):
        database.session.add(city_vo)
        database.session.commit()

    def view_city(self):
        city_vo_list = database.session.query(CityVO, StateVO).join(StateVO,CityVO.city_state_id == StateVO.state_id).all()
        return city_vo_list