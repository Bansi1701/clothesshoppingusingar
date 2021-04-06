from base.com.vo.subcategory_vo import *


class SubCategoryDAO:
    def insert_subcategory(self, subcategory_vo):
        database.session.add(subcategory_vo)
        database.session.commit()

    def view_subcategory(self):
        subcategory_vo_list = database.session.query(SubCategoryVO, CategoryVO).join(CategoryVO,
                                                                                     SubCategoryVO.subcategory_category_id == CategoryVO.category_id).all()
        return subcategory_vo_list

    def delete_subcategory(self, subcategory_id):
        subcategory_vo_list = SubCategoryVO.query.get(subcategory_id)
        database.session.delete(subcategory_vo_list)
        database.session.commit()

    def edit_subcategory(self, subcategory_vo):
        subcategory_vo_list = SubCategoryVO.query.filter_by(subcategory_id=subcategory_vo.subcategory_id).all()
        return subcategory_vo_list

    def update_subcategory(self, subcategory_vo):
        database.session.merge(subcategory_vo)
        database.session.commit()

    def view_ajax_product_subcategory(self,subcategory_vo):
        subcategory_vo_list = SubCategoryVO.query.filter_by(subcategory_category_id=subcategory_vo.subcategory_category_id).all()
        return subcategory_vo_list
