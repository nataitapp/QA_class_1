__author__ = 'nata'

def changeJob(person, newjob):
    person['job'] = newjob

def  happyBirthday(person):
    person['age'] += 1
    return person

person1 = {'name': 'Tom',
           'job': 'button-pusher',
            'age': 34}

person2 = {'name': 'John',
           'job': 'level-puller',
            'age': 41}

print '%s is a %s' % (person1['name'], person1['job'])
print '%s is a %s' % (person2['name'], person1['job'])

changeJob(person1, 'CEO')
happyBirthday(person1,)
print '%s is a %s' % (person1['name'], person1['job'])
print '%s is %s' % (person1['name'], person1['age'])
print '%s is %s and he is a %s' % (person1['name'], person1['age'], person1['job'])


#   ------SAME-------

class Person():
    def __init__(self, name, job, age):
        self._name = name
        self._job = job
        self._age = age

    def changeJob(self, newjob):
        self._job = newjob

    def happyBirthday(self):
        self._age += 1

Tom = Person('Tom', 'button-pusher', 34)
John = Person('John', 'lever-pusher', 42)

print Tom._job
Tom.changeJob('teacher')
print Tom._job



