from user import User
from config import db

if __name__ == '__main__':
    supriadi = User.query.filter_by(name='supriadi').first()
    if supriadi:
        supriadi.name = 'supriadi yusuf' 
        db.session.commit()