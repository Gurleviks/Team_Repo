class Animal:
    def __init__(self, legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs}")

    def return_legs(self):
        return self._number_of_legs


class Dog(Animal):
    def __init__(self, legs_count, name):
        super().__init__(legs_count)
        self._name = name

    def bark(self):
        print(f"{self._name} says 'Woof Woof!'")

    def get_name(self):
        return self._name


dog = Dog(4, "Wololo")
dog.count_legs()
print(dog.return_legs())
print(dog.get_name())
dog.bark()
