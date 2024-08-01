class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f'Olá meu nome {self.name} e eu tenho {self.age} anos')

# eu = Person("vinicius", 17)
# eu.sayHello()


class Student(Person):
    def __init__(self, name, age, studentID):
        super().__init__(name, age)
        self.studentID = studentID

    def sayHello(self):
        print(f'Olá meu nome {self.name} e eu tenho {self.age} anos, ID: {self.studentID}')

tu = Student('Motuca', 18, 1)        
tu.sayHello()