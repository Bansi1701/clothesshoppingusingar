from base.com.vo.city_vo import *
from base.com.vo.state_vo import *


class CityDAO:

    def insert_city(self, city_vo):
        database.session.add(city_vo)
        database.session.commit()

    def view_city(self):
        city_vo_list = database.session.query(CityVO, StateVO).join(StateVO,
                                                                    CityVO.city_state_id == StateVO.state_id).all()
        return city_vo_list

    def delete_city(self, city_vo):
        city_vo_list = CityVO.query.get(city_vo.city_id)
        database.session.delete(city_vo_list)
        database.session.commit()

    def edit_city(self, city_vo):
        city_vo_list = CityVO.query.filter_by(city_id=city_vo.city_id).all()
        return city_vo_list

    def update_city(self, city_vo):
        database.session.merge(city_vo)
        database.session.commit()

    def view_ajax_area_city(self, city_vo):
        city_vo_list = CityVO.query.filter_by(
            city_state_id=city_vo.city_state_id).all()
        return city_vo_list