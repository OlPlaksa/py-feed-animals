class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        # print("is", self.is_hungry)
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.is_hungry = is_hungry
        self.appetite = 3

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.is_hungry = is_hungry
        self.appetite = 7

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    count = 0
    for animal in animals:
        count += Animal.feed(animal)
    return count
