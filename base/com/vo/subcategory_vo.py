from base import database
from base.com.vo.category_vo import CategoryVO


class SubCategoryVO(database.Model):
    __tablename__ = 'subcategory_table'
    subcategory_id = database.Column('subcategory_id', database.Integer, primary_key=True, autoincrement=True)
    subcategory_name = database.Column('subcategory_name', database.String(100), nullable=False)
    subcategory_description = database.Column('subcategory_description', database.String(100), nullable=False)
    subcategory_category_id = database.Column('subcategory_category_id', database.Integer,
                                              database.ForeignKey(CategoryVO.category_id))

    def as_dict(self):
        return {
            'subcategory_id': self.subcategory_id,
            'subcategory_name': self.subcategory_name,
            'subcategory_description': self.subcategory_description,
            'subcategory_category_id': self.subcategory_category_id
        }


database.create_all()
