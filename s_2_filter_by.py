from user import User

if __name__ == '__main__':
    user = User.query.filter_by(id=10).first()
    if user :
        print("nama : %s, age : %s" % ( user.name, user.age))