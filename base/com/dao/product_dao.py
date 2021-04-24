from base.com.vo.product_vo import *


class ProductDAO:

    def insert_product(self, product_vo):
        database.session.add(product_vo)
        database.session.commit()

    def view_product(self):
        product_vo_list = database.session.query(ProductVO, SubCategoryVO, CategoryVO).join(CategoryVO,
                                                                                            ProductVO.product_category_name == CategoryVO.category_id).join(
            SubCategoryVO, ProductVO.product_subcategory_name == SubCategoryVO.subcategory_id).all()
        return product_vo_list

    def delete_product(self, product_id):
        product_vo_list = ProductVO.query.get(product_id)
        database.session.delete(product_vo_list)
        database.session.commit()
        return product_vo_list

    def selected_view_product(self, product_id):
        product_vo_list = ProductVO.query.filter_by(product_id=product_id).all()
        return product_vo_list
