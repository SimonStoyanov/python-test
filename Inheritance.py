# Ineritance
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
