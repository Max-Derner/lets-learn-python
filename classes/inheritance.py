from dunder_methods import Cat


class Huntress(Cat):
    percent_ease_of_murdering: int

    def __init__(self, percent_ease_of_murdering: int, name: str, colour: str, age: int):  # noqa: E501
        super().__init__(name, colour, age)
        self.percent_ease_of_murdering = percent_ease_of_murdering

    def __str__(self):
        return f"{super().__str__()}, a can murder with {self.percent_ease_of_murdering}% efficacy"  # noqa: E501


if __name__ == "__main__":
    ilana = Huntress(percent_ease_of_murdering=100,
                     name='Ilana',
                     age=4,
                     colour='Shadow')
    print(str(ilana))
