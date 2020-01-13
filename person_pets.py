from config import db

class Person(db.Model):

    __tablename__ = 'tb_person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    pets = db.relationship('Pet', backref='owner') # first parameter must be name of class which this is related to

    def __str__(self):
        return self.name

class Pet(db.Model):

    __tablename__ = 'tb_pet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    owner_id = db.Column( db.Integer, 
                          db.ForeignKey('tb_person.id')
                          )
    
    def __str__(self):
        return self.name

if __name__ == '__main__':
    db.create_all()

