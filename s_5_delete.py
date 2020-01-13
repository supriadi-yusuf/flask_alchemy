from user import User
from config import db

if __name__ == '__main__':
    supriadi = User.query.filter_by(name='supriadi yusuf').first()
    if supriadi:
        db.session.delete(supriadi)
        db.session.commit()