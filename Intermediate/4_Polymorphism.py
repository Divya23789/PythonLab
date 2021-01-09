class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says WOOF!"
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says Meow!"

N = Dog("Niko")
F = Cat("Felix")
#Method1
# print(Dog("Niko").speak())
# print(Cat("Felix").speak())

#Method2
# for pet in [N, F]:
#     print(type(pet))
#     print(pet.speak())

#Method3
# def pet_speak(pet):
#     print(pet.speak())
# pet_speak(N)
# pet_speak(F)


