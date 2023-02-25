import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.hunger = 50
        self.car = car
        self.job = job
        self.home = home

    def get_home(self):
        pass

    def get_job(self):
        pass
    def get_car(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def chill(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass





class Job:
    def __init__(self):
        pass


class Home:
    def __init__(self):
        pass

class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.durability = brand_list[self.brand]["durability"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.fuel >= self.consumption and self.durability > 0:
            self.fuel -= self.consumption
            self.durability -= 1
            return True
        else:
            print("The car cannot move")
            return False



brands_of_cars = {
    "Toyota":{"fuel": 18, "durability": 150, "consumption": 3},
    "BMW":{"fuel": 20, "durability": 80, "consumption": 5},
    "Honda":{"fuel": 14, "durability": 130, "consumption": 3},
    "Mercedes":{"fuel": 21, "durability": 95, "consumption": 6},
    "Audi":{"fuel": 19, "durability": 90, "consumption": 5},
    "Ford":{"fuel": 17, "durability": 120, "consumption": 4},
}


#nick = Human("Nick")
#jeb = Human("Jeb")

car = Car("Toyota")

#car.add_passenger(nick)
#car.add_passenger(jeb)
car.print_passengers()