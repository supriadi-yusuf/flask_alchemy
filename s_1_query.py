from user import User

if __name__ == '__main__':
    print("%-30s %s" % ('name', 'age'))
    print('---------                   ------')

    users = User.query.all()    
    for user in users:
        print("%-30s %s" % (user.name, user.age))

    print()

    user = User.query.first()
    print("%-30s %s" % (user.name, user.age))
