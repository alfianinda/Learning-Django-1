# class Dog:
#     dogInfo = "Hey dogs are cool"

#     def bark(self, str):
#         print("BARK!!" + str)

# mydog = Dog()
# # mydog.bark()
# mydog.bark("guk guk guk")

# mydog.name = "Fido"
# mydog.age = 16
# print(mydog.name)
# print(mydog.age)

# Dog.dogInfo = "Hey there"
# print(Dog.dogInfo)

### init method

class Dog:
    dogInfo = "Hey dogs are cool"

    def bark(self, str):
        print("BARK!!" + str)

mydog = Dog()
# mydog.bark()
mydog.bark("guk guk guk")

mydog.name = "Fido"
mydog.age = 16
print(mydog.name)
print(mydog.age)

Dog.dogInfo = "Hey there"
print(Dog.dogInfo)