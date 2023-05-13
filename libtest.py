def adder(*args, **kwargs):
    result = 0
    for elem in args:
        if type(elem) == int or type(elem) == float or type(elem) == bool:
            result += elem
    for elem in kwargs.values():
        if type(elem) == int or type(elem) == float or type(elem) == bool:
            result += elem
    return result





"""
>>> 2+2
5

if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""

"""
if 2+3 == 4:
    print("In fact, 2 + 2 equals 4")

assert 2+2 == 5, "wrong calculation"

"""

"""
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")







import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="We have next logging message:%(asctime)s:%(levelname)s -%(message)s")
try:
    print(10 / 0)
except Exception:
    logging.error("Division By Zero")

"""














"""
def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                reluts = function(*args, **kwargs)
            except (exc_types) as exc:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result - {reluts}")
        return checker
    return checker

@checker(NameError, TypeError, SyntaxError)
def calculate(expression):
    return eval(expression)

@checker(Exception)
def calculateSumofTwoExp(expression1,expression2):
    return eval(expression1) + eval(expression2)






calculate("2+ff2")
calculateSumofTwoExp("2+2", "3+3")

"""




"""
def helper(work):
    work_in_memory = work
    def helperLocked(work):
        return f"I will help you with {work_in_memory}. Afterwards I will help you with {work}"
    return helperLocked

helper = helper("microsoft stocks")
print(helper("sell them"))
print(helper("buy more"))
"""


"""
class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"I will help you with {self.work}. Afterwards I will help you with {work}"

helper = Helper("homework")

print(helper("cleaning"))


"""
























"""
def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have error {exc}")
        else:
            print(f"No Errors. Result - {result}")
    return checker

@checker
def calculate(expression):
    return eval(expression)

#calculate = checker(calculate)
calculate("2/0")


def helper(work):
    work_in_memory = work
    def helperTwo(work):
        return f"I will help you with you {work_in_memory}. Afterwards I will help you with {work}"
    return helperTwo

helperTwo = helper("homework")

helperTwo("work")


print(helperTwo("cleaning"))
print(helperTwo("driving"))
print(helperTwo("cleaning"))

"""















#ry:
    #the code we need to test
#except:
    #in case of the error
#else:
    #no error
#finally:
    #just place to clean up (close all connections, clean mem...)


#class BuildingError(Exception):
 #   def __str__(self):
  #      return f"With this much materials I cannot build a house!"

#def checker_materials(amout_needed, amout):
 #   if amout_needed > amout:
  #      raise BuildingError(amout, "Not enough materials", "ddddd")
  #  else:
  #      return "enough materials"

#materials = 200
#print(checker_materials(400, materials))
#try:
 #   print(checker_materials(400, materials))
#except BuildingError as e:
#    print(e.args)

