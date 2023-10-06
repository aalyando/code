class Car:
    def __init__(self, t):
        self.t = t

    def __add__(self, other):
        return Car(t=(self.t + other.t))


car1 = Car(['a','b'])
car2 = Car(['c','d'])

car3 = car1 + car2
print(f'{car3.t}')


