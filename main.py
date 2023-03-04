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
        self.home = House()


    def get_job(self):
        self.job = Job(job_list)
    def get_car(self):
        self.car = Car(brands_of_cars)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.hunger > 95:
                self.home.food -= 100 - self.hunger
                self.hunger = 100
            else:
                self.hunger += 5
                self. home.food -= 5

    def drive_car(self):
        if self.car.drive():
            return True
        else:
            if self.car.fuel < self.car.consumption:
                self.shopping("fuel")
            else:
                self.car.repair()
                return False
    def shopping(self, items):
        if items == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.pump_gas()

        if not self.drive_car():
            return

        if items == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50


    def work(self):
        if not self.drive_car():
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.hunger -= 3

    def chill(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass





class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Python developer": {"salary": 40, "gladness_less": 5},
    "Java developer": {"salary": 55, "gladness_less": 15},
    "C# developer": {"salary": 50, "gladness_less": 10},
    "C++ developer": {"salary": 60, "gladness_less": 25},
    "Swift developer": {"salary": 55, "gladness_less": 20}
}

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0
        #add space

class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.max_fuel = brand_list[self.brand]["fuel"]
        self.fuel = self.max_fuel
        self.max_durability = brand_list[self.brand]["durability"]
        self.durability = self.max_durability
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.fuel >= self.consumption and self.durability > 0:
            self.fuel -= self.consumption
            self.durability -= 1
            return True
        else:
            print("The car cannot move")
            return False
    def pump_gas(self):
        self.fuel = self.max_fuel
        #calculate the cost depending on galons

    def repair(self):
        self.durability = self.max_durability
        #repair only for +20 check under max value



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

car1 = Car(brands_of_cars)
car2 = Car(brands_of_cars)

print(car1.brand)
print(car2.brand)