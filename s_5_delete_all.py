from user import User
from config import db

if __name__ == '__main__':
    db.session.query(User).delete()
    db.session.commit() 