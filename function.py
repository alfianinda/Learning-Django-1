# def hello():
#     print("Hello World!")
#     print("Hello Dog!")
#     print("Hello Cat!")

# hello()
# hello()
# hello()

#

# def hello(name, age):
#     print("Hello " + name + " you are " + age + " years old")

# hello("Nina", "20")

#

# def hello(name, age):
#     print("Hello {} you are {} years old".format(name, age))

# hello("Nina", 20)

#

# def hello(name = "Inna", age = 0):
#     print("Hello {} you are {} years old".format(name, age))

# hello("Nina", 20)
# hello()

#

# def hello(name = "Inna", age = 0):
#     return "Hello {} you are {} years old".format(name, age)

# hello = hello("Nina", 20)
# print(hello)

#

# Exercise
# Create a function named trippleprint that takes a string as a parameter and prints that string 3 times in a row. So if I passed in the string hello it would print hellohellohello 
# *Be sure to only create the function, don't call it. For example, don't write trippleprint("hello") The exercise will do this for you.

def trippletprint(param):
    print(param * 3)
    # print("{}".format(param) * 3)
    # print(("Today is {}".format(param) + " ") *3)
    # print("I love {}".format(param))
    # print("{} is amazing".format(param))

trippletprint("Hello")