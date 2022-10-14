class Car:  # class car
    def __init__(self, brand):  # constructor with brand argument
        self.brand = brand

    def print_brand(self):  # function to print car brand
        print("Brand = %s for Child class = %s" % (self.brand, type(self).__name__))


class Mazda(Car):  # child class inherited from Car
    pass


class Swift(Mazda):  # second child class inherited from Mazda
    pass


class Hotel:
    def total_no_of_people(self):
        pass


class Hilton(Hotel):
    def __init__(self, no_of_rooms, people_per_room):
        self.no_of_rooms = no_of_rooms
        self.people_per_room = people_per_room

    def total_no_of_people(self):
        total = self.no_of_rooms * self.people_per_room
        print("total no of people=", (total))


class Branch(Hilton):
    pass


class House_types:
    def __init__(self, stairs, flat):
        self.stairs = stairs
        self.flat = flat


class Apartment(House_types):
    def total_flat(self):
        total3 = self.stairs * self.flat
        print("total flats in apartment=", (total3))


class Individual_house(Apartment):
    pass
