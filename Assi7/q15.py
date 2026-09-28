class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['category'] = "Python Class"
        return super().__new__(cls, name, bases, dct)

class ClassA(metaclass=MyMeta):
    pass

class ClassB(metaclass=MyMeta):
    pass

msg = input("Enter tag: ")
print("ClassA category:", ClassA.category, "Tag:", msg)
print("ClassB category:", ClassB.category)
