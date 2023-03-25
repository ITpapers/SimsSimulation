#class Parent:
#    classmethods and attrs

#class Parent2:
#    classmethods and attrs

#class Child(Parent1,Parent2):
#    classmethods and attrs

#class Class1:
 #   var = 20
 #   def __init__(self):
  #      self.var = 10

#class Class2(Class1):
 #   def __init__(self):
  #      print(self.var)
   #     super().__init__()
    #    print(self.var)
     #   print(super().var)

#ccc = Class2()


class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128
    def calculate(self):
        print("Calculating...")

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"
    def display(self):
        print("I display the image")

class SmartPhone(Display,Computer):
    def print_info(self):
        print(self.memory)
        print(self.resolution)
        print(self.model)


iphone = SmartPhone(model="iPhone 15")
iphone.print_info()