


def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i += 1



res = raise_to_the_degrees(12345, 5)
print(res)

for elem in res:
    print(elem)
print("!!!")

for elem in res:
    print(elem)



















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

