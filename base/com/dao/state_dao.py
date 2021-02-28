from base.com.vo.state_vo import *


class StateDAO:
    def insert_state(self,state_vo):
        database.session.add(state_vo)
        database.session.commit()

    def view_state(self):
        state_vo_list = StateVO.query.all()
        return state_vo_list