

class Cat:
    name: str
    colour: str
    age: int

    # A really good website on these methods here:
    # https://www.tutorialsteacher.com/python/magic-methods-in-python

    def __init__(self, name: str, colour: str, age: int):
        self.name = name
        self.colour = colour
        self.age = age

    def __str__(self):  # give string representation of object
        return f"A {self.colour.lower()} cat named {self.name.title()}, who is {self.age} year{'s' if self.age > 1 else ''} old"  # noqa: E501

    def __eq__(self, other):  # allows equality comparison of objects (use '==')
        if isinstance(other, Cat):
            truth = self.name.upper() == other.name.upper()
            truth = self.age == other.age and truth
            truth = self.colour.upper() == other.colour.upper() and truth
            return truth
        else:
            return False

    def __ne__(self, other):  # allows non-equality comparison of objects (use '!=')
        return not self.__eq__(other)

    def __lt__(self, other):  # allows less than comparison of objects (use '<')
        if not isinstance(other, type(self)):
            raise TypeError(f"'<' not supported between instances of 'Cat' and {type(other).__name__}")  # noqa: E501
        if self.age < other.age:
            return True
        else:
            return False

    def __le__(self, other):  # allows less than or equal to comparison of objects (use '<=')
        if not isinstance(other, type(self)):
            raise TypeError(f"'<=' not supported between instances of 'Cat' and {type(other).__name__}")  # noqa: E501
        if self.age <= other.age:
            return True
        else:
            return False

    def __gt__(self, other):  # allows greater than comparison of objects (use '>')
        if not isinstance(other, type(self)):
            raise TypeError(f"'>' not supported between instances of 'Cat' and {type(other).__name__}")  # noqa: E501
        if self.age > other.age:
            return True
        else:
            return False

    def __ge__(self, other):  # allows greater than or equal to comparison of objects (use '>=')
        if not isinstance(other, type(self)):
            raise TypeError(f"'>=' not supported between instances of 'Cat' and {type(other).__name__}")  # noqa: E501
        if self.age >= other.age:
            return True
        else:
            return False

    def __hash__(self):
        return hash(str(self))


if __name__ == "__main__":
    abbi = Cat(name='abbi', colour='Void', age=4)

    print(str(abbi))

    Abbi = Cat(name='Abbi', colour='void', age=4)

    print(f'Abbi == abbi: {Abbi == abbi}')

    print(f'Abbi == 1: {Abbi == 1}')

    bad_cat = 'A bad cat'
    print(f'Abbi != \'{bad_cat}\': {Abbi != bad_cat}')

    print(f'Abbi > 1 {Abbi > 1}')
