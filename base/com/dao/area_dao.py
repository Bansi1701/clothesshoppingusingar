from base.com.vo.area_vo import *


class AreaDAO:

    def insert_area(self, area_vo):
        database.session.add(area_vo)
        database.session.commit()

    def view_area(self):
        area_vo_list = database.session.query(AreaVO, CityVO, StateVO).join(CityVO,
                                                                            AreaVO.area_city_id == CityVO.city_id).join(
            StateVO, AreaVO.area_state_id == StateVO.state_id).all()
        return area_vo_list

    def delete_area(self, area_id):
        area_vo_list = AreaVO.query.get(area_id)
        database.session.delete(area_vo_list)
        database.session.commit()

    def edit_area(self, area_vo):
        area_vo_list = AreaVO.query.filter_by(area_id=area_vo.area_id).all()
        return area_vo_list

    def update_area(self, area_vo):
        database.session.merge(area_vo)
        database.session.commit()
