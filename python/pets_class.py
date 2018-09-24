class Pets(object):
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def pets_available(self):

        print ("I have %s dogs"% (len(self.pets)))
    
    def my_pets_profile(self):
        for pet in self.pets:
            print ("%s is %s"%(pet.__getattribute__("name"), pet.__getattribute__("age")))

    def pet_class(self):
        for pet in self.pets:
            if pet.__getattribute__("vertebrate") != "mammal":
                print ("Non-mammal available")
                return self.pets
            else:
                print ("And they are all mammals, of course")

class Dog(object):

    def __init__(self, name, age, vertebrate, is_hungry = True):
        self.name = name
        self. age = age
        self.vertebrate = vertebrate
        self.is_hungry = is_hungry

    def eat(self):

        self.is_hungry = False

if __name__ == "__main__":
    tom = Dog("Tom", 6, "mammal")
    fletcher = Dog("Fletcher", 7, "mammal")
    larry = Dog("Larry", 9, "mammal")
    my_pets = Pets()
    my_pets.add_pet(tom)
    my_pets.add_pet(fletcher)
    my_pets.add_pet(larry)
    my_pets.pets_available()
    my_pets.my_pets_profile()
    my_pets.pet_class()











