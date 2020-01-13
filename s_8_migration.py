from config import app, db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate( app, db)
manager = Manager( app)

manager.add_command( 'db', MigrateCommand)

class User(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.VARCHAR(50))
    age = db.Column('age', db.Integer) 
    #address = db.Column('address', db.String(50)) # add new field

    def __str__(self):
        return self.name

if __name__ == '__main__':
    manager.run()

# 1. python s_8_migration.py db init
# 2. python s_8_migration.py db migrate
# 3. python s_8_migration.py db upgrade
# 4. if there is change again start from step 2