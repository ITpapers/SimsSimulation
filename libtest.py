#ry:
    #the code we need to test
#except:
    #in case of the error
#else:
    #no error
#finally:
    #just place to clean up (close all connections, clean mem...)


class BuildingError(Exception):
    def __str__(self):
        return f"With this much materials I cannot build a house!"

def checker_materials(amout_needed, amout):
    if amout_needed > amout:
        raise BuildingError(amout, "Not enough materials")
    else:
        return "enough materials"

materials = 200

try:
    print(checker_materials(400, materials))
except BuildingError as error:
    print(error.args)

