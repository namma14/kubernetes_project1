class Animals:
    def __init__(self,animal_type):
        self.animal_type = animal_type
        print("Animal type is:", animal_type)


class Pets(Animals):
    def __init__(self,Homepets):
        self.homepets = Homepets
        print("Yes Dogs are Home pets")


class Dogs(Pets):
    @staticmethod
    def barks(dog_name):
        print(f"{dog_name} barks")

a = Animals("Dogs")
d = Dogs("Yes")
d.barks("badal")
