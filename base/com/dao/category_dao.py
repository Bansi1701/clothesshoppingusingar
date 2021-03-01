from base.com.vo.category_vo import *


class CategoryDAO:
    def insert_category(self, category_vo):
        database.session.add(category_vo)
        database.session.commit()

    def view_category(self):
        category_vo_list = CategoryVO.query.all()
        return category_vo_list

    def delete_category(self, category_vo):
        category_vo_list = CategoryVO.query.get(category_vo.category_id)
        database.session.delete(category_vo_list)
        database.session.commit()

    def edit_category(self, category_vo):
        category_vo_list = CategoryVO.query.filter_by(category_id=category_vo.category_id).all()
        return category_vo_list

    def update_category(self, category_vo):
        database.session.merge(category_vo)
        database.session.commit()
