from flask import *

from base import *
from base.com.dao.city_dao import CityDAO
from base.com.vo.city_vo import CityVO


@app.route('/ajax_area_city', methods=['get'])
def ajax_area_city():
    try:

        city_dao = CityDAO()
        city_vo = CityVO()

        city_vo.city_state_id = request.args.get('stateId')
        city_vo_list = city_dao.view_ajax_area_city(city_vo)

        ajax_area_city = [i.as_dict() for i in city_vo_list]
        print(ajax_area_city)

        return jsonify(ajax_area_city)

    except Exception as ex:
        print('ajax_area_city route exception occured>>>>>>>>>>', ex)
