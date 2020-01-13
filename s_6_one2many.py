from config import db
from person_pets import Person, Pet

if __name__ == '__main__':
    supriadi = Person(name='supriadi')
    ade = Person(name='ade')

    meong1 = Pet(name='meong1', owner=supriadi)
    meong2 = Pet(name='meong2', owner=supriadi)
    meong3 = Pet(name='meong3', owner=ade)

    db.session.add_all([ade, supriadi, meong1, meong2, meong3])
    db.session.commit()

    for pet in supriadi.pets:
        print(pet)