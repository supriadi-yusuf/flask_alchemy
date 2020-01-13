from user import User
from config import db

if __name__ == '__main__':
    supriadi = User(name='supriadi', age=38)
    db.session.add(supriadi) 

    ari = User(name='ari', age=30)
    irma = User(name='irma', age=29)
    insert = db.session.add_all([ari, irma]) 
    
    db.session.commit()