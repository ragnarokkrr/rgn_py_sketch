bob = ('Bob', 30, 'Male')
jane = ('Jane', 29, 'Female')
print bob
print jane[0]

for p in [bob, jane]:
    print '%s is a %d old %s' % p

import collections
# Person = collections.namedtuple('Person', 'name age gender')
Person = collections.namedtuple('Person', ['name', 'age', 'gender'])

print 'type:', type(Person)

bob2 = Person(name='Bob2', age=30, gender='male')
jane2 = Person(name='Jane2', age=29, gender='female')
print bob2, jane2.name

for p in [bob2, jane2]:
    print '%s is a %d old %s' % p
