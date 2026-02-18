# Array
# 1 Bakhsh
list()
tuple()
set()

# 2 Bakhsh
dict()


# list
# 1. Tartib Dare
# 2. Taghir Pazire
# 3. Tekrari Darad
students = [
    'Mohammad Heydari',      # 0  -5
    'Taha Ardavan',          # 1  -4
    'Ali Alavi',             # 2  -3
    'Atiye Azari',           # 3  -2
    'Mohammad Reza Naghili', # 4  -1
]
x = [1, True, False, None, '', 1.0]

'''
print(students)
print(students[0])
print(students[-1])
print(students[1:-1])
print(students[1:])
'''


# tuble
# 1. Tartib Darad
# 2. Taghir Pazir nist
# 3. Tekrari Darad
students = ('Mohammad', 'Taha Ardavan')


# set
# 1. Tartib Nadarad
# 2. Taghir Pazir Hast
# 3. Tekrari Nadarad
students = {'Mohammad', 'Taha Ardavan', 'Mohammad'}
x = {1, 1, True, True, False, 0, 1.0, 20, 20, 40, 50, 10}


# dict
# 0. 2 bakhshi
# 1. Tartib Darad
# 2. Taghir Pazir Hast
# 3. Tekrari Nadarad AMA bakhsh Dovom mitavanad bashad
user = {
    'first_name': 'Mohammad',
    'last_name': 'Heydari',
    'age': 26,
    'students': ['Taha Ardavan', 'Atiye Azari'],
    'books': 26,
}
print(f'{user['first_name']} {user['last_name']}')

books = {
    0: 'Gift from sky',
    1: 'Math',
    20: 'Physic',
}
print(books[20])