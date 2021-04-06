from base.com.vo.product_vo import *


class ProductDAO:

    def insert_product(self,product_vo):
        database.session.add(product_vo)
        database.session.commit()

    def view_product(self):
        product_vo_list = database.session.query(ProductVO, SubCategoryVO, CategoryVO).join(CategoryVO,
                                                                                   ProductVO.product_category_name == CategoryVO.category_id).join(
            SubCategoryVO, ProductVO.product_subcategory_name == SubCategoryVO.subcategory_id).all()
        return product_vo_list
