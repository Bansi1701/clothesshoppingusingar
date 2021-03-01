from base.com.vo.state_vo import *


class StateDAO:
    def insert_state(self, state_vo):
        database.session.add(state_vo)
        database.session.commit()

    def view_state(self):
        state_vo_list = StateVO.query.all()
        return state_vo_list

    def delete_state(self, state_vo):
        state_vo_list = StateVO.query.get(state_vo.state_id)
        database.session.delete(state_vo_list)
        database.session.commit()

    def edit_state(self, state_vo):
        state_vo_list = StateVO.query.filter_by(state_id=state_vo.state_id).all()
        return state_vo_list

    def update_state(self, state_vo):
        database.session.merge(state_vo)
        database.session.commit()
