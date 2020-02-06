# class Dog:
#     dogInfo = "Hey dogs are cool"

#     def bark(self, str):
#         print("BARK!!" + str)

# mydog = Dog() #new Dog
# mydog.bark()
# mydog.bark("guk guk guk")

# mydog.name = "Fido"
# mydog.age = 16
# print(mydog.name)
# print(mydog.age)

# Dog.dogInfo = "Hey there"
# print(Dog.dogInfo)

### init method

# class Dog:
#     def __init__(self, name, age, furcolor):
#         self.name = name
#         self.age = age
#         self.furcolor = furcolor

#     def bark(self, str):
#         print("BARK" + str)

# mydog = Dog() #new Dog
# print(mydog.age)

### Exercise
# Add a method to the Car class called age that returns how old the car is (2018 - year)
# *Be sure to return the age, not print it*

class Car:
    def age(self, year):
        return "2018 - {}".format(year)

yearCar = Car()
print(yearCar.age(2019))

