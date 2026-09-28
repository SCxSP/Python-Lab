class AutoCategory(type):
    def __new__(cls, name, bases, dct):
        dct['category'] = "Python Class"
        return super().__new__(cls, name, bases, dct)

class A(metaclass=AutoCategory):
    pass

class B(metaclass=AutoCategory):
    pass

tag = input("Enter tag: ")
print("A category:", A.category, "Tag:", tag)
print("B category:", B.category)
