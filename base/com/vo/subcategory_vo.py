from base import database


class SubcategoryVO:
    __tablename__ = 'subcategory_table'
    subcategory_id = database.Column('subcategory_id', database.Integer, primary_key=True, autoincrement=True)
    subcategory_name = database.Column('subcategory_name',database.String(100))
    subcategory_description = database.Column('subcategory_description', database.String(100))
