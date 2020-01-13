from config import db

class User(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.VARCHAR(50))
    age = db.Column('age', db.Integer) 

    def __str__(self):
        return self.name

if __name__ == '__main__':
    db.create_all()