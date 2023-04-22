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




Make calculator with FULL an HALF Expressions like *2 OR +8 to prev result
Assignment 2: We have an unfinished calculator function:

def calculate(expression):
    return eval(expression)

Decorate it so that it works as a full-fledged calculator.
Also, the decorator should ensure that the code is stable in execution, while pointing out the problem.





calculate("2+ff2")
calculateSumofTwoExp("2+2", "3+3")






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

