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

"""
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

