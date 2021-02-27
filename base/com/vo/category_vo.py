from base import database


class CategoryVO(database.Model):
    __tablename__ = 'category_table'
    category_id = database.Column('category_id', database.Integer, primary_key=True, autoincrement=True)
    category_name = database.Column('category_name', database.String(100))
    category_description = database.Column('category_description', database.String(100))

    def as_dict(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'category_description': self.category_description
        }


database.create_all()
