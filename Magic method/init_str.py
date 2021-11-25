class person:
    def __init__(self,name,age,relation):
        self.name = name
        self.age = age
        self.relation = relation

    def __str__(self):
        return '{} {} {} '.format(self.name, self.age, self.relation)


name = input("enter name: ")
age = int(input("enter age: "))
relation = input("enter relationship status: ")
p = person(name,age,relation)
print(p.__str__())